import pyttsx3

engine = pyttsx3.init()
while True:
    user=input("Enter what you want me to speak: ")
    if user=="q":
        print("Quitting!!")
        break
    engine.say(user)
    engine.runAndWait()
    