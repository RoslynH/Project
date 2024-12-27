# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

import random
import sys

game_map = {
    "Start_Room": {
        "description": "You are in an empty room. This is where your journey begins. It seems that there is a forest in the north. A large house is visible in the distance to the east. In the west, there is a door, looks kinda scary. ",
        "connections": {"n": "Forest_Trail", "e": "Path", "w": "Stone_Room"},
        "items": {"name": "Sword", "description": "A sharp sword that boosts your attack power.","attack": 10, "picked": False},
        "enemy_chance": 0.0,
        "npcs": [],
        "trap_chance": 0.0,
        "trap_damage": (0, 0),
        "is_maze": False,
        "enemy_defeated": True
        },
    "Path": {
        "description": "You are walking on the path. The large house is nearby.",
        "connections": {"e": "Lobby", "w": "Start_Room"},
        "enemy_chance": 0.8,
        "trap_chance": 0.0,
        "trap_damage": (0, 0),
        "enemy_defeated": False,
        "is_maze": False,
        "items": [],
        "npcs": []
    },
    "Lobby": {
        "description": "You are standing in a lobby. Perhaps there are someone live in here.",
        "connections": {"e": "Guest_Room", "w": "Path", "s1": "Kitchen", "s2": "Library"},
        "enemy_chance": 0.0,
        "trap_chance": 0.0,
        "trap_damage": (0, 0),
        "enemy_defeated": False,
        "is_maze": False,
        "items": [],
        "npcs": []
    },
    "Kitchen": {
        "description": "You are standing in a hot kitchen, where all the foods are made.",
        "connections": {"n": "Lobby"},
        "npcs": ["Cook"],
        "enemy_chance": 0.0,
        "trap_chance": 0.0,
        "trap_damage": (0, 0),
        "enemy_defeated": False,
        "is_maze": False,
        "items": []
    },
    "Guest_Room": {
        "description": "It's a place to rest. No body will interrupt you.",
        "connections": {"w": "Lobby"},
        "heal_points": 50,
        "enemy_chance": 0.0,
        "trap_chance": 0.0,
        "trap_damage": (0, 0),
        "enemy_defeated": False,
        "is_maze": False,
        "items": [],
        "npcs": []
    },
    "Library": {
        "description": "You are in a place surrounded by many books. The owner of this mansion must enjoy knowledge. A phantom figure stands among the piles of books.",
        "connections": {"n": "Lobby"},
        "npcs": ["Librarian"],
        "enemy_chance": 0.0,
        "trap_chance": 0.0,
        "trap_damage": (0, 0),
        "enemy_defeated": False,
        "is_maze": False,
        "items": []
        
    },
    "Forest_Trail": {
        "description": "You are walking on a trial in the forest. This place is somehow creepy. Maybe something is hiding in the bushies.",
        "connections": {"s": "Start_Room", "n": "Natural_Spring"},
        "enemy_chance": 0.4,
        "trap_chance": 0.3,
        "trap_damage": (5, 20),
        "enemy_defeated": False,
        "is_maze": False,
        "items": [],
        "npcs": []
    },
    "Natural_Spring": {
        "description": "You see clear water gushes out from the spring. You feel relaxed standing around the spring. It heals your wound and relieves your exhaustion.",
        "connections": {"n": "Forest", "e": "Temple", "w": "Forest_Trail"},
        "heal_points": 50,
        "enemy_chance": 0.0,
        "trap_chance": 0.0,
        "trap_damage": (0, 0),
        "enemy_defeated": False,
        "is_maze": False,
        "items": [],
        "npcs": []
    },
    "Forest": {
        "description": "You are in a forest, where there are no buildings except for a temple.",
        "connections": {"s": "Natural_Spring", "e": "Temple"},
        "enemy_chance": 0.8,
        "trap_chance": 0.3,
        "trap_damage": (5, 20),
        "enemy_defeated": False,
        "is_maze": False,
        "items": [],
        "npcs": []
    },
    "Temple": {
        "description": "You are in a magnificent temple. In the center of the temple stands an unknown statue of a deity. The temple looks dilapidated, and you wonder if it might hide some treasure within.",
        "connections": {"w1": "Forest", "w2": "Natural_Spring", "e": "Maze"},
        "enemy_chance": 1.0,
        "enemy_defeated": False,
        "is_maze": False,
        "items": {"name": "Greatsword", "description": "A large and heavy greatsword that effectively increases attack power.","attack": 20, "picked": False},
        "trap_chance": 0.0,
        "trap_damage": (0, 0),
        "npcs": []
    },
    "Maze": {
        "description": "You have entered a maze. You might get lost and starve to death, or you might find your way out successfully. Good luck!",
        "connections": {"w": "Temple"},
        "enemy_chance": 0.0,
        "trap_chance": 0.0,
        "trap_damage": (0, 0),
        "enemy_defeated": False,
        "is_maze": True,
        "maze_outcomes": {
            "success": 40,
            "death": 30,
            "rescue": 30
            },
        "items": [],
        "npcs": []
    },
    "Stone_Room": {
        "description": "A room constructed from solid stone bricks, exuding an ancient and sturdy atmosphere.",
        "connections": {"e": "Start_Room", "w": "Stone_Corridor", "s": "Gallery", "n": "Well_Room"},
        "enemy_chance": 0.6,
        "trap_chance": 0.0,
        "trap_damage": (0, 0),
        "enemy_defeated": False,
        "is_maze": False,
        "items": [],
        "npcs": []
    },
    "Stone_Corridor": {
        "description": "You walk down a narrow stone corridor, the walls cold to the touch.",
        "connections": {"e": "Stone_Room", "s": "Boss_Room"},
        "enemy_chance": 0.4,
        "trap_chance": 0.3,
        "trap_damage": (5, 20),
        "enemy_defeated": False,
        "is_maze": False,
        "items": [],
        "npcs": []
    },
    "Gallery": {
        "description": "You enter a gallery, where the walls are adorned with various paintings depicting scenes of adventure and battle. These works feel strangely familiar, as if you have experienced them yourself. To your surprise, the portrait of the woman on the wall suddenly began to speak.",
        "connections": {"n": "Stone_Room"},
        "npcs": ["Portrait_Of_Woman"],
        "enemy_chance": 0.0,
        "trap_chance": 0.0,
        "trap_damage": (0, 0),
        "enemy_defeated": False,
        "is_maze": False,
        "items": []
    },
    "Well_Room": {
        "description": "You stand in a dimly lit room. Strangely, in the center of the room is a well, its water glowing faintly. After drinking the well water, you feel healed.",
        "connections": {"s": "Stone_Room"},
        "heal_points": 50,
        "enemy_chance": 0.0,
        "trap_chance": 0.0,
        "trap_damage": (0, 0),
        "enemy_defeated": False,
        "is_maze": False,
        "items": [],
        "npcs": []
    },
    "Boss_Room": {
        "description": "You enter the boss room, where an enemy awaits you. Prepare for battle!",
        "connections": {"n": "Stone_Corridor", "w": "End_Room"},
        "enemy_chance": 1.0,
        "trap_chance": 0.0,
        "trap_damage": (0, 0),
        "enemy_defeated": False,
        "is_maze": False,
        "items": [],
        "npcs": []
    },
    "End_Room": {
        "description": "This is the end of everything.",
        "connections": {"e": "Boss_Room"},
        "enemy_chance": 0.0,
        "trap_chance": 0.0,
        "trap_damage": (0, 0),
        "enemy_defeated": False,
        "is_maze": False,
        "items": [],
        "npcs": []
    },
}



