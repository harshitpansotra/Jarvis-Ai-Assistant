import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import os
import pyautogui
import wikipedia
import datetime
from playsound import playsound
import keyboard
import pyjokes
from PyDictionary import PyDictionary as Diction
from googletrans import Translator




Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices', voices[1].id)
Assistant.setProperty('rate', 170)


def Speak(audio):
    print(" ")
    Assistant.say(audio)
    print(f": {audio}")
    print("   ")
    print("   ")
    Assistant.runAndWait()




def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing......")
            query = command.recognize_google(audio,language='en-in')
            print(f"You Said : {query}")

        except Exception as Error:
            return "none"
        
        return query.lower()
    

def TaskExe():

    def Music():
        Speak("Tell me the name of the song!")
        musicName = takecommand()

        if 'all eyez on me' in musicName:
            os.startfile('C\\JarvisAI')

        elif 'blanko' in musicName:
            os.startfile('E:\\  \\All-Eyez-on-Me-2Pac-x-Dj-Belite.mp3')

        else:
            pywhatkit.playonyt(musicName)

        Speak("Your song has been started , Enjoy sir!")

    def Whatsapp():
        Speak("Tell me the Message!")
        name = takecommand()

        if 'nitin' in name:
            Speak("Tell me the Message!")
            msg = takecommand()
            Speak("Tell me the time sir!")
            Speak("time in Hour!")
            hour = int(takecommand())
            Speak("Tell in Minutes!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+919915423248" ,msg,hour,min,20)

            Speak("ok sir , sending message!")

        elif 'abhay' in query:
            Speak("Tell me the Message!")
            msg = takecommand()
            Speak("Tell me the time sir!")
            Speak("time in Hour!")
            hour = int(takecommand())
            Speak("Tell in Minutes!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+918968110772" ,msg,hour,min,20)

            Speak("ok sir , sending message!")

        else:
            Speak("Tell me the phone number!")
            phone = int(takecommand())
            ph = '+91' + phone
            Speak("Tell me the Message!")
            msg = takecommand()
            Speak("Tell me the time sir!")
            Speak("time in Hour!")
            hour = int(takecommand())
            Speak("Tell in Minutes!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg(ph,msg,hour,min,20)

            Speak("ok sir , sending message!")

    def OpenApps():
        Speak("Ok sir , Wait a second!")
        
        if 'code' in query:
            os.system("C:\\Users\ABC\AppData\Local\Programs\Microsoft VS Code\Code.exe")

        elif 'chrome' in query:
            os.system("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

        elif 'microsoft edge' in query:
            os.system("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/')

        elif 'gmail' in query:
            webbrowser.open('https://mail.google.com/mail/u/0')

        elif 'maps' in query:
            webbrowser.open('https://www.google.com/maps')

        Speak("Your command has been completed sir!")

    def Dict():
        Speak("Activated Dictionary!")
        Speak("Tell me the problem!")
        probl = takecommand()

        if ' meaning' in query:
            probl = probl.replace("what is the","")
            probl = probl.replace("Frieady","")
            probl = probl.replace("of")
            probl = probl.replace("meaning of","")
            result = Diction.meaning(probl)
            Speak(f"The meaning for {probl} is {result}")

        elif 'synonym' in probl:
            probl = probl.replace("what is the","")
            probl = probl.replace("Frieady","")
            probl = probl.replace("of")
            probl = probl.replace("sanonym of","")
            result = Diction.synonym(probl)
            Speak(f"The Sanonym for {probl} is {result}")

        elif 'antonym' in probl:
            probl = probl.replace("what is the","")
            probl = probl.replace("Frieady","")
            probl = probl.replace("of")
            probl = probl.replace("antonym of","")
            result = Diction.antonym(probl)
            Speak(f"The Antonym for {probl} is {result}")

        Speak("Exited Dictionary!")


    def CloseApps():
        Speak("Ok sir , wait a second!")

        if 'code' in query:
            os.system("TaskKill /f /im code.exe")

        elif 'chrome' in query:
            os.system("TaskKill /f /im chrome.exe")

        elif 'gmail' in query:
            os.system("TaskKill /f /im chrome.exe")

        elif 'maps' in query:
            os.system("TaskKill /f /im chrome.exe")

        elif 'instagram' in query:
            os.system("TaskKill /f /im chrome.exe")

        elif 'microsoft edge' in query:
            os.system("TaskKill /f /im msedge.exe")

        Speak("Your command has been succesfully completed sir!")

    def YouTubeAuto():
        Speak("Whats your command ?")
        comm = takecommand()

        if 'pause' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('1')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'full screen' in comm:
            keyboard.press('f')

        Speak("Done sir!")

    def screenshot():
        Speak("Ok Boss , What should i name that file ?")
        path = takecommand()
        path1name = path + ".png"
        path1 = "D:\\" + path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("D:\\")
        Speak("Here is your screenshot")

    def TakeHimdi():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.....")
            command.pause_threshold = 1
            audio = command.listen(source)

        try:
            print("Recognizing......")
            query = command.recognize_google(audio,language='hi')
            print(f"You Said : {query}")

        except Exception as Error:
            return "none"
        
        return query.lower()
    
    def Tran():
        Speak("Tell me the line")
        line = TakeHimdi()
        translate = Translator()
        result = translate.translate(line)
        Text = result.text
        Speak(Text)





    while True:
        query = takecommand()

        if 'hello' in query:
            Speak("Hello sir , I am Jarvis .")
            Speak("Your Personal Assistant!")
            Speak("How May I Help You?")

        elif 'hi' in query:
            Speak("Hello sir , I am Jarvis .")
            Speak("Your Personal Assistant!")
            Speak("How May I Help You?")



        elif 'how are you' in query:
            Speak("I Am Fine Sir!")
            Speak("Whats About You?")

        elif 'you need a break' in query:
            Speak("Ok Sir , You Can Call Me Anytime !")
            break

        elif 'Kya hall hai' in query:
            Speak("Main Badiya hoon App Btao!")

        elif 'bye'in query:
            Speak("Ok Sir , Bye!")
            break
        elif 'youtube search' in query:
            Speak("Ok Sir , This Is What I Found for Your search")
            query = query.replace("Jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("Done Sir!")

        elif 'google search' in query:
            Speak("This is what i found for your search sir!")
            query = query.replace("Frieady","")
            query = query.replace("google search","")
            pywhatkit.search(query)
            Speak("Done Sir!")

        elif 'website' in query:
            Speak("OK Sir , Launching.....")
            query = query.replace("Frieady","")
            query = query.replace("website","")
            query = query.replace(" "," ")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("Launched")

        elif 'music' in query:
            Music()

        elif 'Wikipedia' in query:
            Speak("Searching Wikipedia....")
            query = query.replace("Frieady","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak(f"According to Wikipedia : {wiki}")

        elif 'whatsapp' in query:
            Whatsapp()

        elif ' screenshot' in query:
            screenshot()

        elif 'open instagram' in query:
            OpenApps()

        elif 'open gmail' in query:
            OpenApps()

        elif 'open maps' in query:
            OpenApps()

        elif 'open chrome' in query:
            OpenApps()

        elif 'open microsoft edge' in query:
            OpenApps()

        elif 'open code' in query:
            OpenApps()

        elif 'clese chrome' in query:
            CloseApps()

        elif 'clese gmail' in query:
            CloseApps()

        elif 'clese instagram' in query:
            CloseApps()

        elif 'clese maps' in query:
            CloseApps()

        elif 'clese code' in query:
            CloseApps()

        elif 'clese microsoft edge' in query:
            CloseApps()

        if 'pause' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('1')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'youtube tool' in query:
            YouTubeAuto()

        elif 'joke' in query:
            get = pyjokes.get_joke()
            Speak(get)

        elif 'repeat my words' in query:
            Speak("Speak Sir!")
            jj = takecommand()
            Speak(f"You said : {jj}")

        elif 'my location' in query:
            Speak("Ok sir , Wait a second!")
            webbrowser.open('https://www.google.com/maps/dir/31.6630022,74.8857985/RUHANI+SATSANG+PREM+SAMAJ+(REGD.),+Majitha+Road,+Tung+Bala,+Amritsar,+Punjab/@31.6605636,74.8868896,16.84z/data=!4m9!4m8!1m1!4e1!1m5!1m1!1s0x39196376561240d1:0x18f8bb8427a11aa8!2m2!1d74.8924918!2d31.6577941?entry=ttu')

        elif 'dictionary' in query:
            Dict()

        elif 'alarm' in query:
            Speak("Enter the time!")
            time = input(": Enter the time :")
            
            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    Speak("Time to wake up sir!")
                    playsound('beast.mp3')
                    Speak("Alarm Closed!")

                elif now>time:
                    break

        elif 'translstor' in query:
            Trans()


TaskExe()


