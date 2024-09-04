import pyttsx3

engine = pyttsx3.init()

if __name__ == "__main__":
    print("welcome")
    while True:
        a = input("enter what you want me to speak: ")
        if (a == "q"):
            engine.say("bye")
            engine.runAndWait()
            break
        engine.say(a)
        engine.runAndWait()