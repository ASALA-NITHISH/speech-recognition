import speech_recognition as sr
import pyttsx3 as pt
import  pywhatkit as pk
listening=sr.Recognizer()
engine=pt.init('dummy')

def speak(text):
    engine.say(text)
    engine.runAndWait()
def hear():
    cmd =''
    try:
        with sr.Microphone() as mic:
            print('listening......')
            listening.adjust_for_ambient_noise(mic)
            voice=listening.listen(mic)
            cmd=listening.recognize_google(voice)
            cmd=cmd.lower()
            if 'Nani' in cmd:
                cmd=cmd.replace('Nani','')
                print(cmd)
    except:
        pass
    return cmd
def run():
    cmd = hear()
    print(cmd)
    # if 'hello' in cmd:
    song = cmd.replace('play', '')
    speak('playing' + song)
    pk.playonyt('Playing...' + song)
run()