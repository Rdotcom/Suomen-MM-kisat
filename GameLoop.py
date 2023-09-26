import time
import math


def airportdistance():
    airportdistance
    # lasketaan lentomatka lentokenttien välillä


player_name = input("Enter your name: ")
money = 100  # Starting money
player_range = 0  # Starting range
player_lives = 3  # Starting lives
game_over = False
win = False

starting_airport = "KJFK"  # tai airport[0]['ident']
current_airport = starting_airport
end_airport = "LAX"  # Los Angeles

questions = [
    {
        "question": "Mikä on kullan kemiallinen merkki?",
        "choices": ["k", "au", "ag", "cu"],
        "correctanswer": "au",
        "time_limit": 15
    }
]

# Game loop
while not game_over:
    # Check if the player has reached the destination
    if current_airport == end_airport:
        print("You win! You have reached your destination!")
        game_over = True
        win = True

    # Display player's current status
    airport = 'JFK Airport'  # Starting at JFK Airport
    #print(f'{player_name}, you are at', airport)
    print(f"You have {money}$, {player_lives} lives left and {player_range} range")
    print("\033[34m---------------------------------------\033[0m")


    print("You need to answer questions to get range")
    print("You have 15 seconds to answer the question")
    input("\033[34mPress Enter when you are ready to answer\033[0m")
    print(questions[0]['question'])

    answer = input("Enter your answer: ")

    # If all answers incorrect, goes back one airport
    if answer.lower() == questions[0]['correctanswer'].lower():
        print("Correct answer!")
        player_range += 500
    else:
        print("Wrong answer! You lose range")
        if player_range > 0:
            player_range -= 100





    airportdistance = 500 # need to calculate distance between airports
    if player_range >= airportdistance:
        print("You have enough range to get to your next destination")
        input("\033[32mPress Enter to use your range\033[0m")

        #current_airport = next_airport  # siirtyy seuraavaan lentokenttään
        print("Welcome to {next_airport}")
        player_range -= airportdistance

    elif player_range <= 0 and money >= 100:
        print("You have run out of range")
        print("You have chosen to buy another change for 100$")
        money -= 100
        # takaisin kysymykset kohtaan

    elif player_range <= 0 < player_lives and money <= 0:
        print("You have run out of range and money")
        print("You have lost one life")
        print(f"{player_lives} lives left")
        player_lives -= 1
        # takaisin kysymykset kohtaan
    else:
        print("You have run out of range, money and lives")
        print("You have lost the game")
        game_over = True
