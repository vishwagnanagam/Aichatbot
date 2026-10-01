import streamlit as st
import ollama

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

with st.sidebar:
    st.title("🤖 AI Chatbot")
    st.write("Your personal AI assistant")
    st.divider()
    st.subheader("⚙️ About")
    st.write("• Streamlit")
    st.write("• Ollama")
    st.write("• Llama 3.2")
    st.divider()
    st.caption("Built as a learning project")

st.title("🤖 AI Chatbot!")
st.subheader("Your AI Assistant")
st.write("Ask questions and get answers instantly using Llama 3.2.")
prompt = st.text_input("Enter your prompt", placeholder="Ask me anything...")
if st.button("Send"):
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
