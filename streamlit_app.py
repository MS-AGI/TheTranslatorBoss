import streamlit as st
from deep_translator import GoogleTranslator
from langdetect import detect, LangDetectException

# Language mappings
LANGUAGES = {
    'Auto Detect': 'auto', 'Afrikaans': 'af', 'Albanian': 'sq', 'Amharic': 'am', 'Arabic': 'ar', 'Armenian': 'hy',
    'Azerbaijani': 'az', 'Basque': 'eu', 'Belarusian': 'be', 'Bengali': 'bn', 'Bosnian': 'bs', 'Bulgarian': 'bg',
    'Catalan': 'ca', 'Cebuano': 'ceb', 'Chinese (Simplified)': 'zh-CN', 'Chinese (Traditional)': 'zh-TW',
    'Corsican': 'co', 'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da', 'Dutch': 'nl', 'English': 'en',
    'Esperanto': 'eo', 'Estonian': 'et', 'Filipino': 'tl', 'Finnish': 'fi', 'French': 'fr', 'Frisian': 'fy',
    'Galician': 'gl', 'Georgian': 'ka', 'German': 'de', 'Greek': 'el', 'Gujarati': 'gu', 'Haitian Creole': 'ht',
    'Hausa': 'ha', 'Hawaiian': 'haw', 'Hebrew': 'iw', 'Hindi': 'hi', 'Hmong': 'hmn', 'Hungarian': 'hu',
    'Icelandic': 'is', 'Igbo': 'ig', 'Indonesian': 'id', 'Irish': 'ga', 'Italian': 'it', 'Japanese': 'ja',
    'Javanese': 'jw', 'Kannada': 'kn', 'Kazakh': 'kk', 'Khmer': 'km', 'Korean': 'ko', 'Kurdish': 'ku',
    'Kyrgyz': 'ky', 'Lao': 'lo', 'Latin': 'la', 'Latvian': 'lv', 'Lithuanian': 'lt', 'Luxembourgish': 'lb',
    'Macedonian': 'mk', 'Malagasy': 'mg', 'Malay': 'ms', 'Malayalam': 'ml', 'Maltese': 'mt', 'Maori': 'mi',
    'Marathi': 'mr', 'Mongolian': 'mn', 'Myanmar (Burmese)': 'my', 'Nepali': 'ne', 'Norwegian': 'no',
    'Pashto': 'ps', 'Persian': 'fa', 'Polish': 'pl', 'Portuguese': 'pt', 'Punjabi': 'pa', 'Romanian': 'ro',
    'Russian': 'ru', 'Samoan': 'sm', 'Scots Gaelic': 'gd', 'Serbian': 'sr', 'Sesotho': 'st', 'Shona': 'sn',
    'Sindhi': 'sd', 'Sinhala': 'si', 'Slovak': 'sk', 'Slovenian': 'sl', 'Somali': 'so', 'Spanish': 'es',
    'Sundanese': 'su', 'Swahili': 'sw', 'Swedish': 'sv', 'Tajik': 'tg', 'Tamil': 'ta', 'Telugu': 'te',
    'Thai': 'th', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Urdu': 'ur', 'Uzbek': 'uz', 'Vietnamese': 'vi',
    'Welsh': 'cy', 'Xhosa': 'xh', 'Yiddish': 'yi', 'Yoruba': 'yo', 'Zulu': 'zu'
}

LANGUAGES_REV = {v: k for k, v in LANGUAGES.items()}

# UI
st.title("🌐 Universal Language Translator")

text = st.text_area("Enter text to translate", height=150)

col1, col2 = st.columns(2)
with col1:
    src_lang = st.selectbox("From (source language)", list(LANGUAGES.keys()), index=0)
with col2:
    dest_lang = st.selectbox("To (target language)", list(LANGUAGES.keys()), index=list(LANGUAGES.keys()).index("English"))

if st.button("Translate"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Translating..."):
            try:
                # Detect language if 'Auto Detect' selected
                if LANGUAGES[src_lang] == 'auto':
                    detected_code = detect(text)
                    src_code = detected_code
                    detected_name = LANGUAGES_REV.get(detected_code, "Unknown")
                    st.info(f"Detected Language: {detected_name}")
                else:
                    src_code = LANGUAGES[src_lang]

                # Translate
                translated = GoogleTranslator(source=src_code, target=LANGUAGES[dest_lang]).translate(text)
                st.text_area("Translated Text", translated, height=150)

            except LangDetectException:
                st.error("Language detection failed. Try providing more text.")
            except Exception as e:
                st.error(f"Translation failed: {e}")

st.markdown("---")
st.markdown("©Copyright All Rights Reserved. \nAn open-source product ThePhyMathAI Co. owned by Mankrit Singh using [deep-translator](https://pypi.org/project/deep-translator/) and [Streamlit](https://streamlit.io/)")


