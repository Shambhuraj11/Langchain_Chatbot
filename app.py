from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
import streamlit  as st

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
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


#OPENAI LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))

