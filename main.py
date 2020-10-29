import speech_recognition as sr
import os
r = sr.Recognizer()
#r.energy_threshold = 100

with sr.Microphone(device_index=3) as source:
    r.adjust_for_ambient_noise(source, duration=0.5)
    print('listening')
    audio = r.listen(source)
try:
    command = r.recognize_google(audio)
    print("Predictions: " + command)
    #print(type(command))
except Exception:
    print("Something went wrong")

os.system(command + ":")
