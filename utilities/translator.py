from googletrans import Translator
from gtts import gTTS
import os

translator = Translator()

def translate_and_speak(text, target_language='kn'):  # Default to Kannada
    try:
        # Translate text
        translation = translator.translate(text, dest=target_language)
        
        # Check if translation is valid
        if translation is None or not translation.text:
            return "Error: Translation failed."

        translated_text = translation.text

        # Create a TTS object
        tts = gTTS(text=translated_text, lang=target_language)

        # Save the audio file
        tts.save("translation.mp3")

        # Play the audio file (requires a suitable media player on your system)
        os.system("mpg321 translation.mp3")  # Adjust this if needed for your system

        return translated_text

    except Exception as e:
        return f"Error: {e}"

# Example usage:
text = input("Enter text:\n")
req_lang = input("Enter required language (Tamil/Hindi/Kannada):\n")

# Language code mapping
lang_code_map = {
    "tamil": "ta",
    "hindi": "hi",
    "kannada": "kn"
}

# Get the language code, default to Kannada
code = lang_code_map.get(req_lang.lower(), "kn")

# Translate and speak
translated_text = translate_and_speak(text, code)

# Output the results
print(f"Original: {text}")
print(f"Translated: {translated_text}")
