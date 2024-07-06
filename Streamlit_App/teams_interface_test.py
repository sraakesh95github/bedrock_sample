import streamlit as st
import InvokeAgent as agenthelper

# Initialize session state for message history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Function to send a message and get the response from agenthelper
def send_message():
    if st.session_state.user_message != "":
        user_message = st.session_state.user_message
        st.session_state.messages.append(("User", user_message))
        st.session_state.user_message = ""

        # Create an event for the lambda_handler
        event = {
            "sessionId": "MYSESSION",
            "question": user_message
        }

        # Get the bot's response from the lambda_handler
        bot_response = agenthelper.lambda_handler(event, None)
        st.session_state.messages.append(("Bot", bot_response["body"]))

# Sidebar for user input
st.sidebar.header("Chat Input")
user_message = st.sidebar.text_input("Type your message here:", key="user_message", on_change=send_message)

# Main chat interface
st.title("Chat Interface")

chat_container = st.container()
with chat_container:
    for sender, message in st.session_state.messages:
        st.markdown(f"**{sender}:** {message}")

# JavaScript to auto-scroll to the bottom of the chat
scroll_js = """
<script>
    var chatContainer = document.getElementsByClassName("element-container")[0];
    chatContainer.scrollTop = chatContainer.scrollHeight;

    // Function to automatically resize the text input box
    function autoResizeInput() {
        const input = document.getElementsByTagName("textarea")[0];
        input.style.height = 'auto';
        input.style.height = (input.scrollHeight) + 'px';
    }

    // Attach the event listener to the text input box
    document.addEventListener("input", autoResizeInput);

    // Initial resize to fit the default content
    autoResizeInput();
</script>
"""
st.markdown(scroll_js, unsafe_allow_html=True)
