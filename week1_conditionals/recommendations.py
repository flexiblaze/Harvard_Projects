


def main():
    diffuculty = input("Hard or easy")
    if not (diffuculty == "Hard" or "Easy"):
        print("Wrong diffuculty")
        return

    players = int(input("multiplayers or single player: "))
    if not (players == "multiplayers" or "single player"):
        print("Wrong players")
        return
    #boolen operators
    if diffuculty == "Hard" and players == "multiplayers":
        recommend("Poker")
    elif diffuculty == "Hard" and players == "single player":
        recommend("klondike")
    elif diffuculty == "Easy" and players == "multiplayers":
        recommend("hearts")
    else:
        recommend("big boy game")

def recommend(gamename):
    print("You might like", gamename)



main() # calling the main