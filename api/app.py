from fastapi import FastAPI
from langserve import add_routes
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import os
import uvicorn
import warnings
warnings.filterwarnings("ignore")

llm = Ollama(model="llama3.2")


app = FastAPI(
    title="Langchain-Chatbot-Server",
    version="1.0",
    description="A simple chatbot api server"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful and fun assistant. Please help by responding to the user's questions"),
        ("user","Question:{question}")
    ]
)

add_routes(
    app,
    prompt|llm,
    path="/personal-assistant"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
