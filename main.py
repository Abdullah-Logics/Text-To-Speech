import pyttsx3

def say(prompt):

    engine = pyttsx3.init()

    engine.getProperty("rate")
    engine.setProperty("rate", 130)

    engine.say(prompt)
    engine.runAndWait()

print("---------Welcome to ROBO_Speaker---------")
print("------Created by Abdullah Bin Usman------\n")

while True:
    prompt = input("Enter What you want me to say: ")
    if prompt.lower() == "exit":
        print("Good Bye")
        say("Good Bye")
        break
    say(prompt)
