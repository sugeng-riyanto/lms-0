import streamlit as st
import os
import json
import sqlite3
from datetime import datetime

# Directories
CONTENT_DIR = "data"
UPLOAD_DIR = "uploads"
TOPICS_FILE = "topics.json"
DATABASE = "users.db"

# Ensure directories exist
os.makedirs(CONTENT_DIR, exist_ok=True)
os.makedirs(UPLOAD_DIR, exist_ok=True)

# SQLite database setup
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_user(username, password, role):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def authenticate_user(username, password, role):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ? AND role = ?", (username, password, role))
    user = cursor.fetchone()
    conn.close()
    return user

# Initialize database
init_db()

# Load and save JSON
def load_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return {}

def save_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

# Topics and Subtopics Management
def load_topics():
    return load_json(TOPICS_FILE)

def save_topics(topics):
    save_json(TOPICS_FILE, topics)

def add_topic(title, subtopics):
    topics = load_topics()
    if title not in topics:
        topics[title] = {}
    for subtopic in subtopics:
        if subtopic not in topics[title]:
            topics[title][subtopic] = []
    save_topics(topics)

def add_sub_subtopic(topic, subtopic, sub_subtopics):
    topics = load_topics()
    if topic in topics and subtopic in topics[topic]:
        topics[topic][subtopic].extend(sub_subtopics)
        topics[topic][subtopic] = list(set(topics[topic][subtopic]))  # Remove duplicates
        save_topics(topics)

# Add Topic/Subtopic Functionality for Teachers
def manage_topics():
    st.subheader("Manage Topics")
    topic = st.text_input("Enter Topic Title", key="manage_topic_title")
    subtopic = st.text_input("Enter Subtopic Title", key="manage_subtopic_title")
    sub_subtopics = st.text_area("Enter Sub-Subtopics (one per line)", key="manage_sub_subtopics").split("\n")
    sub_subtopics = [sub.strip() for sub in sub_subtopics if sub.strip()]

    if st.button("Save Sub-Subtopics", key="manage_topic_save_button"):
        if topic and subtopic and sub_subtopics:
            add_topic(topic, [subtopic])
            add_sub_subtopic(topic, subtopic, sub_subtopics)
            st.success(f"Added sub-subtopics under {topic} > {subtopic} successfully!")
        else:
            st.error("Please provide a topic, subtopic, and at least one sub-subtopic.")

# Edit Existing Content
def edit_content():
    st.subheader("Edit Content")
    topics = load_topics()

    topic = st.selectbox("Select Topic", list(topics.keys()), key="edit_content_topic")
    subtopic = st.selectbox("Select Subtopic", list(topics[topic].keys()), key="edit_content_subtopic")
    sub_subtopic = st.selectbox("Select Sub-Subtopic", topics[topic][subtopic], key="edit_content_sub_subtopic")

    page_filename = f"{topic}_{subtopic}_{sub_subtopic}.md"
    page_path = os.path.join(CONTENT_DIR, page_filename)

    content = ""
    if os.path.exists(page_path):
        with open(page_path, "r") as f:
            content = f.read()

    updated_content = st.text_area("Edit Markdown Content:", value=content, key="edit_content_text")

    if st.button("Save Changes", key="edit_content_save_button"):
        with open(page_path, "w") as f:
            f.write(updated_content)
        st.success(f"Content for {topic} > {subtopic} > {sub_subtopic} updated successfully!")

# Render Sidebar Topics for Navigation
def render_sidebar_topics():
    topics = load_topics()
    selected_topic = st.sidebar.selectbox("Select Topic", list(topics.keys()), key="sidebar_select_topic")

    if selected_topic:
        subtopics = list(topics[selected_topic].keys())
        selected_subtopic = st.sidebar.selectbox("Select Subtopic", subtopics, key="sidebar_select_subtopic")

        if selected_subtopic:
            sub_subtopics = topics[selected_topic][selected_subtopic]
            if "current_sub_subtopic" not in st.session_state or st.session_state.current_sub_subtopic not in sub_subtopics:
                st.session_state.current_sub_subtopic = sub_subtopics[0] if sub_subtopics else None

            selected_sub_subtopic = st.sidebar.radio(
                "Select Sub-Subtopic",
                sub_subtopics,
                index=sub_subtopics.index(st.session_state.current_sub_subtopic) if sub_subtopics else 0,
                key="sidebar_select_sub_subtopic",
            )
            st.session_state.current_sub_subtopic = selected_sub_subtopic

            return selected_topic, selected_subtopic, selected_sub_subtopic, sub_subtopics

    return None, None, None, []

