import random

def draw_battleship_map(ship_positions):
    # Function to create the map of the game
    grid = [['.' for point in range(10)] for point in range(10)]
    for position in ship_positions:
        x, y = position
        grid[y][x] = 'X'
    for row in grid:
        print(' '.join(row))


def place_user_ships():
    # Function that allows user to place their ships on the map
    ships = []
    while len(ships) < 7:
        try:
            x = int(input("Enter the X coordinate for your ship (0-9): "))
            y = int(input("Enter the Y coordinate for your ship (0-9): "))
            if 0 <= x <= 9 and 0 <= y <= 9:
                if (x, y) not in ships:
                    ships.append((x, y))
                else:
                    print("This position already contains a ship. Try again.")
            else:
                print("Coordinates are out of range. Try again.")
        except ValueError:
            print("Invalid input. Try again.")
    draw_battleship_map(ships)    
    return ships


def place_computer_ships():
    # Function that randomly places computer ships on the board without showing the board to the player
    ships = []
    while len(ships) < 7:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if (x, y) not in ships:
            ships.append((x, y))
    return ships


def check_destroyed_ship(position, ships):
    # Function that checks if a ship is destroyed after every move
    if position in ships:
        ships.remove(position)
        return True
    return False



def play_battleship():
    # Function that puts everything above together to be able to play the game
    user_ships = place_user_ships()
    computer_ships = place_computer_ships()
    user_score = 0
    computer_score = 0

    while user_ships and computer_ships:
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

        if check_destroyed_ship(user_guess, computer_ships):
            print("Congratulations! You destroyed a computer's ship.")
            user_score += 1
        else:
            print("You missed!")

        # Computer's turn
        computer_guess_x = random.randint(0, 9)
        computer_guess_y = random.randint(0, 9)
        computer_guess = (computer_guess_x, computer_guess_y)
        print("Computer's guess:", computer_guess)

        if check_destroyed_ship(computer_guess, user_ships):
            print("Oh no! The computer destroyed one of your ships.")
            computer_score += 1
        else:
            print("The computer missed!")

        print("Your ships remaining:", len(user_ships))
        print("Computer's ships remaining:", len(computer_ships))
        print("-----------------------")

    # Determine the winner
    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif user_score < computer_score:
        print("Sorry! The computer won the game!")
    else:
        print("It's a tie!")


play_battleship()


