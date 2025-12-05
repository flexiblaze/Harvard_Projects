




def greeting():
    greet = str(input("Greeting: ")).strip().lower()
    return greet

def main():
    greet = greeting() # python runs the function one time, returned value get stored in greet
    if "hello" in greet:
        print("$0")
    elif greet.startswith("h"): # its explains itself
        print("$20")
    else:
        print("$100")

main()
#/*
#🔍 Analogy (simple)

#Think of greeting() like asking someone a question.

#If you call greeting() twice, it’s like asking:

#“What’s your greeting?”
#(user answers)
#“Okay… what’s your greeting again?”

#But if you do greet = greeting(), you ask once, then use their answer as many times as you want.

