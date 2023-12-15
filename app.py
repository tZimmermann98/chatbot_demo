import time
import streamlit as st

DEMO_RESPONSE = "This is a demo response."

def demo_response(response):
    """Simulate a response from the assistant."""
    for char in response:
        yield char

# Styling
st.markdown("""
    <style>
    div[data-testid="chatAvatarIcon-user"] {
        background-color: #1F93AC;
    }
    div[data-testid="chatAvatarIcon-assistant"] {
        background-color: #3D1D78;
    }
    </style>
    """, unsafe_allow_html=True)

# Page intro
st.title("< Assistant Name >")
st.caption("Assistant Description")
st.divider()

# Chat
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Your Welcome Message Here"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Process user input
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        full_response = ""
        message_placeholder = st.empty()
        for chunk in demo_response(DEMO_RESPONSE):
            full_response += chunk
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})