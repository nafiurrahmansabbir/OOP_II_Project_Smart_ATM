import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer and text-to-speech converter
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for user input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        user_input = recognizer.recognize_google(audio)
        print("User said:", user_input)
        return user_input
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return ""

# Function to execute tasks based on user input
def process_input(input_text):
    if "hello" in input_text:
        speak("Hello! How can I help you?")
    elif "weather" in input_text:
        # Code to fetch weather information from an API
        speak("The weather today is sunny.")
    elif "goodbye" in input_text:
        speak("Goodbye! Have a great day.")
        exit()
    else:
        speak("I'm sorry, I didn't understand that.")

# Main loop
while True:
    user_input = listen().lower()
    process_input(user_input)
