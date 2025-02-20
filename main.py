import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    """Process user voice command and execute corresponding action."""
    command = command.lower()

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://instagram.com")

    elif "open chat" in command:
        speak("Opening ChatGPT")
        webbrowser.open("https://chatgpt.com")

    elif "search" in command:
        search_query = command.replace("search", "").strip()
        if search_query:
            url = f"https://www.google.com/search?q={search_query.replace(' ', '+')}"
            speak(f"Searching for {search_query} on Google")
            webbrowser.open(url)
        else:
            speak("What would you like to search for?")

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        print("Listening for activation...")

        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)  # Reduce noise issues
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=2)
                word = recognizer.recognize_google(audio).lower()

            if "jarvis" in word:
                speak("Yes? How can I help?")
                print("Jarvis Active... Listening for command")

                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                
                process_command(command)

        except sr.UnknownValueError:
            print("Could not understand the command. Try again.")
        except sr.RequestError:
            print("Speech Recognition service unavailable. Check your internet connection.")
        except Exception as e:
            print(f"Error: {e}")
