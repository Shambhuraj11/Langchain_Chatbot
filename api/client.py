import requests 
import streamlit as st

def get_llama_response(input_text):
    response = requests.post(
        url="http://localhost:8000/essay/invoke",
        json= {"input":{"topic":input_text}}
    
    )
    
    return response.json()['output']


st.title("Langchain APP with LLAMA3")
input_text = st.text_input("Write Topic name")

if input_text:
    st.write(get_llama_response(input_text))

