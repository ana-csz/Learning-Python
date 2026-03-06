import random

player = {
    "class": "Paladin",
    "hp": 150, 
    "atk": 25, 
    "def": 10
}
npc = {
    "class": "Orc",
    "hp": 200,
    "atk": 35, 
    "def": 15
}

while player["hp"] > 0 and npc["hp"] > 0:
    print(f"\n--- STATUS: {player['class']} HP: {player['hp']} | {npc['class']} HP: {npc['hp']} ---")

    #1. Player Turn
    act = input("Choose your action: [1] Attack [2]Heal: ")

    if act == "1":
        dmg = player["atk"] - npc["def"]
        dmg = max(0, dmg)
        npc["hp"] -= dmg
        print(f"You attacked o {npc['class']} and caused {dmg} damage!")
    elif act =="2":
        heal = 20
        player["hp"] += heal
        print(f"You used a healing potion and recovered {heal} de HP!")

    if npc["hp"] <= 0:
        print(f"The {npc['class']} was defeated! You Win!")
        break

    npc_decision = random.randint(1, 2)
    if npc_decision == 1:
        dmg_npc = npc["atk"] - player["def"]
        dmg_npc = max(0, dmg_npc)
        player["hp"] -= dmg_npc
        print(f"{npc['class']} hit you! You lose {dmg_npc} HP.")
    else:
        print(f"{npc['class']} missed the atacck")

    if player["hp"] <= 0:
        print("You fell in battle... Game Over!")

