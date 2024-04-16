import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

st.title("🐦 REVCO", help="AI Code Reviwer")
prompt = st.text_area("Enter Python code below to review", height=200)

if st.button("Generate Review") == True:
    genai.configure(api_key= os.environ.get("API_KEY"))

    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(f""" You are a helpful and polite assistant,
                                    Given following python code you have to review it and 
                                    find the errors and bugs and list them(separately) with ordered list with short explanation,
                                    after that generate the correct code with header-text 'Corrected Code': {prompt}
                                    """)
    st.header("Code Review")
    st.write(response.text)