player = {
    "name": "",
    "current_room": "Start_Room",
    "inventory": [],
    "hp": 100,
    "max_hp": 100,
    "attack": 10,
    "memory": [],
    "maze_outcome": None
}

npcs = {
    "Cook": {
        "greeting": "Hi. Do you want something?",
        "options": {
            "1": {"text": "Do you know me?", "response": "Yes, we were companions on a long journey.", "memory": "Cook: The cook in the mansion was my teammate. He always cooked for us. The food was so good that we often fought for the last bite of the dishes. However, one day he was captured by the master of the mansion. After that, he became the cook of the mansion, forever."},
            "2": {"text": "I want some help.", "response": "Sorry, I can't help you. Now, I'm just a cook in this mansion."},
            "3": {"text": "Just greeting.", "response": "Good luck!"}
            }
        },
    "Librarian": {
        "greeting": "Welcome! How may I assist you?",
        "options": {
            "1": {"text": "Do you know me?", "response": "We were partners. I can still remember your favorite story,'The hero at the end of the dungeon.'.", "memory": "Librarian: The librarian in the mansion was my close friend. We adventured together and fought many monsters. He knew my favorite story, 'The Hero at the End of the Dungeon.' It was also my dream to become the hero who reaches the end of the dungeon. But I failed to save him. His soul has been bound in the endless sea of books."},
            "2": {"text": "Can you give me some advice?", "response": "Of course. The master of this mansion has been gone for a few hours because he obtained something precious from you. Leave the mansion and find him. Don't worry about us. Win back your memory!"},
            "3": {"text": "Just greeting.", "response": "Call me if you needed."}
            }
        },
    "Portrait_Of_Woman": {
        "greeting": "I want to speak with you.",
        "options": {
            "1": {"text": "Well, I lost my memory, but I'm still sure that I've never seen this before.", "response": "I'm so glad to see you again. These paintings only remind me of our adventures and the tragic situations I’ve been through. I wish I could help you, but the only thing I can do is encourage you to escape from the master of this dungeon and the mansion, who separated us and turned me into a portrait.", "memory": "Portrait_Of_Woman: We were teammates before she became a portrait. She was once a brave warrior, beautiful and strong. Together, we defeated many enemies, big and small, and shared many important moments in life, such as her wedding. I don’t know if I will ever have the chance to tell her partner about what happened to her."},
            "2": {"text": "Why can you speak?", "response": "I was turned into a magical portrait because the dungeon master wanted to humiliate us."},
            }
        }
    }
