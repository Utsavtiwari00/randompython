import random
level = int(input("level= "))
randomNumber = random.randint(1,level)
while True:
    try:
        userguess= int(input("Enter a number: "))

        if userguess>randomNumber:
            print("Too big!")
        elif userguess<randomNumber:
            print("Too small!")
        else:
            print("Just right!")
            break
    except ValueError:
        print("Not a number!")

