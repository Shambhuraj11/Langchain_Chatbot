from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
from dotenv import load_dotenv
import os 
load_dotenv()

os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRAICING_V2']= os.getenv("LANGCHAIN_TRAICING_V2")
os.environ['LANGCHAIN_ENDPOINT'] = "https://api.smith.langchain.com"
os.environ['LANGCHAIN_PROJECT'] = os.getenv("LANGCHAIN_PROJECT")

app = FastAPI(
    title= "Lanchain Server",
    version="1.0",
    description="Langchain APP"
)

model = Ollama(model='llama3')

prompt1 = ChatPromptTemplate.from_template(
    "Write me sentences about {topic} in 3 lines"
)

add_routes(
    app,
    prompt1|model,
    path="/essay"

)

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)