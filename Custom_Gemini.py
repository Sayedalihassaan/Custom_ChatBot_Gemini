from langchain.schema import SystemMessage , AIMessage , HumanMessage 
import streamlit as st 
import os 
from dotenv import load_dotenv 
from langchain_google_genai import ChatGoogleGenerativeAI


 _ = load_dotenv(override=True)
 
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") 


st.set_page_confing( page_title = "Custom Assistant" , page_icon='🤖' )

st.subheader("Custom Chat Gemini 🤖") 
 
chat = ChatGoogleGenerativeAI(model = "gemini-1.5-pro" , api_key = GOOGLE_API_KEY) 
 
 
system_message = st.text_input(label = "System Role") 
 
 
user_message = st.text_input(label = "Send a Message") 


if "Messages" not in st.session_state : 
    st.session_state.messages = [] 
    
    
with st.sidebar : 
    if system_message : 
        if not any(isinstance(x , SystemMessage) for x in st.session_state.messages) :
            
             st.session_state.messages.append(SystemMessage(content = system_message))


    if user_message :
        st.session_state.messages.append()