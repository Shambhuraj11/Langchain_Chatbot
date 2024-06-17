import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.retrieval import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser 
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRAICING_V2'] = "true"
os.environ['LANGCHAIN_ENDPOINT'] = os.getenv('LANGCHAIN_ENDPOINT')
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
os.environ['LANGCHA(IN_PROJECT'] = os.getenv("LANGCHAIN_PROJECT")

groq_api_key = os.environ['GROQ_API_KEY']

if 'vector' not in st.session_state:
    st.session_state.embeddings = OllamaEmbeddings(model="all-minilm")
    st.session_state.loaders = WebBaseLoader("https://en.wikipedia.org/wiki/High_courts_of_India")
    st.session_state.docs = st.session_state.loaders.load()

    st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap = 100)
    st.session_state.f_docs = st.session_state.text_splitter.split_documents(documents=st.session_state.docs)

    st.session_state.vectors = FAISS.from_documents(st.session_state.f_docs,st.session_state.embeddings)

st.title("Chatbot with GROQ")
llm = ChatGroq(groq_api_key= groq_api_key,model="llama3-8b-8192")

prompt = ChatPromptTemplate.from_template(
    """Please think step by step.Answer the questions based on provided context only.
    **Context**:
    {context}
    
    **Question**:
    {input}
    """
    
)

doc_chain = create_stuff_documents_chain(llm=llm,prompt=prompt,output_parser=StrOutputParser())
retriever = st.session_state.vectors.as_retriever()
retriever_chain = create_retrieval_chain(retriever,doc_chain)

inpt = st.text_input("On which topic you wanna chat!!")

if st.button(label="Submit"):
    if inpt:
        with st.spinner(text="In Progress....."):
            try:
                response = retriever_chain.invoke({"input":inpt})
                st.write(response['answer'])
            except Exception as e:
                st.error(f"An exception occurred {e}")
    else:
        st.warning("Please enter a topic before submitting")            
