from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os 
from dotenv import load_dotenv

load_dotenv()

# os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
# LangSmith
os.environ['LANGCHAIN_TRAICING_V2'] = os.getenv("LANGCHAIN_TRAICING_V2")
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are helpful assistant. Please response to user queries"),
        ("user","Question:{question}")
    ]
)

st.title("Langchain Demo with OPENAI API")

input_text = st.text_input("Search the topic you want")

llm = Ollama(model = "llama3")