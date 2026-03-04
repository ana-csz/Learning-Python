Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

question1 = int(input("Do you like Dawn or Dusk? 1) Dawn 2) Dusk "))

print("Your answer was:", question1)

if question1 == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif question1 == 2:
  Hufflepuff += 1
  Slytherin += 1
else: print("Wrong input.")

question2 = int(input("When I'm dead, I want people to remember me ass: 1) The Good 2) The Great 3) The Wise 4) The Bold "))

print("Your answer was:", question2)

if question2 == 1:
  Hufflepuff += 2
elif question2 == 2:
  Slytherin += 2
elif question2 == 3:
  Ravenclaw += 2
elif question2 == 4:
  Gryffindor += 2
else:
  print("Wrong input.")

question3 = int(input("Wich kind of instrument most pleases your ear? 1) The Violin 2) The trumpet 3) The piano 4) The Drum "))

print("Your answer was:", question3)

if question3 == 1:
  Slytherin += 4
elif question3 == 2:
  Hufflepuff += 4
elif question3 == 3:
  Ravenclaw += 4
elif question3 == 4:
  Gryffindor += 4
else:
  print("Wrong input.")

scores = [Gryffindor, Ravenclaw, Hufflepuff, Slytherin]
houses = ["Gryffindor", "RavenClaw", "Hufflepuff", "Slytherin"]
max_score = max(scores)
house_index = scores.index(max_score)
print("The house you belong to is:", houses[house_index])


