from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from langsmith import Client
import streamlit as st
import os 
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

# os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
# LangSmith

os.environ['LANGCHAIN_ENDPOINT'] ="https://api.smith.langchain.com"
os.environ['LANGCHAIN_TRAICING_V2'] = "true"
os.environ['LANGCHAIN_API_KEY'] = str(os.getenv("LANGCHAIN_API_KEY"))
os.environ['LANGCHAIN_PROJECT'] = "pt-respectful-wasabi-44"

client = Client()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are helpful assistant. Please response to user queries"),
        ("user","Question:{question}")
    ]
)

st.title("Langchain Demo with OPENAI API")

input_text = st.text_input("Search the topic you want")

# Ollama
llm = Ollama(model = "llama3")
output_parser = StrOutputParser()

chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))