from gtts import gTTS
import os

def text_to_speech(text, output_file="output.mp3"):
    tts = gTTS(text)
    tts.save(output_file)
    os.system("mpg123 " + output_file)  # You may need to install mpg123 for playing the audio

if __name__ == "__main__":
    text = input("Enter the text you want to convert to speech: ")
    text_to_speech(text)
