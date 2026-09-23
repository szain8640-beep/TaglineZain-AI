import streamlit as st
import requests

# Page Configuration
st.set_page_config(page_title="TaglineZain AI Studio", page_icon="⚡", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stTextInput input, .stTextArea textarea {
        background-color: #161b22;
        color: #ffffff;
        border-radius: 8px;
        border: 1px solid #30363d;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ TaglineZain-AI Studio")
st.write("Aapka apna high-level AI platform: Smart Chat, AI Image Generator, aur Voice Studio.")

# Tabs for Features
chat_tab, image_tab, voice_tab = st.tabs(["💬 Smart Chat", "🖼️ AI Image Generator", "🗣️ Voice Studio"])

# 1. SMART CHAT TAB (Smart Conversational Engine)
with chat_tab:
    st.subheader("TaglineZain Advanced Intelligent Chat")
    st.write("Aap yahan koi bhi sawal pooch sakte hain—coding, e-commerce, business strategy ya aam guftagu.")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Salam! Main TaglineZain-AI hoon. Batayein aaj main aapki kya behtareen madad kar sakta hoon?"}
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Yahan apna sawal ya prompt likhein..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("TaglineZain soch raha hai..."):
                p_lower = prompt.lower().strip()
                
                # Smart Conversational Handlers for Natural Chat Experience
                if any(word in p_lower for word in ["kesy ho", "kese ho", "kaise ho", "how are you"]):
                    reply = "Main bilkul theek hoon! Allah ka shukar hai. Aap sunayein, aap kaise hain aur aaj main aapki kya madad karoon?"
                elif any(word in p_lower for word in ["salam", "assalam", "hello", "hi", "hey"]):
                    reply = "Waikum Assalam! Bataiye, aaj konsa naya project ya sawal discuss karna hai?"
                elif any(word in p_lower for word in ["era name", "tumhara naam", "who are you", "what is your name"]):
                    reply = "Mera naam **TaglineZain-AI** hai, aur main aapka apna advanced AI assistant hoon jo aapke sabhi tasks ko behtar banane ke liye tayyar kiya gaya hai."
                else:
                    try:
                        # Fallback to web search knowledge for general queries
                        url = f"https://api.duckduckgo.com/?q={requests.utils.quote(prompt)}&format=json"
                        response = requests.get(url, timeout=5)
                        data = response.json()
                        answer = data.get("AbstractText", "")
                        
                        if answer:
                            reply = f"🤖 **TaglineZain AI Answer:**\n\n{answer}"
                        else:
                            reply = f"Aapka yeh sawal bohot acha hai! '{prompt}' ke hawale se yeh kehna hai ke yeh ek ahem topic hai jis par mazeed focus karne se behtareen nataij mil sakte hain. Aap is baray mein aur kya pochna chahte hain?"
                    except Exception:
                        reply = f"Main aapki baat samajh gaya hoon ('{prompt}'). Is par mazeed tafseel se baat karte hain, batayein agla step kya kiya jaye?"
            
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})

# 2. IMAGE GENERATOR TAB
with image_tab:
    st.subheader("AI Image Studio")
    img_prompt = st.text_input("Tasveer ka prompt likhein:", "A stunning futuristic cyberpunk city with neon lights")
    if st.button("Generate Image Now"):
        if img_prompt:
            with st.spinner("Tasveer tayyar ho rahi hai..."):
                encoded = requests.utils.quote(img_prompt)
                img_url = f"https://image.pollinations.ai/prompt/{encoded}"
                st.success("Tasveer kamyabi ke sath tayyar ho gayi hai!")
                st.image(img_url, caption=img_prompt, use_container_width=True)

# 3. VOICE STUDIO TAB
with voice_tab:
    st.subheader("Professional Voice Studio")
    voice_text = st.text_area("Yahan text likhein:", "Hello! Welcome to TaglineZain AI Studio.")
    if st.button("Generate Voice Audio"):
        if voice_text:
            with st.spinner("Aawaz tayyar ho rahi hai..."):
                encoded_v = requests.utils.quote(voice_text)
                audio_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={encoded_v}&tl=en&client=tw-ob"
                st.success("Aawaz kamyabi ke sath tayyar ho gayi hai!")
                st.audio(audio_url, format='audio/mp3')
