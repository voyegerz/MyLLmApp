import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st
import time

load_dotenv()

RESPONSE = """ """

def stream_data():
    for word in RESPONSE.split(" "):
        yield word + " "
        time.sleep(0.04)


genai.configure(api_key= os.environ.get("API_KEY"))

st.title("🐯 DASTOR", help="AI Based Data Science Tutor - Conversational Agent")
st.write("your personal data science tutor.")
st.write("ask me anything about topics related to data science...")
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest", 
                            system_instruction="""Your name is 🐯 DASTOR, and
                                                You are data science expert tutor and a helpful and polite assistant,
                                                you will provide explaination to the given data science topic
                                                and resolve the user's queries be specific and brief, if the topic is not related to the data science or ai 
                                                then you can politely request the user to ask questions related to data science domain.
                                                if you asked who made you then answer with this response - me 🐯 DASTOR was created by Neeraj Kumar 😍.
                                            """)
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

chat = model.start_chat(history=st.session_state["chat_history"])

for msg in chat.history:
    st.chat_message(msg.role).write(msg.parts[0].text)

prompt = st.chat_input("Ask Data science queries...")

if prompt:
    st.chat_message("user").write(prompt)
    response = chat.send_message(prompt)
    RESPONSE = response.text
    st.chat_message("🐯").write_stream(stream_data)
    st.session_state["chat_history"]=chat.history