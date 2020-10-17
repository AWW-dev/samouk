rock = []
country = []

def collect_song():
    song = "Wpisz tytuł piosenki "
    ask = "Wciśniej r lub c albo q, aby wyjsc: "

    while True:
        genre = input(ask)

        if genre == "q":
            break

        if genre == "r":
            rk = input(song)
            rock.append(rk)

        elif genre == "c":
            ck = input(song)
            country.append(ck)

        else:
            print("Nieprawidłowe polecenie!")

    print(rock)
    print(country)

collect_song()