import speech_recognition as sr
import pyttsx3
import wikipedia
import os
import datetime

# Initialize the recognizer and the text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Use the microphone as a source of audio input
with sr.Microphone() as source:
    # Set the minimum amount of silence for a phrase to be considered complete
    r.pause_threshold = 0.8
    
    # Continuously listen for questions until the user says "stop"
    while True:
        print("Speak now!")
        audio = r.listen(source)

        try:
            # Convert audio to text
            text = r.recognize_google(audio)
            print("You said: " + text)

            # Stop listening if the user says "stop"
            if text == "stop":
                print("Goodbye!")
                break

            # Check if the user wants to open an application
            if "open calculator" in text:
                os.startfile('calc.exe')
                print("Opening Calculator")

            elif "open Microsoft Edge" in text:
                os.startfile('msedge.exe')
                print("Opening Microsoft Edge")

            elif "what time is it" in text:
                time_now = datetime.datetime.now().strftime("%I:%M %p")
                print("The current time is " + time_now)
                engine.say("The current time is " + time_now)
                engine.runAndWait()

            elif "what date is it" in text:
                date_now = datetime.date.today().strftime("%B %d, %Y")
                print("Today's date is " + date_now)
                engine.say("Today's date is " + date_now)
                engine.runAndWait()

            else:
                # Query Wikipedia for the answer to the question
                wikipedia.set_lang("en")
                answer = wikipedia.summary(text, sentences=2)

                # Convert the answer to speech and play it
                print(answer)
                engine.say(answer)
                engine.runAndWait()

        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        except wikipedia.exceptions.PageError:
            print("Sorry, I could not find a Wikipedia page that matches your query.")
        except wikipedia.exceptions.DisambiguationError as e:
            print("Please be more specific. {0}".format(e))