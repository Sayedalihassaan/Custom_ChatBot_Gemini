from langchain.schema import SystemMessage, HumanMessage, AIMessage
import streamlit as st
from streamlit_chat import message
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.exceptions import LangChainException



# Load environment variables
load_dotenv(override=True)
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Validate API key
if not GOOGLE_API_KEY:
    st.error("Google API key not found. Please set it in the .env file.")
    st.stop()

# Initialize Gemini model
try:
    chat = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        api_key=GOOGLE_API_KEY,
        temperature=0.7,  
        max_tokens=1000   
    )
except Exception as e:
    st.error(f"Failed to initialize Gemini model: {str(e)}")
    st.stop()



# Page configuration
st.set_page_config(
    page_title="Custom Gemini Assistant",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)


# Custom CSS for better styling
st.markdown("""
    <style>
    .stTextInput > div > input {
        border-radius: 10px;
        padding: 10px;
    }
    .stButton > button {
        border-radius: 10px;
        background-color: #4CAF50;
        color: white;
    }
    .chat-container {
        max-height: 500px;
        overflow-y: auto;
        padding: 10px;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)


# Initialize session state for messages
if 'messages' not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a helpful assistant with a friendly tone.")
    ]

# Main UI
st.title("🤖 Custom Gemini Assistant")
st.markdown("Chat with your AI assistant powered by Google's Gemini model.")

# Sidebar for system message and settings
with st.sidebar:
    st.header("Assistant Settings")
    system_message = st.text_input(
        label="System Role",
        value="You are a helpful assistant with a friendly tone.",
        help="Define the assistant's behavior or persona."
    )
    
    # Option to clear chat history
    if st.button("Clear Chat History"):
        st.session_state.messages = [SystemMessage(content=system_message)]
        st.success("Chat history cleared!")

# Update system message if changed
if system_message and st.session_state.messages[0].content != system_message:
    st.session_state.messages[0] = SystemMessage(content=system_message)

# Chat input
with st.form(key="chat_form", clear_on_submit=True):
    user_prompt = st.text_input("Send a Message", placeholder="Type your message here...")
    submit_button = st.form_submit_button("Send")

# Handle user input
if submit_button and user_prompt:
    st.session_state.messages.append(HumanMessage(content=user_prompt))
    try:
        with st.spinner("Generating response..."):
            response = chat(st.session_state.messages)
            st.session_state.messages.append(AIMessage(content=response.content))
    except LangChainException as e:
        st.error(f"Error generating response: {str(e)}")
    except Exception as e:
        st.error("An unexpected error occurred. Please try again.")

# Display chat history
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for i, msg in enumerate(st.session_state.messages[1:], start=1):
    is_user = isinstance(msg, HumanMessage)
    message(
        msg.content,
        is_user=is_user,
        key=f"msg_{i}",
        avatar_style="identicon" if is_user else "bottts",
        seed="user" if is_user else "bot"
    )
st.markdown('</div>', unsafe_allow_html=True)

# Display token usage (optional, for debugging or user info)
if st.checkbox("Show Token Usage"):
    try:
        token_count = chat.get_num_tokens_from_messages(st.session_state.messages)
        st.write(f"Total tokens used in this session: {token_count}")
    except Exception:
        st.write("Token usage information unavailable.")