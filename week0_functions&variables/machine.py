emoticon = "v.v"


def main():
    global emoticon # change the emotion , make it globally here
    say("is anyone there?")
    emoticon = ":D"
    say("wassupp")


def say(phrase):
    print(phrase + " " + emoticon)


main()