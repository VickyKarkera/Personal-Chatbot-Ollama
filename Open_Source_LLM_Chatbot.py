from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv
import warnings
warnings.filterwarnings("ignore")

os.environ["LANGSMITH_TRACING_V2"] = "true"

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful and fun assistant. Please help by responding to the user's questions"),
        ("user","Question:{question}")
    ]
)

# Streamlit Framework
st.title("Personal Assistant Chatbot with Ollama")
input_text = st.text_input("Hi! How can I assist you today?")

# Ollama LLM
llm = Ollama(model="llama3.2")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))