# Render Markdown Content
def render_page(topic, subtopic, sub_subtopic, sub_subtopics):
    page_filename = f"{topic}_{subtopic}_{sub_subtopic}.md"
    page_path = os.path.join(CONTENT_DIR, page_filename)
    if os.path.exists(page_path):
        with open(page_path, "r") as f:
            content = f.read()
        st.markdown(content, unsafe_allow_html=True)
    else:
        st.write(f"No content available for {topic} > {subtopic} > {sub_subtopic}. Please add it.")

    current_index = sub_subtopics.index(sub_subtopic) if sub_subtopics else -1
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if current_index > 0:
            if st.button("Previous", key="prev_button"):
                st.session_state.current_sub_subtopic = sub_subtopics[current_index - 1]
                st.experimental_rerun()
    with col3:
        if current_index < len(sub_subtopics) - 1:
            if st.button("Next", key="next_button"):
                st.session_state.current_sub_subtopic = sub_subtopics[current_index + 1]
                st.experimental_rerun()

    year = datetime.now().year
    st.markdown(f"<footer style='text-align: center;'>@{year} aqeelainstruments.co.id</footer>", unsafe_allow_html=True)

# Add New Content
def add_content():
    st.subheader("Add New Page")
    topics = load_topics()

    topic = st.selectbox("Select Topic", list(topics.keys()), key="add_content_topic")
    subtopic = st.selectbox("Select Subtopic", list(topics[topic].keys()), key="add_content_subtopic")
    sub_subtopic = st.selectbox("Select Sub-Subtopic", topics[topic][subtopic], key="add_content_sub_subtopic")

    markdown = st.text_area("Paste Markdown Content:", key="add_content_markdown")
    multimedia = st.file_uploader("Upload Multimedia", type=["png", "jpg", "mp4"], key="add_content_file")

    multimedia_path = None
    if multimedia:
        multimedia_path = os.path.join(UPLOAD_DIR, multimedia.name)
        with open(multimedia_path, "wb") as f:
            f.write(multimedia.read())

    if st.button("Save Page", key="add_content_save_button"):
        if topic and subtopic and sub_subtopic and markdown:
            filename = f"{topic}_{subtopic}_{sub_subtopic}.md"
            save_path = os.path.join(CONTENT_DIR, filename)
            with open(save_path, "w") as f:
                content = markdown
                if multimedia_path:
                    if multimedia_path.endswith(".mp4"):
                        content += f"\n\n<video controls src='{multimedia_path}'></video>"
                    else:
                        content += f"\n\n![Image]({multimedia_path})"
                f.write(content)
            st.success(f"Page for {topic} > {subtopic} > {sub_subtopic} added successfully!")
        else:
            st.error("Please fill in all fields!")

# Authentication and Sign-Up
def login():
    with st.sidebar:
        st.subheader("Login")
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")
        role = st.selectbox("Role", ["Student", "Teacher"], key="login_role")
        if st.button("Login", key="login_button"):
            user = authenticate_user(username, password, role)
            if user:
                st.session_state.user_role = role
                st.session_state.username = username
                st.session_state.logged_in = True
                st.success(f"Logged in as {role}")
            else:
                st.error("Invalid credentials!")
        st.markdown("---")
        if st.button("Sign Up", key="login_signup_button"):
            st.session_state.show_signup = True

def sign_up():
    with st.sidebar:
        st.subheader("Sign Up")
        new_username = st.text_input("New Username", key="signup_username")
        new_password = st.text_input("New Password", type="password", key="signup_password")
        new_role = st.selectbox("Role", ["Student", "Teacher"], key="signup_role")
        if st.button("Create Account", key="signup_create_button"):
            if new_username and new_password:
                success = add_user(new_username, new_password, new_role)
                if success:
                    st.success(f"Account created for {new_username} as {new_role}!")
                    st.session_state.show_signup = False
                    st.session_state.logged_in = True
                    st.session_state.user_role = new_role
                    st.session_state.username = new_username
                else:
                    st.error("Username already exists. Please choose a different username.")
            else:
                st.error("Please fill in all fields.")

# Logout
def logout():
    if st.sidebar.button("Logout", key="logout_button"):
        st.session_state.clear()
        st.session_state["logged_in"] = False
        st.session_state["show_signup"] = False
        st.stop()

# Main App
def main():
    st.set_page_config(page_title="LMS", layout="wide")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "user_role" not in st.session_state:
        st.session_state.user_role = None
    if "username" not in st.session_state:
        st.session_state.username = None
    if "show_signup" not in st.session_state:
        st.session_state.show_signup = False

    if not st.session_state.logged_in:
        if st.session_state.show_signup:
            sign_up()
        else:
            login()
    else:
        topic, subtopic, sub_subtopic, sub_subtopics = render_sidebar_topics()

        logout()

        if st.session_state.user_role == "Teacher":
            manage_topics()
            add_content()
            edit_content()

        if topic and subtopic and sub_subtopic:
            render_page(topic, subtopic, sub_subtopic, sub_subtopics)

if __name__ == "__main__":
    main()
