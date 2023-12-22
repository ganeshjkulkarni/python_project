"""Treasure Island"""

print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
print("You are at a cross road. Where do you want to go? Type \"left\" or \"right\"")
cross_road_turn = input()
if cross_road_turn == 'left':
    print("You come to a lake. The is an island in the middle of the lake. "
          "Type \"wait\" to wait for the boat. Type \"swim\" to swim across.")
    lake_cross = input()
    if lake_cross == 'wait':
        print("There are three doors, Red, Blue and Yellow, which one you want to go in?")
        door = input()
        if door.lower() == 'red':
            print("It's a room full of fire. Game Over!")
        elif door.lower() == 'yellow':
            print("You found the treasure! You win!")
        elif door.lower() == 'blue':
            print("You enter a room of beats. Game over!")
        else:
            print("You choose a door that doesn't exist. Game over!")
    else:
        print("You got attacked by a hungry Lion, Game over!")
else:
    print("You fell into a hole, Game over!")

