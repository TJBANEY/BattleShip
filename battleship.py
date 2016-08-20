SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]

BOARD_SIZE = 10

VERTICAL_SHIP = ' |'
HORIZONTAL_SHIP = ' -'
EMPTY = 'O'
MISS = '.'
HIT = '*'
SUNK = '#'

player1_guesses = []
player2_guesses = []

coordinate_list = []
coordinate_row = []

for item in range(1, 11):
    for c in range(ord('A'), ord('A') + BOARD_SIZE):
        coordinate_row.append((chr(c), item))
    coordinate_list.append(coordinate_row)
    coordinate_row = []

class Player:
    name = ""

    def __str__(self):
        return "{}".format(self.name)

class Ship:
    name = ""
    ship_type = ""
    area = []
    direction = ""
    vector = ""

    def __str__(self):
        return "{}".format(self.ship_type)

player1 = Player()

aircraft_carrier1 = Ship()
aircraft_carrier1.ship_type = SHIP_INFO[0]

battleship1 = Ship()
battleship1.ship_type = SHIP_INFO[1]

destroyer1 = Ship()
destroyer1.ship_type = SHIP_INFO[3]

patrolboat1 = Ship()
patrolboat1.ship_type = SHIP_INFO[4]

submarine1 = Ship()
submarine1.ship_type = SHIP_INFO[2]

player2 = Player()

aircraft_carrier2 = Ship()
aircraft_carrier2.ship_type = SHIP_INFO[0]

battleship2 = Ship()
battleship2.ship_type = SHIP_INFO[1]

destroyer2 = Ship()
destroyer2.ship_type = SHIP_INFO[3]

patrolboat2 = Ship()
patrolboat2.ship_type = SHIP_INFO[4]

submarine2 = Ship()
submarine2.ship_type = SHIP_INFO[2]

player1_ships = [aircraft_carrier1, battleship1, submarine1, destroyer1, patrolboat1]
player2_ships = [aircraft_carrier2, battleship2, submarine2, destroyer2, patrolboat2]

def valid_input(input):    
    input_list = [item for item in list(input) if item != ' ']

    if ord(input_list[0].upper()) in range(ord('A'), (ord('Z') + 1)):
        try:
            int(input_list[1])
        except:
            return "Second entry must be a number between 1 - 10"
        else:
            if int(input_list[1]) in range(1, 11):
                return True
            else:
                return "Second entry must be a number between 1 - 10"
    else:
        return "First entry must be a letter"

def valid_placement(start, direction, vector):
    if direction == 'v':
        if vector == 'u':
            if (int(start[1]) - 5) < 0:
                return "Invalid ship placement"
            else:
                return True
        else:
            if (int(start[1]) + 5 > 10):
                return "Invalid ship placement"
            else:
                return True
    else:
        if vector == 'l':
            if (ord(start[0].upper()) - 5) < ord('A'):
                return "Invalid ship placement"
            else:
                return True
        else:
            if (ord(start[0].upper()) + 5) > ord('J'):
                return "Invalid ship placement"
            else:
                return True

def prompt_player_for_name():
    player1.name = input("Player 1, please enter your name: ")

    clear_screen()

    player2.name = input("Player 2, please enter your name: ")

    clear_screen()

def prompt_player_for_position(player, ship):

    while True:
        ship_start = input("{}, enter starting position for your {} e.g A2 ".format(player.name, ship))
        if valid_input(ship_start) == True:
            ship_start = [item for item in list(ship_start) if item != ' ']
            break
        else:
            print(valid_input(ship_start))

    ship.direction = input("Choose either horizontal or vertical: h/v ? ")

    while True:
        if ship.direction == 'v':
            ship.vector = input('Choose direction(up/down) u/d: ')
            if valid_placement(ship_start, ship.direction, ship.vector) == True:
                break
            else:
                print(valid_placement(ship_start, ship.direction, ship.vector))
        else:
            ship.vector = input('Choose direction(left/right) l/r: ')
            if valid_placement(ship_start, ship.direction, ship.vector) == True:
                break
            else:
                print(valid_placement(ship_start, ship.direction, ship.vector))


    coordinates = list(ship_start)

    ship_area = []
    if ship.direction == 'v':
        if ship.vector == 'u':
            for coord in range((int(coordinates[1]) - (ship.ship_type[1] - 1)), (int(coordinates[1]) + 1)):
                ship_area.append((coordinates[0], coord))
        else:
            for coord in range(int(coordinates[1]), (int(coordinates[1]) + ship.ship_type[1])):
                ship_area.append((coordinates[0], coord))
        ship.area = ship_area
        ship_area = []
    else:
        if ship.vector == 'l':
            for coord in range((ord(coordinates[0]) - (ship.ship_type[1]) + 1), (ord(coordinates[0]) + 1)):
                ship_area.append((chr(coord), int(coordinates[1])))
        else:
            for coord in range(ord(coordinates[0]), (ord(coordinates[0]) + ship.ship_type[1])):
                ship_area.append((chr(coord), int(coordinates[1])))
        ship.area = ship_area
        ship_area = []

    clear_screen()
    print_player_board(player)

