'''
MIT License
Copyright (c) 2022 Ahad 
If you want to use this code for any purpose, kindly give credits before using. 
You can modify or edit it but you are not allowed to remove the author name 
from the code.
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

# Importing required modules
import random
import webbrowser
import pyttsx3
from speech_recognition import *
from datetime import *
import wikipedia

name = "Ahad" # Elena wants to know your name enter your name here.
engine = pyttsx3.init("sapi5") # Using Microsoft Speech API
voices = engine.getProperty("voices") # Getting voices present in your computer.
engine.setProperty("voice", voices[1].id) # I want zeera's voice to be Elena's voice so I entered zeera's voice.

# Making say function so our assistant can speak.
def say(audio):
    engine.say(audio)
    engine.runAndWait()

# When you run Elena it will greet you using greetMe function.
def greetMe():
    hour = int(datetime.now().hour) # Taking current hour.
    # If it's 12 AM and less then 12 PM Elena will say Good Morning.
    if hour >= 0 and hour < 12:
        print("Elena: Good morning love how are you?")
        say("Good morning love how are you?")
    # Else if Time is 12 AM and is less than 6 PM Elena will say Good Afternoon.
    elif hour >= 12 and hour < 18:
        print(f"Elena: Good afternoon {name}! What are you doing?")
        say(f"Good afternoon {name}! What are you doing?")
    # Else if Time is greater than 6 PM and less than 12 AM Elena will say Good Evening.
    else: 
        print(f"Elena: Good evening {name}! I assume you must be tired you should go sleep.")
        say(f"Good evening {name}! I assume you must be tired you should go sleep.")
    # Making a list of messages so you won't have to listen same message as you open Elena.
    greetList = [
        f"Hey {name} how can I help you?",
        f"Hey I am your personal assistant Elena, How may I help you {name}?"
    ]
    randNumber = random.randint(0, 1)
    print(f'Elena: {greetList[randNumber]}') # Randomizing messages in greetList
    say(greetList[randNumber])

# Making a get command function so Elena will listen what you say.
def getCmd():
    r = Recognizer() # Defining recognizer
    # Getting you microphone as source so Elena can get your voice through your microphone 
    with Microphone() as source:
        print("Elena: Listening to you...")
        r.pause_threshold = 1
        getAudio = r.listen(source) # Listening to you

    try:
        print("Elena: Let me recognize what you've said...")
        say("Let me recognize what you've said...")
        query = r.recognize_google(getAudio, language="en-us") # Elena using Google engine to recognize what you've said
        print(f"{name}: {query}\n")
    except Exception as e:
        print("Elena: I wasn't able to listen you properly try saying it again.")
        say("I wasn't able to listen you properly try saying it again.") # If Elena can't hear you properly it will throw a error.
        return "None"
    return query
if __name__ == "__main__":
    print('''
╔═╗┬  ┌─┐┌┐┌┌─┐
║╣ │  ├┤ │││├─┤
╚═╝┴─┘└─┘┘└┘┴ ┴
''')
    print('''
Author: Ahad#3257                           
Website: https://itscruel.cf
Github: https://github.com/CruelDev69/Assistant-Elena
''')
    greetMe()
    # Making a infinite while loop so you won't have to run Elena everytime you say something 
    while True:
      args = getCmd().lower()

       # Making commands for Elena
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
      elif "help" in args:
        print('''
|-------------------|------------------------------------------------------------------------------------------------|
| Command Name      | Description                                                                                    |
|-------------------|------------------------------------------------------------------------------------------------|
| Wikipedia         | Elena will search your given query on wikipedia and will tell you result.                      |
| Developer         | Opens website of developer in your default browser.                                            |
| Robots            | Opens Developer's discord bots website in your default browser.                                |
| Open Repo         | Opens this repository in your default browser.                                                 |
| Open YouTube      | Opens YouTube in your default browser.                                                         |
| Open Discord      | Opens Discord in your default browser.                                                         |
| Open Instagram    | Opens Instagram in your default browser.                                                       |
| Open Twitter      | Opens Twitter in your default browser.                                                         |
| Open Facebook     | Opens Facebook in your default browser.                                                        |
| Open GitHub       | Opens GitHub in your default browser.                                                          |                                             
| Open Google       | Opens Google in your default browser.                                                          |
| Time              | Tells you what time is it.                                                                     |
| Help              | Shows help menu in console.                                                                    |
| Quit              | Quits the program.                                                                             |
|-------------------|------------------------------------------------------------------------------------------------|
        ''')
        say("My commands are: \nWikipedia\nDeveloper\nRobots\nOpen Repo\nOpen YouTube\nOpen Discord\nOpen Instagram\nOpen Twitter\nOpen Facebook\nOpen GitHub\nOpen Google\nTime\nHelp\nQuit")
