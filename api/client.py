import requests
import streamlit as st

def get_llm_response(input_text):
    response = requests.post("http://localhost:8000/personal-assistant/invoke",
    json = {"input":{"question":input_text}})

    return response.json()["output"]

# streamlit framework
st.title("Personal Assistant Chatbot with Ollama")
input_text = st.text_input("How can I help you today?")

if input_text:
    st.write(get_llm_response(input_text))