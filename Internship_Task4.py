import streamlit as st
import requests
import textwrap
import random
import time
from streamlit_lottie import st_lottie

# ---------- CONFIG ----------
st.set_page_config(page_title="Health Assistant Chatbot", page_icon="🩺", layout="centered")

import json

# ---------- LOTTIE ANIMATION FROM LOCAL FILE ----------
def load_lottie_file(filepath):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except:
        return None

# ✅ Load from your local Lottie file (change the path accordingly)
lottie_health = load_lottie_file(r"")  # replace with actual file path


# ---------- THINKING MESSAGES ----------
thinking_messages = [
    "🤖 I'm thinking... 🧠 You can relax while I make a careful decision on your question.",
    "💭 Let me ponder that for a moment. I want to give you the best answer I can.",
    "⏳ Processing your health query... Your well-being matters!",
    "🩺 Just a second... I'm reviewing general medical knowledge to assist you.",
    "🔍 Looking through my virtual medical books... please hold on.",
    "🤔 Hmm... interesting question! Let me check what I know about that.",
    "🧠 I'm analyzing that with care, please give me a moment."
]

# ---------- API SETUP ----------
API_TOKEN = ""  # Replace with your real Hugging Face token
API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}

# ---------- QUERY FUNCTION ----------
def query_model(prompt):
    payload = {
        "inputs": prompt,
        "options": {"wait_for_model": True}
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)

        if response.status_code != 200:
            return f"❌ Error {response.status_code}: Unable to process request."

        result = response.json()
        return result[0]['generated_text'].split("Assistant:")[-1].strip()

    except Exception as e:
        return f"❌ Internal error: {e}"

# ---------- HEALTH CHATBOT LOGIC ----------
def health_chatbot(user_input):
    prompt = f"""You are a friendly and helpful virtual medical assistant. 
You only provide general health information. You do not diagnose or prescribe treatments. 
For serious or personal health issues, always advise the user to consult a healthcare professional.

User: {user_input}
Assistant:"""
    return query_model(prompt)

# ---------- UI DESIGN ----------
st.markdown("""
    <style>
        .big-title {
            font-size: 2.5rem;
            font-weight: bold;
            text-align: center;
            margin-top: -40px;
            color: #4F8BF9;
        }
        .footer {
            margin-top: 30px;
            font-size: 0.9rem;
            text-align: center;
            color: grey;
        }
        .stTextInput > div > div > input {
            font-size: 16px;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st_lottie(lottie_health, height=250, key="health")
st.markdown('<div class="big-title">Health Assistant Chatbot 🩺</div>', unsafe_allow_html=True)

st.markdown("Ask me general health-related questions. I’ll respond with helpful, safe information.")

# ---------- INPUT BOX ----------
user_input = st.text_input("💬 Your Question:", placeholder="e.g., What causes a sore throat?")

if user_input:
    st.markdown(f"<i>{random.choice(thinking_messages)}</i>", unsafe_allow_html=True)
    time.sleep(2)

    response = health_chatbot(user_input)
    wrapped = textwrap.fill(response, width=100)

    st.markdown("---")
    st.subheader("🤖 Chatbot Response:")
    st.markdown(f"<div style='font-size: 17px; line-height: 1.6;'>{wrapped}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.success("🩺 I hope that helped! Feel free to ask me another health question.")

# ---------- FOOTER ----------
st.markdown("""
<div class="footer">
Made with ❤️ by Muhammad Ahsan Kareem | Powered by Hugging Face + Streamlit
</div>
""", unsafe_allow_html=True)