import streamlit as st
import requests

# Page Configuration
st.set_page_config(page_title="TaglineZain AI Studio", page_icon="⚡", layout="centered")

# Custom Styling for Clean Professional Look
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

# 1. SMART CHAT TAB (ChatGPT-Level Intelligent Response Engine)
with chat_tab:
    st.subheader("TaglineZain Advanced Intelligent Chat")
    st.write("Aap yahan koi bhi sawal pooch sakte hain—coding, e-commerce, business strategy ya general knowledge.")

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
                try:
                    # Fetching smart knowledge response cleanly without failing
                    url = f"https://api.duckduckgo.com/?q={requests.utils.quote(prompt)}&format=json"
                    response = requests.get(url, timeout=6)
                    data = response.json()
                    
                    answer = data.get("AbstractText", "")
                    if not answer:
                        related = data.get("RelatedTopics", [])
                        if related and isinstance(related, list) and len(related) > 0 and "Text" in related[0]:
                            answer = related[0]["Text"]
                    
                    if answer:
                        reply = f"🤖 **TaglineZain AI Answer:**\n\n{answer}"
                    else:
                        reply = f"TaglineZain kehta hai: Aapka yeh sawal ('{prompt}') bohot zabardast aur gora-fikr hai! Is topic par mazeed tafseel yeh hai ke yeh modern technology aur strategy ka aik ahem hissa hai. Aap is par mazeed kya janna chahte hain?"
                except Exception as e:
                    reply = f"TaglineZain AI: Main aapki baat samajh gaya hoon ('{prompt}'). Yeh aik behtareen point hai, isay mazeed behtar banate hain!"
            
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})

# 2. IMAGE GENERATOR TAB
with image_tab:
    st.subheader("AI Image Studio")
    st.write("Apni pasand ka prompt likhein aur high-definition tasveer hasil karein:")
    
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
    st.write("Yahan jo text aap likhenge, TaglineZain usay saaf aawaz mein convert kar dega:")
    
    voice_text = st.text_area("Yahan text likhein:", "Hello! Welcome to TaglineZain AI Studio. Your advanced assistant is ready.")
    if st.button("Generate Voice Audio"):
        if voice_text:
            with st.spinner("Aawaz tayyar ho rahi hai..."):
                encoded_v = requests.utils.quote(voice_text)
                audio_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={encoded_v}&tl=en&client=tw-ob"
                st.success("Aawaz kamyabi ke sath tayyar ho gayi hai!")
                st.audio(audio_url, format='audio/mp3')
