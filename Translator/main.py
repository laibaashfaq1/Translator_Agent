import streamlit as st
import google.generativeai as genai

# Load Gemini API Key from Streamlit Secrets
api_key = st.secrets["GEMINI_API_KEY"]

# Check API key
if not api_key:
    st.error("❌ Gemini API key not found. Please set it in Streamlit secrets.")
    st.stop()

# Configure Gemini API
genai.configure(api_key=api_key)

# Supported languages
languages = [
    "Urdu", "Roman Urdu", "English", "Roman English", "Spanish", "German",
    "Chinese", "Japanese", "Korean", "Arabic", "Russian", "Hindi", "Bengali",
    "Turkish", "Italian", "Greek", "Thai", "French"
]

# Streamlit UI setup
st.set_page_config(page_title="🌐 Translator by Laiba", layout="centered")
st.title("🌍 Language Translator")
st.markdown("**Created by Laiba Ashfaq** — Translate your text into multiple languages effortlessly.")
st.divider()

# Input fields
text_input = st.text_area("✏️ Enter the text you want to translate:", height=150)
selected_language = st.selectbox("🌐 Select your desired language:", languages)
submit = st.button("🔁 Translate")
st.divider()

# Translation logic
if submit:
    if not text_input.strip():
        st.warning("⚠️ Please enter some text to translate.")
    else:
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")

            # Create prompt based on selected language
            if selected_language == "Roman Urdu":
                prompt = f"Translate the following text to Urdu but write it in Roman Urdu using English alphabets only:\n\n{text_input}"
            elif selected_language == "Roman English":
                prompt = f"Translate the following text to English and write it in Roman English using simple Latin script only:\n\n{text_input}"
            else:
                prompt = f"Translate the following text into {selected_language}. Please reply only in the native {selected_language} script with no transliteration:\n\n{text_input}"

            # Generate and display the response
            response = model.generate_content(prompt)
            translated_text = response.text.strip()

            st.success(f"✅ Translated to {selected_language}:")
            st.markdown(f"```{translated_text}```")

        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
