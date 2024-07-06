import streamlit as st
import InvokeAgent as agenthelper

# Streamlit app
st.title('Amazon Bedrock Chat Interface')

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Function to display chat history
def display_chat():
    for chat in st.session_state['chat_history']:
        st.write(f"You: {chat['question']}")
        st.write(f"Bedrock: {chat['answer']}")

# User input
prompt = st.text_input('Ask a question:')
event = {
  "sessionId": "MYSESSION",
  "question": prompt
}
if st.button('Send'):
    if prompt:
        response = agenthelper.lambda_handler(event, None)
        st.session_state['chat_history'].append({'question': prompt, 'answer': response['body']})
        display_chat()
    else:
        st.write("Please enter a question.")

# Display chat history
display_chat()