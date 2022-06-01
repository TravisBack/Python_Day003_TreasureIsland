print("Welcome to Treasure Island!")
print()
print("Your mission is to find the treasure.")
print()

print("You come to a fork in the path.\nTo the left leads to the river.\nTo the right leads to the woods.")
while True:
    answer = input("Do you go <left> or <right>? ")
    if answer == "left" or answer == "right":
        if answer == "left":
            print("You're still alive!")
        if answer == "right":
            print("You get eaten by wolves! Game Over!")
            exit()
        break

print()

print("You make your way to the river.\nYou see the river looks calm but it's wide.\nThere is a dock but no boat.")
while True:
    answer = input("Do you <swim> or <wait>? ")
    if answer == "swim" or answer == "wait":
        if answer == "wait":
            print("You wait for the boat and make it across the river.")
        if answer == "swim":
            print("The river is to rough under the surface that you drown. Game Over!")
            exit()
        break

print()

print("You make it to a small stone building with 3 doors of different colors.")
while True:
    answer = input("Do you choose the <red>, <yellow>, or <blue> door? ")
    if answer == "red" or answer == "yellow" or answer == "blue":
        if answer == "yellow":
            print("You found the treasure! You win!")
        if answer == "red":
            print("You die in an inferno! Game over!")
        if answer == "blue":
            print("You die in an icy blizard! Game over!")
        break
