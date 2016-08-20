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

coordinate_list = []

coordinate_row = []

for item in range(1, 11):
    for c in range(ord('A'), ord('A') + BOARD_SIZE):
        coordinate_row.append((chr(c), item))
    coordinate_list.append(coordinate_row)
    coordinate_row = []

class Player:
    name = ""

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

# There will be one board with tuples 1 - 10 and A - J
# For each player it will loop through the tuples
# There will be an if conditional to see if tuple is in
# Ship area fields, if they are area will be * or # if the entire ship is sunk
# selected area will also go into a "chosen fields" array. If the tuple is in
# chosen fields, but not in any of the ships, than it will be . , else O

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
            # for x in (6 - 3), 7
            # for x in [3, 4, 5, 6]
            for coord in range((int(coordinates[1]) - (ship.ship_type[1] - 1)), (int(coordinates[1]) + 1)):
                ship_area.append((coordinates[0], coord))
        else:
            # for x in 1, (1 + 5)
            # for x in [1, 2, 3, 4, 5]
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

def print_player_board(player):

    updated_row = []
    print_board_heading()

    if player == player1:
        for row in range(0, 10):
            updated_row.append(str(row + 1).rjust(2))
            for column in coordinate_list[row]:

                if column in aircraft_carrier1.area:
                    if aircraft_carrier1.direction == 'v':
                        updated_row.append(VERTICAL_SHIP)
                    else:
                        updated_row.append(HORIZONTAL_SHIP)
                elif column in battleship1.area:
                    if battleship1.direction == 'v':
                        updated_row.append(VERTICAL_SHIP)
                    else:
                        updated_row.append(HORIZONTAL_SHIP)
                elif column in submarine1.area:
                    if submarine1.direction == 'v':
                        updated_row.append(VERTICAL_SHIP)
                    else:
                        updated_row.append(HORIZONTAL_SHIP)
                elif column in destroyer1.area:
                    if destroyer1.direction == 'v':
                        updated_row.append(VERTICAL_SHIP)
                    else:
                        updated_row.append(HORIZONTAL_SHIP)
                elif column in patrolboat1.area:
                    if patrolboat1.direction == 'v':
                        updated_row.append(VERTICAL_SHIP)
                    else:
                        updated_row.append(HORIZONTAL_SHIP)
                else:
                    updated_row.append(" O")

            print("".join(updated_row))
            updated_row = []
    else:
        for row in range(0, 10):
            updated_row.append(str(row + 1).rjust(2))
            for column in coordinate_list[row]:

                if column in aircraft_carrier2.area:
                    if aircraft_carrier1.direction == 'v':
                        updated_row.append(VERTICAL_SHIP)
                    else:
                        updated_row.append(HORIZONTAL_SHIP)
                elif column in battleship2.area:
                    if battleship1.direction == 'v':
                        updated_row.append(VERTICAL_SHIP)
                    else:
                        updated_row.append(HORIZONTAL_SHIP)
                elif column in submarine2.area:
                    if submarine1.direction == 'v':
                        updated_row.append(VERTICAL_SHIP)
                    else:
                        updated_row.append(HORIZONTAL_SHIP)
                elif column in destroyer2.area:
                    if destroyer1.direction == 'v':
                        updated_row.append(VERTICAL_SHIP)
                    else:
                        updated_row.append(HORIZONTAL_SHIP)
                elif column in patrolboat2.area:
                    if patrolboat1.direction == 'v':
                        updated_row.append(VERTICAL_SHIP)
                    else:
                        updated_row.append(HORIZONTAL_SHIP)
                else:
                    updated_row.append(" O")

            print("".join(updated_row))
            updated_row = []


def clear_screen():
    print("\033c", end="")

def print_board_heading():
    print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))

def start_game():
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

start_game()
