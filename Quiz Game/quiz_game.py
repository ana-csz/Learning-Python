print("Welcome to my Quizz!")
answer_user = input("Do you want start the Quizz? (Y/N) ")

if answer_user != "Y":
    quit()

score = 0

print("Começando...") 

print("Who developed the GTA V game? \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n")
answer_1 = input("Your answer: ")

if answer_1 == "A": 
    print("Correct!")
    score = score + 10
else: 
    print("Incorrect!")

print("What is the best-selling video game of all time? \n (A) Grand Theft Auto V \n (B) Tetris \n (C) Minecraft \n (D) Super Mario Bros. \n")
answer_2 = input("Your answer: ")

if answer_2 == "C": 
    print("Correct!")
    score = score + 10
else: 
    print("Incorrect!")

print("In the original Donkey Kong arcade game, what was Mario's first name? \n (A) Carpenter \n (B) Jumpman \n (C) Plumber\n (D) Redman \n")
answer_3 = input("Your answer: ")

if answer_3 == "B": 
    print("Correct!")
    score = score + 10
else: 
    print("Incorrect!")

print("What does the acronym RPG stand for in gaming? \n (A) Real-time Playing Game \n (B) Role-Playing Game \n (C) Random Player Game \n (D) Run and Play Game \n")
answer_4 = input("Your answer: ")

if answer_4 == "B": 
    print("Correct!")
    score = score + 10
else: 
    print("Incorrect!")

print("Which popular indie farming simulation game features a distinct pixel art style and was developed by a single person? \n (A) Terraria \n (B) Harvest Moon \n (C) Animal Crossing \n (D) Stardew Valley \n")
answer_5 = input("Your answer: ")

if answer_5 == "D": 
    print("Correct!")
    score = score + 10 
else: 
    print("Incorrect!")

print("What is the highest level a player character can naturally reach in the base rules of Dungeons & Dragons 5th Edition? \n (A) 10 \n (B) 20 \n (C) 50 \n (D) 100 \n")
answer_6 = input("Your answer: ")

if answer_6 == "B": 
    print("Correct!")
    score = score + 10 
else: 
    print("Incorrect!")

print(f"You've reached the end of Quizz! Your score is {score}/60")
