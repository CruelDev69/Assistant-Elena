import random
import webbrowser
import pyttsx3
from speech_recognition import *
from datetime import *
import wikipedia

name = "Ahad"
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def say(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Elena: Good morning love how are you?")
        say("Good morning love how are you?")
    elif hour >= 12 and hour < 18:
        print(f"Elena: Good afternoon {name}! What are you doing?")
        say(f"Good afternoon {name}! What are you doing?")
    else: 
        print(f"Elena: Good evening {name}! I assume you must be tired you should go sleep.")
        say(f"Good evening {name}! I assume you must be tired you should go sleep.")
    greetList = [
        f"Hey {name} how can I help you?",
        f"Hey I am your personal assistant Elena, How may I help you {name}?"
    ]
    randNumber = random.randint(0, 1)
    print(f'Elena: {greetList[randNumber]}')
    say(greetList[randNumber])

def getCmd():
    r = Recognizer()
    with Microphone() as source:
        print("Elena: Listening to you...")
        r.pause_threshold = 1
        getAudio = r.listen(source)

    try:
        print("Elena: Let me recognize what you've said...")
        say("Let me recognize what you've said...")
        query = r.recognize_google(getAudio, language="en-us")
        print(f"{name}: {query}\n")
    except Exception as e:
        print("Elena: I wasn't able to listen you properly try saying it again.")
        say("I wasn't able to listen you properly try saying it again.")
        return "None"
    return query
if __name__ == "__main__":
    print('''
╔═╗┬  ┌─┐┌┐┌┌─┐
║╣ │  ├┤ │││├─┤
╚═╝┴─┘└─┘┘└┘┴ ┴
'''
    print('''
Author: Ahad#3257                           
Website: https://itscruel.cf
Github: https://github.com/CruelDev69/Assistant-Elena
''')
    greetMe()
    while True:
      args = getCmd().lower()

      if "wikipedia" in args:
        query = args.replace("wikiepedia", "")
        say(f"Searching {query} in wikipedia")
        results = wikipedia.summary(query, sentences=3)
        print("Elena: According to wikipedia")
        say("According to wikipedia")
        print(results)
        say(results)
      elif "fine" in args:
        print("Elena: Oh that's good to know.")
        say("Oh that's good to know") 
      elif "open repo" in args:
        webbrowser.open("https://github.com/CruelDev69/Assistant-Elena")
        say("Opening my source code repository...")
        print("Elena: Opening my source code repository...")
      elif "developer" in args:
        webbrowser.open("https://itscruel.cf")
        say("Opening my Developer's website...")
        say("Fact If you'll click on his name in center website will play a music.")
        print("Elena: Opening my Developer's website...")
        print("Elena: Fact If you'll click on his name in center website will play a music.")
      elif "robots" in args:
        webbrowser.open("https://thevunit.vivre.cf")
        webbrowser.open("https://thevunit.vivremusic.cf")
        say("Opening websites of my developer's discord bots...")
        say("Vivre and Vivre Music")
        print("Elena: Opening websites of my developer's discord bots...")
        print("Elena: Vivre and Vivre Music.")
      elif "open discord" in args:
        webbrowser.open("https://discord.com/app")
        say("Opening Discord...")
        print("Elena: Opening Discord...")
      elif "open google" in args:
        webbrowser.open("https://google.com")
        say("Opening Google...")
        print("Elena: Opening Google...")
      elif "open youtube" in args:
        webbrowser.open("https://youtube.com/channel/UC5vCNtDoHuJTOMD8oqL7AgQ")
        say("Opening YouTube...")
        print("Elena: Opening YouTube...")
      elif "open instagram" in args:
        webbrowser.open("https://instagram.com/ahadnoor._")
        say("Opening Instagram...")
        print("Elena: Opening Instagram...")
      elif "open twitter" in args:
        webbrowser.open("https://twitter.com/19Ahadnoor")
        say("Opening Twitter...")
        print("Elena: Opening Twitter...")
      elif "open facebook" in args:
        webbrowser.open("https://facebook.com/ahad.noor.18041")
        say("Opening Facebook...")
        print("Elena: Opening Facebook...")
      elif "time" in args:
        currentTime = datetime.now().strftime("%H:%M:%S")
        print(f"Elena: The time is {currentTime}.")
        say(f"The time is {currentTime}")
      elif "quit" in args:
        break 
