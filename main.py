import speech_recognition as sr
import os
import sys
import pyautogui



import speech
r = sr.Recognizer()
#r.energy_threshold = 500

def listen():
    with sr.Microphone(device_index=0) as source:
        r.adjust_for_ambient_noise(source, duration=1)
        #speech.say('SEARCHING KEYWORD')
        print('listening')
        audio = r.listen(source)
        print(audio)
        #r.recognize_google(audio)

    #listen()
    try:
        command = r.recognize_google(audio)
        print("Predictions: " + command)
        if "volume up" in command:
            speech.say('volume up')
            l = command.split()
            for i in range(20):
                pyautogui.hotkey('volumeup')
            listen()
        if "volume down" in command:
            l = command.split()
            for i in range(10):
                pyautogui.hotkey('volumedown')
            #pyautogui.hotkey('fn', 'pause')
            listen()
        if "close tab" in command:
            speech.say('closing tab')
            pyautogui.hotkey('ctrl', 'w')
            listen()
            #listen()
        if "close" in command:
            l = command.split()
            i = l.index('close')
            kill = "taskkill /f /im " + command.split()[i+1] + ".exe"
            speech.say('closing ' + command.split()[i+1])
            os.system(kill)
            listen()
        if "exit" in command:
            speech.say('closing program')
            sys.exit()
        if "type" in command:
            l = command.split()
            i = l.index('type')
            s = len(l)
            e = ""
            for j in range(i+1, s):
                e += (l[j]) + " "
            pyautogui.write(e)
            listen()
        if "open" in command:
            l = command.split()
            i = l.index('open')

            if l[i + 1] != "chrome" or "firefox":
                os.system("start " + l[i + 1])

            if l[i + 1] != "chrome" or "firefox":
                    os.system("start " + l[i + 1] + ":")
            speech.say('starting' + l[i + 1])
        if "press enter" in command:
            pyautogui.press("enter")
        if command == "new tab":
            pyautogui.hotkey('ctrl', 't')
            listen()
        if "new tab" in command:
            pyautogui.hotkey('ctrl', 't')
            listen()
        if "tab" in command:
            l = command.split()
            i = l.index('tab')
            pyautogui.hotkey('ctrl', l[i + 1])
            listen()
        if "switch window" in command:
            pyautogui.hotkey('alt', 'tab')
            listen()
        if ".com" in command:
            l = command.split()
            i = l.index('start')
            os.system("start " + "www." + l[i+1])
            print("start " + "www." + l[i+1])
            listen()
        if "scroll down" in command:
            l = command.split()
            i = l.index('down')
            for i in range(int(l[i+1])):
                pyautogui.scroll(-10)
            listen()
        #if '.com' is after browser check, program doesn't run .com check suspecting "or" statement interference
        else:
            listen()
        listen()
        #else: what does : mean?
         #   os.system(command + ":")
        #print(type(command))
    except Exception:
        print("Something went wrong")
        listen()

listen()


