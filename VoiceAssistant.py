
from cgitb import text
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes


def speechtext():
    
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listening . . .")
        audio_data = recognizer.record(source, duration=5)
        print ("Recognizing . . .")
        try:
            data = recognizer.recognize_google(audio_data)
            #print(data)
            #print(data.lower())
            return data.lower()
        except sr.UnknownValueError:
                print("Sorry, Didnt get ya")
                text_to_speech("Sorry, did not understand")
                


def text_to_speech(x) :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine. setProperty('rate',160)
    engine.say(x)
    engine.runAndWait()


if __name__ == '__main__':
    
    try:
        if "hey peter" in speechtext():
            print("Hey, how can I help you")        
            text_to_speech("Hey, how can I help you")
            while True :
                data1 = speechtext()
                if "your name" in data1:
                        name = "My name is peter"
                        print(name)
                        text_to_speech(name)
                elif "old are you" in data1:
                        age = "I am ageless"
                        print(age)
                        text_to_speech(age)
                elif "date" in data1:
                        date  = datetime.datetime.now().strftime("%Y-%m-%d")
                        print(date)
                        text_to_speech(date)
                elif "time" in data1:
                        time  = datetime.datetime.now().strftime("%I-%M-%p")
                        print(time)
                        text_to_speech(time)
                elif "joke" in data1:
                        joke = pyjokes.get_joke(category='neutral')
                        print(joke)
                        text_to_speech(joke)
                elif "youtube" in data1:
                        print("Opening Youtube")
                        webbrowser.open("https://www.youtube.com/")
                elif "portfolio" in data1:
                        print("Opening Portfolio")
                        webbrowser.open("https://knat01.github.io/Portfolio/")
                elif "" or None in data1:
                        text_to_speech("Sorry, Didnt get ya")
                elif "exit" in data1:
                        print("Thank you")
                        text_to_speech("Thank you")
                        break  
                
    except TypeError:
            print("Enjoy your day!")
            text_to_speech("Enjoy your day!")