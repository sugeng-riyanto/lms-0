import streamlit as st

st.title("Multiple Choice Question")

question = "What is the capital of France?"
options = ["Madrid", "Rome", "Paris", "Berlin"]

answer = st.radio(question, options)

if st.button("Submit"):
    if answer == "Paris":
        st.success("Correct! Paris is the capital of France.")
    else:
        st.error("Wrong answer. Try again!")
