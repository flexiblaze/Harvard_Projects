

#input mostly takes string as default thats why u need to put int etc

def get_guessing():
    guess = (input("Guess a number between 1 and 10: "))
    return guess

def main():
    guessed = get_guessing()
    if guessed == "fifty":
        print("Goodboy")
    else:
        print("hell nah")
    print(guessed)

main()