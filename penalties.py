import random

CENTER = 0
LEFT = 1
RIGHT = 2


def dive():
    number = random.randint(1, 2)
    return number


# Implement your functions here.
def goal(kick_direction, dive_direction):
    if kick_direction == dive_direction:
        return False
    else:
        return True


def print_ball(ball):
    if ball == 1:
        print("-----------------")
        print("| O             |")
        print("|               |")
        print("|               |")

    if ball == 2:
        print("-----------------")
        print("|             O |")
        print("|               |")
        print("|               |")


def print_goalkeeper(goalkeeper):
    if goalkeeper == 1:
        print("-----------------")
        print("| _ o|          |")
        print("|    \          |")
        print("|     \\\        |")

    if goalkeeper == 2:
        print("-----------------")
        print("|          |o _ |")
        print("|          /    |")
        print("|        //     |")


def penalty_shootout(team):
    seed_number = 87
    random.seed(seed_number)

    print("-----------------")
    print("|     _ o _     |")
    print("|       |       |")
    print("|      / \      |")

    number_of_rounds = 1
    team1 = 'Suomi'
    team2 = team
    game_continues = True
    team1_score = 0
    team2_score = 0
    team1_turn = 0
    team2_turn = 0
    current_team = team2
    rounds = 0

    while game_continues:
        if abs(team1_score - team2_score) > (number_of_rounds - rounds) and team1_turn == team2_turn:
            game_continues = False
        else:
            if team1_turn == team2_turn:
                rounds += 1
                print(f'KIERROS {rounds}')
            print(f'{team1} on tehnyt {team1_score} maalia, {team2} on tehnyt {team2_score}.')
            if current_team == team1:
                current_team = team2
                print(f"Nyt on {current_team} joukkueen vuoro!")
                team2_turn += 1
            else:
                current_team = team1
                print(f"Nyt on {current_team} joukkueen vuoro")
                team1_turn += 1

            if current_team == team1:
                kick = int(input(f"Kumpaan suuntaan pelaaja vetää?? (1: vasemmalle/2: oikealle)\n"))
                while kick != 1 and kick != 2:
                    print(f'Syötä 1 tai 2')
                    kick = int(input(f"Kumpaan suuntaan pelaaja vetää? (1: vasemmalle/2: oikealle)\n"))
            else:
                kick = random.randint(1, 2)

            if current_team == team2:
                dive_direction = int(input(f"Minne maalivahti hyppää? (1: vasemmalle/2: oikealle)\n"))
                while dive_direction != 1 and dive_direction != 2:
                    print(f'Syötä 1 tai 2')
                    dive_direction = int(input(f"Minne maalivahti hyppää? (1: vasemmalle/2: oikealle)\n"))
            else:
                dive_direction = dive()

            if goal(kick, dive_direction):
                print(f'Veto: {kick} Torjunta: {dive_direction}')
                print(f"Ja veto menee...")
                print_ball(kick)
                print(f"Ja maalivahti menee...")
                print_goalkeeper(dive_direction)
                print(f'{current_team} sai maalin!')

                if current_team == team1:
                    team1_score += 1
                else:
                    team2_score += 1

            else:
                print(f'Veto: {kick} Torjunta: {dive_direction}')
                print(f"Ja veto menee...")
                print_ball(kick)
                print(f"Ja maalivahti menee...")
                print_goalkeeper(dive_direction)
                print(f'Ei maalia. Maalivahti torjui vedon!')

            if rounds >= number_of_rounds and team1_score == team2_score and team1_turn == team2_turn:
                print("Tasapeli! Siirrytään äkkikuolema -kierroksiin!")
                number_of_rounds += 1

    print(f'{team1} yritykset: {team1_turn}')
    print(f'{team2} yritykset: {team2_turn}')
    print(f"Peli päättyi! {team1} teki {team1_score} ja {team2} teki {team2_score}")
    if team1_score > team2_score:
        return team1
    elif team2_score > team1_score:
        print(f"Ottelun voittaja on {team2}!")
        return team2