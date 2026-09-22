import streamlit as st
import ollama
st.title("AI Chatbot")
st.write("Welcome to Chatbot")
prompt = st.text_input("Enter your prompt")
if st.button("send"):
    if prompt:
        response = ollama.chat(
            model = "llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        st.write(response["message"]["content"])
    else:
        st.warning("Please enter a prompt.")