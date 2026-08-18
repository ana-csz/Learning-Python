import random

print("Welcome to the Guess Number!")

choice_number = input("Enter the maximum challenge number: ")

if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print("Error: The value entered is not an integer. Please run again and enter a number.")
    quit()

random_number = random.randint(8, choice_number)

n_choices = 0

while True:
    answer_user = input("Guess the number: ")

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("Error: The value entered is not an integer. Please run again and enter a number.")
        continue

    n_choices = n_choices + 1
    if answer_user == random_number:
        print("You got it!")
        break
    elif answer_user > random_number:
        print("The random number is less than that.")
    else:
        print("The random number is greater than that.")

print("Number of attempts: " + str(n_choices))
