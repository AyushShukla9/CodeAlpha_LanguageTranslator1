import streamlit as st
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import os

# Initialize translator
translator = Translator()

st.set_page_config(page_title="Language Translator", page_icon="🌍")

st.title("🌍 Language Translation Tool")

# Input text
text = st.text_area("✏️ Enter text to translate:")

# Language selection
languages = list(LANGUAGES.values())

source_lang = st.selectbox("🌐 Source Language", languages, index=languages.index("english"))
target_lang = st.selectbox("🌐 Target Language", languages, index=languages.index("hindi"))

# Convert language name to code
def get_lang_code(lang_name):
    for code, name in LANGUAGES.items():
        if name == lang_name:
            return code

# Translate button
if st.button("🔄 Translate"):
    if text.strip() != "":
        src_code = get_lang_code(source_lang)
        tgt_code = get_lang_code(target_lang)

        translated = translator.translate(text, src=src_code, dest=tgt_code)

        st.subheader("✅ Translated Text:")
        st.success(translated.text)

        # Copy feature
        st.code(translated.text)

        # Text-to-Speech
        tts = gTTS(translated.text)
        tts.save("output.mp3")

        st.audio("output.mp3")

        # Clean up file
        if os.path.exists("output.mp3"):
            os.remove("output.mp3")

    else:
        st.warning("⚠️ Please enter some text")
