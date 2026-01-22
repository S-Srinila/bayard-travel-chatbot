import streamlit as st
from chatbot import chatbot_response

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Bayard Vacations – Travel Assistant",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #141E30, #243B55);
    font-family: 'Segoe UI', sans-serif;
}

/* Header */
h1 {
    color: #ffffff !important;
    font-weight: 700;
    text-shadow: 0px 2px 10px rgba(0, 0, 0, 0.6);
}

.subtitle {
    color: #E0E0E0;
    font-size: 16px;
}


/* Chat area */
.chat-box {
    max-width: 750px;
    margin: auto;
    padding-bottom: 140px;
}

/* User message */
.user-msg {
    background: #DCF8C6;
    color: black;
    padding: 12px 16px;
    border-radius: 18px 18px 4px 18px;
    margin: 8px 0;
    max-width: 80%;
    margin-left: auto;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}

/* Bot message */
.bot-msg {
    background: #ffffff;
    color: black;
    padding: 12px 16px;
    border-radius: 18px 18px 18px 4px;
    margin: 8px 0;
    max-width: 80%;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}

/* Fixed input container */
.input-container {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: #ffffff;
    padding: 12px;
    box-shadow: 0 -4px 10px rgba(0,0,0,0.2);
}

/* Floating bot icon */
.bot-icon {
    position: fixed;
    bottom: 90px;
    right: 25px;
    background: #25D366;
    color: white;
    width: 55px;
    height: 55px;
    border-radius: 50%;
    text-align: center;
    font-size: 28px;
    line-height: 55px;
    box-shadow: 0 6px 15px rgba(0,0,0,0.4);
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("🌍Welcome To Bayard Vacations – Travel Assistant")
st.markdown(
    "<div class='subtitle'>Ask me about packages, destinations, pricing, or booking process.</div>",
    unsafe_allow_html=True
)

# ---------------- SESSION STATE ----------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- CHAT DISPLAY ----------------
st.markdown('<div class="chat-box">', unsafe_allow_html=True)

for speaker, message in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f'<div class="user-msg">{message}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-msg">{message}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- INPUT (BOTTOM FIXED) ----------------
st.markdown('<div class="input-container">', unsafe_allow_html=True)

col1, col2 = st.columns([6, 1])
with col1:
    user_input = st.text_input(
        "Message",
        placeholder="Type your message...",
        label_visibility="collapsed"
    )
with col2:
    send = st.button("➤", key="send", help="Send message")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- MESSAGE HANDLING ----------------
if send and user_input:
    bot_reply = chatbot_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", bot_reply))
    st.rerun()


# ---------------- FLOATING ICON ----------------
st.markdown('<div class="bot-icon">🤖</div>', unsafe_allow_html=True)

