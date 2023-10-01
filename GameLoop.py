import math
from geopy import distance



def airportinfo(): #icao
    #sql database name, latitude_deg, longitude_deg
    return

def airportdistance(current, target):
    # lasketaan lentomatka lentokenttien välillä
    start = airportinfo(current)
    end = airportinfo(target)
    return distance.distance((start['latitude_deg'], start['longitude_deg']),
                             (end['latitude_deg'], end['longitude_deg'])).km






player_name = input("Anna pelaajan nimi: ")
money = 100  # Aloitus rahat
player_range = 0  # Aloitus range
player_lives = 3  # Aloitus elämät
game_over = False
win = False

starting_airport = "KJFK"  # New York
current_airport = starting_airport
end_airport = "LAX"  # Los Angeles


# Game loop
while not game_over:
    # Katsotaan onko pelaaja voittanut pelin
    if current_airport == end_airport:
        print("Voitit pelin! Pääsit päätepysäkille!")
        #käytit ... aikaa
        game_over = True
        win = True


    # Näyttää pelaajan tiedot
    player_info = (f"Sinulla on {money:.0f}$, {player_lives} elämää jäljellä ja {player_range:.0f}km rangea")
    leveys = len(text) + 4
    print("\033[34m" + "-" * leveys + "\033[0m")
    print(f"\033[34m| {player_info} |\033[0m")
    print("\033[34m" + "-" * leveys + "\033[0m")


    # Ohjeita pelaajalle
    print(f"{player_name}, vastaa kysymyksiin, jotta saat lisää rangea")
    print("Sinulla on 15 sekuntia aikaa vastata")
    input("\033[34mPaina Enter kun olet valmis vastaamaan\033[0m") # Paussi ennen kysymyksiä

    # kysymykset


    # timelimit
    starttime = time.time()
    player_answer = input("Vastaus: ")
    timetaken = time.time() - starttime

    if timetaken > time_limit:
        print("Aika loppui kesken!")
    else:
        print("Ehdit vastata ajoissa!")

    # jos vastaukset väärin, menee takaisin yhden lentokentän
    # jos yksi, kaksi tai kolme oikein, rangea lisää
    if correctanswer == 3:
        print("Sait kaikki vastaukset oikein!")
        player_range += 1500
    elif correctanswer == 2:
        print("Sait kaksi vastausta oikein!")
        player_range += 1000
    elif correctanswer == 1:
        print("Sait yhden vastauksen oikein!")
        player_range += 500
    else:
        print("Sait kaikki vastaukset väärin! Menet takaisin yhden lentokentän")
        if currect_airport != "KJFK":
            current_airport = 1#menee takaisin yhden lentokentän




     # lasketaan lentomatka lentokenttien välillä
    distance_km = airportdistance(current_airport, target_airport)

    if player_range >= distance_km:
        print(f"Sinulla on tarpeeksi rangea lentää {target_airport}") # airport name
        input(f"\033[32mPaina Enter käyttääksesi {distance_km} rangea\033[0m")

        # menee seuraavaan lentokenttään
        print("Tervetuloa {next airport}")
        player_range -= airportdistance

    elif player_range <= 0 and money >= 100:
        print("Sinulta loppui range")
        print("Päätit käyttää 100$ uuteen yritykseen")
        money -= 100
        # takaisin kysymykset kohtaan

    elif player_range <= 0 < player_lives and money <= 0:
        print("Sinulta loppui range ja rahat")
        print("Päätit käyttää elämän uuteen yritykseen")
        print(f"{player_lives} elämää jäljellä")
        player_lives -= 1
        # takaisin kysymykset kohtaan
    else:
        print("Sinulta loppui range, rahat ja elämät")
        print("\033[31mHävisit pelin!\033[0m")
        game_over = True
