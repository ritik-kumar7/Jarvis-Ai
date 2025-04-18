import streamlit as st
from utils.chat import get_jarvis_response
import time
import random
import re

# Preloader with animation
if "preloaded" not in st.session_state:
    with st.spinner(""):
        preloader_html = """
        <style>
            .preloader {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: #0f0c29;
                display: flex;
                justify-content: center;
                align-items: center;
                z-index: 9999;
                transition: opacity 0.5s;
            }
            
            .orb {
                width: 80px;
                height: 80px;
                border-radius: 50%;
                background: linear-gradient(45deg, #5ec2dd, #e989ff);
                animation: pulse 1.5s infinite;
                box-shadow: 0 0 50px rgba(94,194,221,0.5);
            }
            
            @keyframes pulse {
                0% { transform: scale(0.8); opacity: 0.8; }
                50% { transform: scale(1.2); opacity: 1; }
                100% { transform: scale(0.8); opacity: 0.8; }
            }
        </style>
        <div class="preloader">
            <div class="orb"></div>
        </div>
        """
        st.markdown(preloader_html, unsafe_allow_html=True)
        time.sleep(random.uniform(2, 3))
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
st.set_page_config(page_title="Jarvis - AI Assistant", layout="centered", page_icon="https://i.imgur.com/mvMfOa5.png")

# Enhanced CSS
st.markdown("""
    <style>
        /* Main background */
        .stApp {
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            min-height: 100vh;
        }

        /* Chat messages */
        .message {
            color: #ffffff;
            margin: 1.5rem 0;
            padding: 1.2rem;
            border-radius: 20px;
            max-width: 85%;
            animation: messageAppear 0.4s cubic-bezier(0.18, 0.89, 0.32, 1.28);
            position: relative;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.1);
        }

        .user-message {
            background: linear-gradient(145deg, rgb(255 82 248 / 32%), rgb(105 244 255 / 38%));
            margin-left: auto;
            box-shadow: 5px 5px 15px rgba(0,0,0,0.2),
                       -2px -2px 10px rgba(255,255,255,0.05);
        }

        .bot-message {
            background: linear-gradient(145deg, rgba(229,184,251,0.15), rgba(224,242,182,0.15));
            box-shadow: 5px 5px 15px rgba(0,0,0,0.2),
                       -2px -2px 10px rgba(255,255,255,0.05);
        }

        /* Message icons */
        .message-icon {
            height: 37px;
            width: 37px;
            border-radius: 50%;
            object-fit: cover;
            border: 2px solid rgba(255,255,255,0.2);
            padding: 0px;
            position: absolute;
            top: -18px;
            left: -9px;
            background: #0f0c29;
        }

        /* Input styling */
        .stTextInput input {
            background: rgba(255,255,255,0.1) !important;
            border: 1px solid rgba(255,255,255,0.2) !important;
            color: white !important;
            border-radius: 15px !important;
            padding: 12px 20px !important;
        }

        .stTextInput input:focus {
            box-shadow: 0 0 15px rgba(94,194,221,0.5) !important;
            border: 1px solid #5ec2dd !important;
        }

        /* Send button */
        .stButton button {
            background: linear-gradient(45deg, #5ec2dd, #e989ff) !important;
            color: white !important;
            border: none !important;
            border-radius: 15px !important;
            padding: 12px 30px !important;
            font-weight: bold !important;
            transition: all 0.3s !important;
        }

        .stButton button:hover {
            transform: scale(1.05);
            box-shadow: 0 0 25px rgba(94,194,221,0.4);
        }

        /* Header styling */
        .main-header {
            background: linear-gradient(45deg, #5ec2dd, #e989ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2.75rem !important;
            text-shadow: 0 0 30px rgba(94,194,221,0.4);
            padding: 1rem 0 !important;
        }

        /* Landing page */
        .landing-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            
            text-align: center;
            animation: fadeIn 1s ease-out;
        }

        .gradient-text {
            background: linear-gradient(to right, #5ec2dd, #e989ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 4rem;
            font-weight: bold;
            margin-bottom: 1rem;
            text-shadow: 0 0 20px rgba(94,194,221,0.5);
            font-family: ui-rounded;
        }

        .subtitle {
            color: rgba(255,255,255,0.8);
            font-size: 1.5rem;
            margin-bottom: 2rem;
            font-family: ui-rounded;
        }

        /* Floating particles background */
        .particles {
            position: fixed;
            width: 100%;
            height: 100%;
            z-index: -1;
        }

        /* Animations */
        @keyframes float {
            0% { transform: translateY(0) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(180deg); }
            100% { transform: translateY(0) rotate(360deg); }
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes messageAppear {
            from { transform: translateY(10px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }

        /* Scrollbar styling */
        ::-webkit-scrollbar {
            width: 8px;
        }

        ::-webkit-scrollbar-track {
            background: rgba(0,0,0,0.1);
        }

        ::-webkit-scrollbar-thumb {
            background: linear-gradient(45deg, #5ec2dd, #e989ff);
            border-radius: 4px;
        }
    </style>
""", unsafe_allow_html=True)