z = 0

enemies = [
    {"name": "Goblin", "hp": 30, "attack": 10},
    {"name": "Orc", "hp": 40, "attack": 10},
    {"name": "Bandit", "hp": 50, "attack": 15},
    {"name": "Minotaur", "hp": 55, "attack": 15},
    {"name": "Slime", "hp": 30, "attack": 10},
    {"name": "Snake", "hp": 45, "attack": 10}
]

def generate_enemy(room):
    if random.random() < game_map[room]["enemy_chance"]:
        enemy = random.choice(enemies)
        return enemy
    return None
    
def fight_enemy(room_name, enemy):
    print(f"{player['name']} and {enemy['name']} start fighting!")
    
    enemy_health = enemy['hp']
    enemy_attack = enemy['attack']
    room_name = player["current_room"]

    while enemy_health > 0 and player["hp"] > 0:
        damage_to_enemy = random.randint(player["attack"] - 5, player["attack"] + 5)
        enemy_health -= damage_to_enemy
        print(f"{player['name']} deals {damage_to_enemy} points of damage. {enemy['name']} remaining hp：{enemy_health}")
        
        if enemy_health <= 0:
            print(f"{player['name']} beats {enemy['name']}！")
            game_map[room_name]["enemy_defeated"] = True
            return True
        
        damage_to_player = random.randint(enemy_attack - 5, enemy_attack + 5)
        player["hp"] -= damage_to_player
        print(f"{enemy['name']} attacks. {player['name']} losts {damage_to_player} points of hp，remaining hp：{player['hp']}")
        
        if player["hp"] <= 0:
            print(f"{player['name']} has been defeated by {enemy['name']} .")
            return False

    return False



def opening() :
    print("Hello! Welcome to the world!")
    print("Adventuer, what is your name?")
    player['name'] = input("Please input your name: ")
    print(f"Hi，{player['name']}！")
    print("It's time to start your adventure.")
    print("You are now sitting on the ground in a dungeon, confused by your situations.")
    print("What happened to you?")
    print("It's kinda weird that you have all your equipment around you. But you don't have any memory about yourself.")
    print(" ")
    print("Yep, I know that I'm a adventurer who is exploring this myhr. However, what actually am I doing these days?")
    print("What is the purpose of exploring the maze?")
    print("It's seems that I have lost all the important memories. What should I do?")
    print("Now, it's time for you to do the dicision that can change your life")

def show_room():
    room = game_map[player["current_room"]]
    print(f"\nYou are now in {player['current_room']}")
    print(room["description"])
    if room["items"]:
        print("There is a item here:")
        for l, m in room["items"].items():
            print(l, ':', m)
    else:
        print("There is no items in the this place")
    if room["enemy_defeated"]:
        print("There's no enemy here.")
    else:
        enemy = generate_enemy(player["current_room"])
        if enemy:
            print(f"There is a {enemy['name']}!")
            result = fight_enemy(room, enemy)
            if not result:
                print("You failed. Game over!")
                return
        else:
            print("There's no enemy here.")
    if random.random() < room["trap_chance"]:
        trap_damage = random.randint(room["trap_damage"][0], room["trap_damage"][1])
        player["hp"] -= trap_damage
        print(f"You trigger the trap. Lost {trap_damage} point of hp. remaining hp：{player['hp']}")
        if player["hp"] <= 0:
            print("You are dead. Game over!")
            return
    if room.get("heal_points", 0) > 0:
        heal = room["heal_points"]
        player["hp"] = min(player["hp"] + heal, player["max_hp"])
        print(f"You have healed {heal} points of hp. Remaing hp：{player['hp']}/{player['max_hp']}")
    if room["npcs"]:
        print("There is someone to talk:")
        print(room["npcs"])
    else:
        print("There's no npc here.")
    if room["is_maze"]:
        enter_maze()
    
        

