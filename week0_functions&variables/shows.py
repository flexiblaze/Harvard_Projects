SHOWS = []


#string methonds


def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append()(show.strip().title()) #all begin of the word

    print(', '.join(cleaned_shows)) #join together

main()
