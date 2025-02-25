import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

@st.cache_resource
def load_model():
    return genai.GenerativeModel('gemini-pro')

model = load_model()
chat = model.start_chat(history=[])

st.set_page_config(page_title="CyberSimbax Chatbot")
st.title("🦁 CyberSimbax A.I Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How can I help you?"}]

# Display messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Your message"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        response = chat.send_message(prompt)
        ai_response = response.text
    except Exception as e:
        ai_response = f"Error: {str(e)}"

    with st.chat_message("assistant"):
        st.markdown(ai_response)
    
    st.session_state.messages.append({"role": "assistant", "content": ai_response})