def talk_to_npc(npc_name):
    npc = npcs[npc_name]
    print(f"{npc_name}: {npc['greeting']}")
    for key, option in npc['options'].items():
        print(f"{key}. {option['text']}")
    choice = input("Please enter your choice: ")    
    if choice in npc['options']:
        selected_option = npc['options'][choice]
        print(f"{npc_name}: {selected_option['response']}")        
        if "memory" in selected_option:
            add_memory(selected_option["memory"])

def add_memory(memory):
    if memory not in player["memory"]:
        player["memory"].append(memory)
        print(f"{player['name']} remember something：{memory}")
    else:
        print(f"{player['name']} alredy have the memory.")

def start_game():
    opening()
    show_room()
    while True:
        if player["current_room"] == "End_Room":
            print("You have successfully made it to the exit of the dungeon, finally able to leave this perilous world. What will the end be?")
            game_over("Successfully make it to the end.")
            break
        if player["hp"] <= 0:
            game_over("You died during the journey.")
            break
        if player["maze_outcome"] == "death":
            game_over("Died in the maze.")
            break
        if player["maze_outcome"] == "rescue":
            game_over("Being rescued.")
            break
        print()
        print("'Action List'")
        print("What do you want to do?")
        print("1: Explore")
        print("2: Talk to NPC")
        print("3: Pick the item")
        print("4: Show my information")
        print("5: Leave the game")
        action = input("Please enter your choice: ")
        if action == "1":
            room = game_map[player["current_room"]]
            available_directions = room["connections"]
            print("Available directions: ")
            for x, y in available_directions.items():
                print(x, ':', y)
            direction = input("Which direction do you want to go?: ").lower()
            if direction in available_directions:
                new_room = room["connections"][direction]
                player["current_room"] = new_room
                show_room()
        elif action == "2":
            room = game_map[player["current_room"]]
            if room["npcs"]:
                print(f"You talk to {room["npcs"]}.")
                npc_name = room["npcs"][0]
                talk_to_npc(npc_name)
            else:
                print("There are no NPCs in this room.")
        elif action == "3":
            room = game_map[player["current_room"]]
            if room["items"]:
                item = room["items"]
                add_weapon(item["name"], item["attack"])
                room["items"] = None
            else:
                print("There is no item to pick up in this room.")
        elif action == "4":
            print("Player Information:")
            for i, j in player.items():
                print(i, ':', j)

        elif action == "5":
            print("Thank you for playing! See you next time.")
            game_over("You leave the game.")
            break




def enter_maze():
    current_room = player["current_room"]
    room = game_map[current_room]
    print("You enter a maze.")
    outcomes = room["maze_outcomes"]
    outcome = random.choices(
        ["success", "death", "rescue"],
        weights=[outcomes["success"], outcomes["death"], outcomes["rescue"]],
        k=1
    )[0]
    
    if outcome == "success":
        print("You successfully navigate through the maze and find the way out.")
        player["current_room"] = "temple"
        return
    elif outcome == "death":
        print("You fail to find the exit and eventually die in front of the sealed door at the maze's entrance.")
        print("You died in the maze.")
        player["maze_outcome"] = "death"
        return
    elif outcome == "rescue":
        print("You are found deep within the maze and successfully rescued.")
        print("An adventuring party leads you out of the maze.")
        player["maze_outcome"] = "rescue"
        return
        

def add_weapon(weapon, attack_bonus):
    player["inventory"].append(weapon)
    player["attack"] += attack_bonus
    print(f"{player['name']} picked up a：{weapon}！ Attack bonus increase {attack_bonus} points！")


def game_over(ending_message):
    print("\n===== Game Over =====")
    print(ending_message)
    print()
    if player["current_room"] == "End_Room": 
        if len(player["memory"]) == 3: 
            print("Somehow, the dungeon master hasn't appeared...")
            print("It seems you've uncovered some of the secrets. There's nothing for you to discovered. Thank you for playing!")
            print("Congratulations! You have found all your companions and the memories with them. Although you can't continue with them, nor can you recover all the memories, please continue to live courageously! Like a 'hero'")
        else:
            print("Somehow, the dungeon master hasn't appeared... Huh? Why am I thinking this? Who is the dungeon master?")
            print("It seems the mystery still lingers. Will you ever understand the full story?")
    print("Player's status at the end of the game:")
    for key, value in player.items():
        print(key, ':', value)
    print("====================")
    input("Press Enter to close the game.")
    sys.exit()
    
    
start_game()
print("Welcome to the 'Dungeon of Memories'")
