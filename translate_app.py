# import streamlit as st
# from googletrans import Translator
# from langcodes import standardize_tag, Language
# import time
#
# def translate_text(text, target_lang):
#     translator = Translator()
#     translation = translator.translate(text, dest=target_lang)
#     return translation.text
#
# def translate_to_all_languages(text):
#     supported_languages = ['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny',
#                             'zh-cn', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl',
#                             'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw', 'he', 'hi', 'hmn', 'hu', 'is', 'ig', 'id',
#                             'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb',
#                             'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'or', 'ps', 'fa', 'pl',
#                             'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es',
#                             'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh',
#                             'yi', 'yo', 'zu']
#
#     translations = {}
#     with st.spinner("Translating..."):
#         info_text = st.info("Translated to 0 languages")
#         for i, lang_code in enumerate(supported_languages, start=1):
#             time.sleep(0.1)  # Simulating translation delay
#             translation = translate_text(text, lang_code)
#             translations[lang_code] = translation
#             info_text.text(f"Translated to {i} languages")
#     st.success("Translation Completed!")
#     return translations
#
# def main():
#     st.title("Language Translator")
#
#     # User input
#     text_to_translate = st.text_area("Enter text in English:", "")
#
#     if st.button("Translate"):
#         if not text_to_translate:
#             st.warning("Please enter text to translate.")
#         else:
#             translations = translate_to_all_languages(text_to_translate)
#
#             # Display translations
#             st.header("Translations in All Languages:")
#             for lang_code, translation in translations.items():
#                 st.write(f"**{lang_code.upper()}**: {translation}")
#
#             # Copy to clipboard button
#             st.button("Copy to Clipboard", on_click=lambda: st.write(translations))
#
# if __name__ == "__main__":
#     main()
import streamlit as st
from googletrans import Translator, LANGUAGES
import time

def translate_text(text, target_lang):
    translator = Translator()
    translation = translator.translate(text, dest=target_lang)
    return translation.text

def get_all_languages():
    return list(LANGUAGES.keys())

def translate_to_all_languages(text):
    supported_languages = get_all_languages()

    translations = {}
    with st.spinner("Translating..."):
        info_text = st.info("Translated to 0 languages")
        for i, lang_code in enumerate(supported_languages, start=1):
            time.sleep(0.1)
            translation = translate_text(text, lang_code)
            translations[lang_code] = translation
            info_text.text(f"Translated to {i} languages")
    st.success("Translation Completed!")
    return translations

def main():
    st.title("Language Translator")

    text_to_translate = st.text_area("Enter text in English:", "")

    if st.button("Translate"):
        if not text_to_translate:
            st.warning("Please enter text to translate.")
        else:
            translations = translate_to_all_languages(text_to_translate)

            st.header("Translations in All Languages:")
            for lang_code, translation in translations.items():
                st.write(f"**{lang_code.upper()}**: {translation}")

            st.button("Copy to Clipboard", on_click=lambda: st.write(translations))

if __name__ == "__main__":
    main()
