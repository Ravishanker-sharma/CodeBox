from gtts import gTTS
import pyttsx3


def text_to_audio(text, speed=1.0, voice='english'):
    # Using gTTS for text-to-speech conversion
    tts = gTTS(text=text, lang=voice, slow=False)
    tts.save("output.mp3")

    # Using pyttsx3 for playing the audio with customizable speed and voice
    engine = pyttsx3.init()

    # Setting the speed rate
    engine.setProperty('rate', speed * 150)  # Adjust 150 according to your preference

    # Setting the voice
    found_voice = False
    voices = engine.getProperty('voices')
    for v in voices:
        # Check if 'languages' attribute is present in the voice
        if hasattr(v, 'languages') and v.languages:
            if v.languages[0] == voice:
                engine.setProperty('voice', v.id)
                found_voice = True
                break

    # Check if the specified voice was not found
    if not found_voice:
        print(f"Voice '{voice}' not found. Using the default voice.")

    # Playing the audio
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    # Example usage
    text_to_audio("Hello, this is a test. You can customize speed and voice.", speed=1.3, voice='en')
