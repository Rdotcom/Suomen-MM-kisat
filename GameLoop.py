import math
from geopy import distance



def airportinfo(): #icao
    #sql database ident, name, latitude_deg, longitude_deg

def airportdistance(current, target):
    # lasketaan lentomatka lentokenttien välillä
    start = airportinfo(current)
    end = airportinfo(target)
    return distance.distance((start['latitude_deg'], start['longitude_deg']),
                             (end['latitude_deg'], end['longitude_deg'])).km



player_name = input("Anna pelaaja nimi: ")
money = 100  # Starting money
player_range = 0  # Starting range
player_lives = 3  # Starting lives
game_over = False
win = False

starting_airport = "KJFK"  # New York
current_airport = starting_airport
end_airport = "LAX"  # Los Angeles


# Game loop
while not game_over:
    # Katsotaan onko pelaaja voittanut pelin
    if current_airport == end_airport:
        print("Sinä voitit pelin! Pääsit päätepysäkille!")
        game_over = True
        win = True

    # Näyttää pelaajan tiedot
    airport = 'JFK Airport'  # Starting at JFK Airport
    print(f"Sinulla on {money}$, {player_lives} elämää jäljellä ja {player_range} rangea")
    print("\033[34m---------------------------------------\033[0m")

    # Ohjeita pelaajalle
    print(f"{player_name}, vastaa kysymyksiin, jotta saat lisää rangea")
    print("Sinulla on 15 sekuntia aikaa vastata")
    input("\033[34mPaina Enter kun olet valmis vastaamaan\033[0m") # Pauses the game before question


    # tarvii timelimit
    # kysymykset


    # jos vastaukset väärin, menee takaisin yhden lentokentän
    # jos yksi, kaksi tai kolme oikein, rangea lisää
    '''
    answer = input("Anna vastaus: ")
    
    if answer.lower() == questions[0]['correctanswer'].lower():
        print("Oikea vastaus!")
        player_range += 500
    else:
        print("Väärä vastaus! Hävisit rangea")
        if player_range > 0:
            player_range -= 100
    '''



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