# Add floating particles effect
st.markdown("""
    <div class="particles">
        <style>
            .particle {
                position: absolute;
                background: radial-gradient(circle, rgba(94,194,221,0.5) 0%, rgba(233,137,255,0.5) 100%);
                border-radius: 50%;
                animation: float 15s infinite linear;
            }
        </style>
        <script>
            for(let i=0; i<30; i++) {
                const particle = document.createElement('div');
                particle.className = 'particle';
                particle.style.width = Math.random()*4+2+'px';
                particle.style.height = particle.style.width;
                particle.style.left = Math.random()*100+'%';
                particle.style.top = Math.random()*100+'%';
                particle.style.animationDuration = Math.random()*10+10+'s';
                document.querySelector('.particles').appendChild(particle);
            }
        </script>
    </div>
""", unsafe_allow_html=True)

# Typing effect only for new bot messages
def type_writer(text, delay=0.01):
    displayed = ""
    for char in text:
        displayed += char
        time.sleep(delay)
        yield displayed

# Landing page if no chat started
if not st.session_state.chat_started:
    st.markdown("""
        <div class="landing-container">
            <div class="gradient-text">Hello, Partner</div>
            <div class="subtitle">I am Jarvis, your AI assistant</div>
            <div style="font-size: 1rem; color: rgba(255,255,255,0.6); margin-bottom: 2rem;">
                How can I help you today?
            </div>
        </div>
    """, unsafe_allow_html=True)

    with st.form(key="start_chat_form"):
        cols = st.columns([3, 1])
        with cols[0]:
            init_input = st.text_input("Enter your message to Jarvis:", placeholder="Ask me anything...", label_visibility="collapsed")
        with cols[1]:
            if st.form_submit_button("Start Chat", use_container_width=True) and init_input.strip():
                st.session_state.chat_started = True
                response = get_jarvis_response(init_input)
                st.session_state.chat_history.append(("You", init_input))
                st.session_state.chat_history.append(("Jarvis", response))
                st.session_state.last_rendered_index = -1
                st.rerun()

else:
    # Chat UI with enhanced header
    st.markdown("""
        <h1 class="main-header">
            <img src="https://i.imgur.com/mvMfOa5.png" style="height: 64px; vertical-align: middle; margin-right: 15px;">
            Jarvis AI Assistant
        </h1>
    """, unsafe_allow_html=True)

    # Chat display
    chat_container = st.container()
    with chat_container:
        for i, (sender, message) in enumerate(st.session_state.chat_history):
            icon = "https://img.icons8.com/fluency/48/user-male-circle.png" if sender == "You" else "https://i.imgur.com/mvMfOa5.png"
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
                                <img src="{icon}" class="message-icon" />
                                {partial}
                            </div>
                        ''', unsafe_allow_html=True)
                    st.code(code_content, language=lang)
                    st.session_state.last_rendered_index = i
                else:
                    st.markdown(f'''
                        <div class="message {message_class}">
                            <img src="{icon}" class="message-icon" />
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
                                <img src="{icon}" class="message-icon" />
                                {partial}
                            </div>
                        ''', unsafe_allow_html=True)
                    st.session_state.last_rendered_index = i
                else:
                    st.markdown(f'''
                        <div class="message {message_class}">
                            <img src="{icon}" class="message-icon" />
                            {formatted_msg}
                        </div>
                    ''', unsafe_allow_html=True)

    # Chat input with enhanced styling
    with st.form(key="chat_form", clear_on_submit=True):
        cols = st.columns([4, 1])
        with cols[0]:
            user_input = st.text_input("Type your message:", placeholder="Ask me anything...", label_visibility="collapsed")
        with cols[1]:
            submitted = st.form_submit_button("🚀 Send", use_container_width=True)

        if submitted and user_input.strip():
            with st.spinner(""):
                spinner_html = """
                <style>
                    @keyframes spin {
                        0% { transform: rotate(0deg); }
                        100% { transform: rotate(360deg); }
                    }
                    .spinner {
                        width: 24px;
                        height: 24px;
                        border: 4px solid rgba(94,194,221,0.2);
                        border-top: 4px solid #5ec2dd;
                        border-radius: 50%;
                        animation: spin 1s linear infinite;
                        display: inline-block;
                        vertical-align: middle;
                        margin-right: 10px;
                    }
                </style>
                <div class="spinner"></div>
                <span style="color: white;">Jarvis is thinking...</span>
                """
                st.markdown(spinner_html, unsafe_allow_html=True)
                response = get_jarvis_response(user_input)
                st.session_state.chat_history.append(("You", user_input))
                st.session_state.chat_history.append(("Jarvis", response))
                st.rerun()
