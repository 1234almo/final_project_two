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