def win_status(player):
    if player == player1:
        if ship_sunk(aircraft_carrier2, player1):
            if ship_sunk(battleship2, player1):
                if ship_sunk(patrolboat2, player1):
                    if ship_sunk(submarine2, player1):
                        if ship_sunk(destroyer2, player1):
                            print("player 1 has won")
                            return True

        return False
    else:
        if ship_sunk(aircraft_carrier1, player2):
            if ship_sunk(battleship1, player2):
                if ship_sunk(patrolboat1, player2):
                    if ship_sunk(submarine1, player2):
                        if ship_sunk(destroyer1, player2):
                            print("player 2 has won")
                            return True
        return False

def print_player_board(player):
    if player == player1:
        ships = player1_ships
        guesses = player2_guesses
        opponent = player2
    else:
        ships = player2_ships
        guesses = player1_guesses
        opponent = player1

    updated_row = []
    print_board_heading()

    for row in range(0, 10):
        updated_row.append(str(row + 1).rjust(2))
        for column in coordinate_list[row]:
            in_ship = False
            for ship in ships:
                if column in ship.area:
                    in_ship = True
                    if column in guesses:
                        if ship_sunk(ship, opponent):
                            updated_row.append(" #")
                        else:
                            updated_row.append(" *")
                    else:
                        if ship.direction == "v":
                            updated_row.append(VERTICAL_SHIP)
                        else:
                            updated_row.append(HORIZONTAL_SHIP)
            if not in_ship:
                if column in guesses:
                    updated_row.append(" .")
                else:
                    updated_row.append(" O")
            else:
                continue

        print("".join(updated_row))
        updated_row = []

def print_opponent_board(player):
    if player == player1:
        ships = player1_ships
        guesses = player2_guesses
    else:
        ships = player2_ships
        guesses = player1_guesses

    updated_row = []
    print_board_heading()

    for row in range(0, 10):
        updated_row.append(str(row + 1).rjust(2))
        for column in coordinate_list[row]:
            in_ship = False
            for ship in ships:
                if column in ship.area:
                    in_ship = True
                    if column in guesses:
                        if ship_sunk(ship, player):
                            updated_row.append(" #")
                        else:
                            updated_row.append(" *")
                    else:
                        updated_row.append(" O")

            if not in_ship:
                if column in guesses:
                    updated_row.append(" .")
                else:
                    updated_row.append(" O")

        print("".join(updated_row))
        updated_row = []

def ship_sunk(ship, opponent):
    if opponent == player2:
        for area in ship.area:
            if area not in player2_guesses:
                return False
    else:
        for area in ship.area:
            if area not in player1_guesses:
                return False

    return True

def clear_screen():
    print("\033c", end="")

def print_board_heading():
    print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))

def player_turn(player, opponent):
    while True:
        start = input("{}, it is your turn. Press enter to continue: ".format(player.name))
        if start == "":
            break
        else:
            print("Something went wrong !")

    # top board should be where you have gone
    # button board is your board with players guesses

    clear_screen()


    print_opponent_board(opponent)
    print(" ")
    print_player_board(player)

    choice = input("{}, Enter a place to hit: ".format(player.name))
    choice = list(choice)
    choice = (choice[0], int(choice[1]))

    if player == player1:
        player1_guesses.append((choice[0], int(choice[1])))
    else:
        player2_guesses.append((choice[0], int(choice[1])))

    if player is player1:
        ship_list = [aircraft_carrier2, battleship2, destroyer2, patrolboat2, submarine2]
    else:
        ship_list = [aircraft_carrier1, battleship1, destroyer1, patrolboat1, submarine1]

    miss = True
    for ship in ship_list:
        if choice in ship.area:
            message = "You hit one of their ships!"
            miss = False
    if miss:
        message = "You missed"

    if win_status(player) == True:
        play_again = input("Congratulations ! You won. Play Again ? y/n ")
        if play_again == 'y':
            start_game()
        else:
            clear_screen()
    else:
        while True:
            proceed = input("{}, press enter to continue: ".format(message))

            if proceed == "":
                break

        clear_screen()
        player_turn(opponent, player)

def start_game():
    clear_screen()
    prompt_player_for_name()

    prompt_player_for_position(player1, aircraft_carrier1)
    prompt_player_for_position(player1, battleship1)
    prompt_player_for_position(player1, submarine1)
    prompt_player_for_position(player1, destroyer1)
    prompt_player_for_position(player1, patrolboat1)

    prompt_player_for_position(player2, aircraft_carrier2)
    prompt_player_for_position(player2, battleship2)
    prompt_player_for_position(player2, submarine2)
    prompt_player_for_position(player2, destroyer2)
    prompt_player_for_position(player2, patrolboat2)

    # clear_screen()

    player_turn(player1, player2)

start_game()