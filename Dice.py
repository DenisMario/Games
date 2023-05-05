import random
repeat= True
while repeat:
    print("You rolled a", random.randint (1,6))
    print("Do you wanna roll again?")
    repeat= 'y' in input()
