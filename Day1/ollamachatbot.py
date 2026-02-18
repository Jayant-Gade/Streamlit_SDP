import os
import streamlit as st
from langchain_community.llms import Ollama  # Corrected from 11ms / 011ama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser # Corrected from StroutputParser

# 1. Define the Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the question asked"),
    ("user", "Question:{question}")
])

# 2. Streamlit UI Setup
st.set_page_config(page_title="LangChain Demo", page_icon="🤖")
st.title("LangChain Demo with Gemma 2")

input_text = st.text_input("What question do you have in mind?")

# 3. Initialize Ollama Model (Ensure Ollama is running locally!)
llm = Ollama(model="gemma2:2b")
output_parser = StrOutputParser()

# 4. Create the Chain (Using LangChain Expression Language - LCEL)
chain = prompt | llm | output_parser

# 5. Invoke the chain if there is input
if input_text:
    with st.spinner("Thinking..."):
        response = chain.invoke({"question": input_text})
        st.write(response)

