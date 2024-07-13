from random import randint

name = input("")
print("Welcome to the higher/lower game,", name + "!")

while True:
    lower = int(input("Enter the lower bound: "))
    upper = int(input("Enter the upper bound: "))
    if lower < upper:
        break
    print("The lower bound must be less than the upper bound. \n")

random_int = randint(lower, upper)
print()


user_num = int(input("Great, now guess a number between {} and {}: ".format(lower, upper)))

while random_int != user_num:
    if user_num < random_int:
        print("Nope, too low.\n")
    if user_num > random_int:
        print("Nope, too high.\n")
    user_num = int(input("Guess another number: "))
    print(user_num)

print("You got it!")
