



def convert(text):

    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    get_input = input("Input: ")
    print(convert(get_input))

main()