import speech_recognition as sr
from pydub import AudioSegment

def speech_to_text_and_save():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Open the microphone and listen for audio
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        # Use Google Web Speech API to convert speech to text
        text = recognizer.recognize_google(audio)
        print("You said: " + text)

        # Save the audio as an MP3 file
        audio.export("listened_audio.mp3", format="mp3")
        print("Listened audio saved as 'listened_audio.mp3'")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))


def speech_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Open the microphone and listen for audio
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        # Use Google Web Speech API to convert speech to text
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

if __name__ == "__main__":
    speech_to_text()
    speech_to_text_and_save()
