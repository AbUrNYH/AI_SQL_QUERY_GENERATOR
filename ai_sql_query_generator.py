import os
import re
from sqlalchemy import create_engine
from dotenv import load_dotenv
from langchain.sql_database import SQLDatabase
from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Database connection
user = os.getenv("USER")
password = os.getenv("PASSWORD")
host = os.getenv("HOST")
database = os.getenv("DATABASE")

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")
db = SQLDatabase(engine)

# OpenAI model setup
base_url = os.getenv("BASE_URL")
api_key = os.getenv("API_KEY")
model = os.getenv("MODEL")

LLM = ChatOpenAI(
    openai_api_base=base_url,
    openai_api_key=api_key,
    model_name=model,
    streaming=True
)

# Function to clean SQL query
def clean_sql_query(response):
    match = re.search(r"SELECT .*", response, re.DOTALL | re.IGNORECASE)
    if match:
        query = match.group(0)
        query = query.replace("\n", " ").replace("`", "").strip()
        return query
    return response.strip()

# Function to get schema
def get_schema(db):
    return db.get_table_info()

def run_query(query):
    try:
        return db.run(query)
    
    except Exception as e:
        return f"SQL ERROR : {e}"

def get_sql_query(user_question):
    sql_prompt = ChatPromptTemplate.from_template("""
    Based on the table schema below, write a SQL query that would answer the user's question:
    {schema}

    # SQL Query Generation

    Question: {question}
    SQL Query:""")

    sql_chain = (
        RunnablePassthrough.assign(schema=lambda x: get_schema(db))
        | sql_prompt
        | LLM.bind(stop=["\nSQLResult:"])
        | StrOutputParser()
    )

    # User question
    sql_query = sql_chain.invoke({"question": user_question})
    
    return clean_sql_query(sql_query)

def get_response(user_question, sql_query):
    # Response Generation
    response_prompt = ChatPromptTemplate.from_template("""
    Based on the table schema below, question, sql query, and sql response, write a natural language response:
    {schema}

    Question: {question}
    SQL Query: {query}
    SQL Response: {response}
    """)
    
    full_chain = (
        RunnablePassthrough.assign(
            query=lambda x: sql_query,  # Ensure sql_chain is called correctly
            schema=lambda x: get_schema(db),
            response=lambda vars: run_query(sql_query),
        )
        | response_prompt
        | LLM
    )

    # Test full chain
    final_response = full_chain.stream({"question": user_question})
    
    return final_response

def main():
    while True:
        user_question = input("")
        print()
        
        sql_query = get_sql_query(user_question)
        
        response = get_response(user_question, sql_query)
        history_chat = ""
        
        for chunk in response:
            print(chunk.content, end="", flush=True)
            history_chat += chunk.content
            
        print("\n")
        
if __name__ == "__main__":
    main()