import speech_recognition as sr
import pyttsx3
import keyboard
import threading
import time
import platform

class Decoder:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.listening = False
        self.os = platform.system()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
        try:
            text = self.recognizer.recognize_google(audio).lower()
            print(f"Recognized: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""

    def process_command(self, command):
        if "close this application" in command:
            self.speak("Closing the application")
            if self.os == "Windows":
                keyboard.press_and_release('alt+f4')
            elif self.os == "Linux":
                keyboard.press_and_release('alt+f4')
            else:
                print("Unsupported OS for this command")

    def run(self):
        while True:
            text = self.listen()
            if "decoder" in text:
                self.speak("Hey")
                self.listening = True
                command = self.listen()
                self.process_command(command)
                self.listening = False

def background_listen():
    decoder = Decoder()
    decoder.run()

if __name__ == "__main__":
    print("Starting Decoder...")
    thread = threading.Thread(target=background_listen)
    thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping Decoder...")