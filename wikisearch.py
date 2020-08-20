import wikipedia
import speech_recognition as sr

sr.Microphone(device_index=1)
r=sr.Recognizer()
r.energy_threshohold=5000

with sr.Microphone() as source:
    print("Speak")
    audio=r.listen(source)
    try:
         text=r.recognize_google(audio)
         
    except NameError:
        print("Cant recognice")     




wikipedia.search(text)
contentall = (wikipedia.page(text).content)

contentone = contentall.split(".")[0]
contenttwo = contentall.split(".")[1]
print(text)
print(contentone + "." + contenttwo + ".")
