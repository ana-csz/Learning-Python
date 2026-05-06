import random

class Character:
    def __init__(self, job_class, hp, atk, defense):
        self.job_class = job_class
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def is_alive(self):
        return self.hp > 0

    def attack(self, target):
        damage = max(0, self.atk - target.defense)
        target.hp -= damage
        print(f"{self.job_class} attacked {target.job_class} and dealt {damage} damage!")

    def heal(self):
        amount = 20
        self.hp += amount
        print(f"{self.job_class} used a potion and recovered {amount} HP!")

player = Character("Paladin", 150, 25, 10)
npc = Character("Orc", 200, 35, 15)

while player.is_alive() and npc.is_alive():
    print(f"\n--- STATUS: {player.job_class} HP: {player.hp} | {npc.job_class} HP: {npc.hp} ---")
    
    choice = input("Choose: [1] Attack [2] Heal: ")
    
    if choice == "1":
        player.attack(npc)
    elif choice == "2":
        player.heal()

    if not npc.is_alive():
        print(f"The {npc.job_class} was defeated! You win!")
        break

    if random.randint(1, 2) == 1:
        npc.attack(player)
    else:
        print(f"The {npc.job_class} missed the attack!")

if not player.is_alive():
    print("Game Over!")
      

   
