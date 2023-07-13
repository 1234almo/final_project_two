import random

SHIP_SIZES = [5, 3, 3, 2, 2, 2]

def draw_battleship_map(ship_positions):
    # Function to create the map of the game
    grid = [['.' for _ in range(10)] for _ in range(10)]
    for positions in ship_positions:
        for position in positions:
            x, y = position
            grid[y][x] = 'X'
    for row in grid:
        print(' '.join(row))
    print("-----------------------")


def place_user_ships():
    # Function that allows user to place their ships on the map
    ships = []
    for ship_size in SHIP_SIZES:
        while True:
            try:
                print(f"Placing a ship of size {ship_size}")
                x = int(input("Enter the X coordinate for your ship (0-9): "))
                y = int(input("Enter the Y coordinate for your ship (0-9): "))
                if 0 <= x <= 9 and 0 <= y <= 9:
                    ship = [(x, y)]
                    direction = input("Enter the direction (h for horizontal, v for vertical): ")
                    for i in range(1, ship_size):
                        if direction == 'h':
                            new_position = (x + i, y)
                        if direction == 'v':
                            new_position = (x, y + i)
                        else:
                            print("Invalid letter. Try again.")
                        if new_position[0] <= 9 and new_position[1] <=9:
                            ship.append(new_position)
                        else:
                            raise ValueError("Invalid ship position. Try again.")
                    overlapping_positions = set(position for existing_ship in ships for position in existing_ship) & set(ship)
                    if not overlapping_positions:
                        ships.append(ship)
                        draw_battleship_map(ships)
                        break
                    else:
                        print("The position already contains a ship. Try again.")
                else:
                    print("Coordinates are out of range. Try again.")
            except ValueError:
                print("Invalid input. Try again.")
    return ships


def place_computer_ships():
    # Function that randomly places computer ships on the board without showing the board to the player
    ships = []
    for ship_size in SHIP_SIZES:
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            ship = [(x, y)]
            direction = random.choice(['h', 'v'])
            for i in range(1, ship_size):
                if direction == 'h':
                    new_position = (x + i, y)
                else:
                    new_position = (x, y + i)
                if new_position[0] <= 9 and new_position[1] <=9:
                    ship.append(new_position)
                else:
                    break   
            if all(position not in ships for position in ship):
                ships.append(ship)
                break
    return ships


def check_destroyed_ship(position, ships):
    # Function that checks if a ship is destroyed after every move
    for ship in ships:
        if position in ship:
            ship.remove(position)
            if not ship:
                ships.remove([])
                return True
            else:
                return len(ship)
    return False


def select_next_target(previous_hit, ship_positions):
    # Function to select the next target position next to the previous hit
    x, y = previous_hit
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    valid_neighbors = [neighbor for neighbor in neighbors if neighbor not in ship_positions and 0 <= neighbor[0] <= 9 and 0 <= neighbor[1] <= 9]
    if valid_neighbors:
        return random.choice(valid_neighbors)
    else:
        return None



def play_battleship():
    # Function that puts everything above together to be able to play the game
    user_ships = place_user_ships()
    computer_ships = place_computer_ships()
    user_remaining_ships = list(user_ships)
    computer_remaining_ships = list(computer_ships)
    user_score = 0
    computer_score = 0
    previous_computer_hit = None
    next_computer_target = None

    while user_remaining_ships and computer_remaining_ships:
        # User's turn
        valid_user_guess = False
        while not valid_user_guess:
            try:
                user_guess_x = int(input("Enter the X coordinate to guess the computer's ship: "))
                user_guess_y = int(input("Enter the Y coordinate to guess the computer's ship: "))
                if 0 <= user_guess_x <= 9 and 0 <= user_guess_y <= 9:
                    valid_user_guess = True
                else:
                    print("Coordinates are out of range. Try again.")
            except ValueError:
                print("Invalid input. Try again.")

        user_guess = (user_guess_x, user_guess_y)

        ship_size = check_destroyed_ship(user_guess, computer_remaining_ships)
        if ship_size:
            print(f"Congratulations! You hit a computer's ship, remaining size {ship_size}.")
            user_score += 1
            if not computer_remaining_ships:
                break
        else:
            print("You missed!")

        # Computer's turn
        if previous_computer_hit and next_computer_target:
            computer_guess = next_computer_target
        else:
            computer_guess_x = random.randint(0, 9)
            computer_guess_y = random.randint(0, 9)
            computer_guess = (computer_guess_x, computer_guess_y)

        print("Computer's guess:", computer_guess)

        ship_size = check_destroyed_ship(computer_guess, user_remaining_ships)
        if ship_size:
            print(f"Oh no! The computer hit one of your ships, remaining size {ship_size}.")
            computer_score += 1
            previous_computer_hit = computer_guess
            next_computer_target = select_next_target(computer_guess, user_remaining_ships)
            if not user_remaining_ships:
                break
        else:
            print("The computer missed!")
            previous_computer_hit = None
            next_computer_target = None

        print("Your ships remaining:", len(user_remaining_ships))
        print("Computer's ships remaining:", len(computer_remaining_ships))
        print("-----------------------")

    # Determine the winner
    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif user_score < computer_score:
        print("Sorry! The computer won the game!")
    else:
        print("It's a tie!")


play_battleship()


