# LMS with Streamlit

This project is a Learning Management System (LMS) developed using **Streamlit** for the front-end, **SQLite3** for the back-end database, and **Markdown** for managing content. It allows teachers and students to collaborate in a structured learning environment.

## Features

### Authentication
- **Sign Up**: Users can create accounts as either `Student` or `Teacher`.
- **Login**: Secure login for existing users based on role (`Student` or `Teacher`).
- **Logout**: Users can safely log out, clearing session data.

### Content Management (For Teachers)
- **Manage Topics**: Add topics, subtopics, and sub-subtopics to organize content.
- **Add Content**: Teachers can add new pages, including Markdown-based text and multimedia (images or videos).
- **Edit Content**: Modify existing pages for better collaboration and improvement.

### Content Navigation (For Students and Teachers)
- **Sidebar Navigation**: Topics, subtopics, and sub-subtopics are organized in a hierarchical structure.
- **Markdown Rendering**: Pages are displayed with Markdown formatting, allowing rich text and media content.
- **Pagination**: Navigate between sub-subtopics with `Previous` and `Next` buttons.

### Database and Storage
- **SQLite3 Database**: Stores user information (username, password, role).
- **File Management**:
  - Markdown files for storing content.
  - `uploads/` directory for storing multimedia files.

### Footer
A footer displaying the current year and attribution.

---

## Directory Structure
```
├── data/                # Directory for Markdown files
├── uploads/             # Directory for uploaded multimedia files
├── topics.json          # JSON file storing topics and subtopics
├── users.db             # SQLite3 database file
├── app.py               # Main application file
├── README.md            # Documentation file
```

---

## How to Run the Project

### Prerequisites
1. Install Python (>=3.7).
2. Install dependencies:
   ```bash
   pip install streamlit
   ```

### Run the App
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```
2. Start the application:
   ```bash
   streamlit run app.py
   ```

### Access the App
- Open the local URL displayed in the terminal (e.g., `http://localhost:8501`).

---

## Key Files

### `app.py`
Main application logic, including authentication, content management, and rendering.

### `topics.json`
Stores the hierarchical structure of topics, subtopics, and sub-subtopics.

### `users.db`
SQLite3 database storing user credentials and roles.

---

## Future Enhancements
- Add a richer user interface with custom CSS or Bootstrap integration.
- Implement role-based access control for specific features.
- Enhance multimedia support with better file handling.
- Add analytics for tracking student progress.

---

## Author
This project was created by [Your Name]. Feel free to reach out for feedback or contributions!
