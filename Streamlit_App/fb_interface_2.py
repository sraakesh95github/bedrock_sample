import streamlit as st
import InvokeAgent as agenthelper
import time

# Set the title of the app
st.title("Chat Interface")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Type a message..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Simulate assistant response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        # full_response = ""
        event = {
            "sessionId": "MYSESSION",
            "question": prompt
        }
        response = agenthelper.lambda_handler(event, None)
        full_response = response['body']
        assistant_response = "Hello! How can I help you today?"
        
        # Simulate typing effect
        for chunk in assistant_response.split():
            full_response += chunk + " "
            response_placeholder.markdown(full_response + "▌")
            time.sleep(0.05)
        
        response_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})