import streamlit as st
from utils.chat import get_jarvis_response
import time
import random
import re

# Preloader wait once
if "preloaded" not in st.session_state:
    time.sleep(random.uniform(3, 4))
    st.session_state.preloaded = True
    st.rerun()

# Init session state
if "chat_started" not in st.session_state:
    st.session_state.chat_started = False
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "last_rendered_index" not in st.session_state:
    st.session_state.last_rendered_index = -1

# Page config
st.set_page_config(page_title="Jarvis - AI", layout="centered")

# Typing effect only for new bot messages
def type_writer(text, delay=0.01):
    displayed = ""
    for char in text:
        displayed += char
        time.sleep(delay)
        yield displayed

# Custom CSS
st.markdown("""
    <style>
        .message {
            color: #000000;
            margin: 1rem 0;
            padding: 1rem;
            border-radius: 1rem;
            max-width: 80%;
            animation: messageAppear 0.3s ease-out;
        }

        .user-message {
            background: linear-gradient(129deg, #cbffe8, #ff97ff);
            margin-left: auto;
            border-bottom-right-radius: 5px;
        }

        .bot-message {
            background: linear-gradient(135deg, #e5b8fb, #e0f2b6);
            border-bottom-left-radius: 5px;
        }

        .bot-message strong, .bot-message u {
            font-weight: bold;
            text-decoration: underline;
        }

        @keyframes messageAppear {
            from { transform: translateY(10px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }

        .center {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            padding-top: 100px;
            height: 50vh;
            color: white;
        }

        .gradient-text {
            background: linear-gradient(to right, #5ec2dd, #e989ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 48px;
            font-weight: bold;
            font-family: ui-rounded;
        }

        .st-emotion-cache-seewz2 h2 {
            font-size: 2.25rem;
            padding: 1rem 0px;
            font-family: ui-monospace;
        }

        .st-emotion-cache-seewz2 h1 {
            background: linear-gradient(to right, #5ec2dd, #e989ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2.75rem;
            font-weight: 700;
            padding: 1.25rem 0px 1rem;
            font-family: fangsong;
        }
    </style>
""", unsafe_allow_html=True)

# Landing page if no chat started
if not st.session_state.chat_started:
    st.markdown("""
        <div class="center">
            <div class="gradient-text">Hello, Partner</div>
            <h2>I am Jarvis, How can I help you Today?</h2>
            <p>Type something below to start chatting with Jarvis</p>
        </div>
    """, unsafe_allow_html=True)

    with st.form(key="start_chat_form"):
        init_input = st.text_input("Enter your message to Jarvis:", placeholder="Ask me anything...")
        if st.form_submit_button("Start Chat") and init_input.strip():
            st.session_state.chat_started = True
            response = get_jarvis_response(init_input)
            st.session_state.chat_history.append(("You", init_input))
            st.session_state.chat_history.append(("Jarvis", response))
            st.session_state.last_rendered_index = -1
            st.rerun()

else:
    # Chat UI with header
    st.markdown("""
        <h1 style='font-family: ui-rounded; font-size: 2.75rem; background: linear-gradient(to right, #5ec2dd, #e989ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>
            <img src="https://img.icons8.com/ios-filled/50/1b96ae/robot.png" style="height: 36px; vertical-align: middle; margin-right: 10px;" />
            Jarvis - Your AI Assistant
        </h1>
    """, unsafe_allow_html=True)

    # Chat display
    chat_container = st.container()
    with chat_container:
        for i, (sender, message) in enumerate(st.session_state.chat_history):
            icon = "https://img.icons8.com/ios-filled/50/1b96ae/user.png" if sender == "You" else "https://img.icons8.com/ios-filled/50/ca34ca/robot.png"
            message_class = "user-message" if sender == "You" else "bot-message"

            # Handle code blocks differently
            if message.startswith("```") and sender == "Jarvis":
                # Extract language and code content
                lang_match = re.match(r"```(\w+)", message)
                lang = lang_match.group(1) if lang_match else ""
                code_content = "\n".join(message.strip("`").split("\n")[1:-1])  # Skip ```lang and ending ```

                if i > st.session_state.last_rendered_index:
                    placeholder = st.empty()
                    for partial in type_writer("Here is the code:"):
                        placeholder.markdown(f'''
                            <div class="message {message_class}">
                                <img src="{icon}" style="height: 24px; vertical-align: middle; margin-right: 10px;" />
                                {partial}
                            </div>
                        ''', unsafe_allow_html=True)
                    st.code(code_content, language=lang)
                    st.session_state.last_rendered_index = i
                else:
                    st.markdown(f'''
                        <div class="message {message_class}">
                            <img src="{icon}" style="height: 24px; vertical-align: middle; margin-right: 10px;" />
                            Here is the code:
                        </div>
                    ''', unsafe_allow_html=True)
                    st.code(code_content, language=lang)

            else:
                # Normal message rendering with markdown support
                formatted_msg = message.replace("**", "<strong>").replace("__", "<u>").replace("\n", "<br>")
                formatted_msg = formatted_msg.replace("<strong><u>", "<strong><u>").replace("</u></strong>", "</u></strong>")

                if i > st.session_state.last_rendered_index and sender == "Jarvis":
                    placeholder = st.empty()
                    for partial in type_writer(formatted_msg):
                        placeholder.markdown(f'''
                            <div class="message {message_class}">
                                <img src="{icon}" style="height: 24px; vertical-align: middle; margin-right: 10px;" />
                                {partial}
                            </div>
                        ''', unsafe_allow_html=True)
                    st.session_state.last_rendered_index = i
                else:
                    st.markdown(f'''
                        <div class="message {message_class}">
                            <img src="{icon}" style="height: 24px; vertical-align: middle; margin-right: 10px;" />
                            {formatted_msg}
                        </div>
                    ''', unsafe_allow_html=True)

    # Chat input
    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_input("Type your message:", placeholder="Ask me anything...")
        submitted = st.form_submit_button("🚀 Send")

        if submitted and user_input.strip():
            with st.spinner("Jarvis is thinking..."):
                response = get_jarvis_response(user_input)
                st.session_state.chat_history.append(("You", user_input))
                st.session_state.chat_history.append(("Jarvis", response))
                st.rerun()
