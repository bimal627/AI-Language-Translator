import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

st.set_page_config(
    page_title="Language Translator",
    page_icon="🌐"
)

st.title(" Language Translatior Tool")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Nepali": "ne",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja"
}

text = st.text_area("Enter Text")

source_lang = st.selectbox(
    "Source Language",
    list(languages.keys())
)

target_lang = st.selectbox(
    "Target Language",
    list(languages.keys())
)

if st.button("Translate"):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:

            translated_text = GoogleTranslator(
                source=languages[source_lang],
                target=languages[target_lang]
            ).translate(text)

            st.subheader("Translated Text")
            st.success(translated_text)

            tts = gTTS(
                text=translated_text,
                lang=languages[target_lang]
            )

            audio_file = "translation.mp3"
            tts.save(audio_file)

            st.subheader("🔊 Speech")

            with open(audio_file, "rb") as audio:
                st.audio(audio.read(), format="audio/mp3")

        except Exception as e:
            st.error(f"Error: {e}")