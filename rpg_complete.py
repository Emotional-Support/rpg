import random
import sys
import time


def print_animation(text, delay=0.01, delay1=0.1):
    for char in text:
        print(char, end="", flush=True)
        if char not in ["!", ".", ":"]:
            time.sleep(delay)
        else:
            time.sleep(delay1)
    print()


user_hp = 100
user_inventory = ["Fist"]
user_coins = 100
opponent_hp = 100
shop = {
    "1": {"1": ["Iron Greatsword", 50], "2": ["Silver Dagger", 50]},
    "2": {
        "1": ["Health Potion", 25],
        "2": ["Strength Potion", 50],
        "3": ["Weakness potion", 50],
    },
    "3": {"1": ["Slingshot", 25]},
    "4": {
        "1": ["Archangel's Smite", 125],
        "2": ["Bloody Chalice", 125],
    },
    "5": {"1": ["The Shard of Oblivion", 150], "2": ["Ethereal Prism", 150]},
}

names = ["George", "Brian", "Stacy", "Kevin", "Mike", "Alyssa", "Tom", "Anna", "Dave"]
cool_names = {
    "George": [
        " ██████╗ ███████╗ █████╗ ██████╗  ██████╗ ███████╗",
        "██╔════╝ ██╔════╝██╔══██╗██╔══██╗██╔════╝ ██╔════╝",
        "██║  ██╗ █████╗  ██║  ██║██████╔╝██║  ██╗ █████╗ ",
        "██║  ╚██╗██╔══╝  ██║  ██║██╔══██╗██║  ╚██╗██╔══╝  ",
        "╚██████╔╝███████╗╚█████╔╝██║  ██║╚██████╔╝███████╗",
        " ╚═════╝ ╚══════╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝",
    ],
    "Brian": [
        "██████╗ ██████╗ ██╗ █████╗ ███╗  ██╗",
        "██╔══██╗██╔══██╗██║██╔══██╗████╗ ██║",
        "██████╦╝██████╔╝██║███████║██╔██╗██║",
        "██╔══██╗██╔══██╗██║██╔══██║██║╚████║",
        "██████╦╝██║  ██║██║██║  ██║██║ ╚███║",
        "╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚══╝",
    ],
    "Stacy": [
        " ██████╗████████╗ █████╗  █████╗ ██╗   ██╗",
        "██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚██╗ ██╔╝",
        "╚█████╗    ██║   ███████║██║  ╚═╝ ╚████╔╝",
        " ╚═══██╗   ██║   ██╔══██║██║  ██╗  ╚██╔╝",
        "██████╔╝   ██║   ██║  ██║╚█████╔╝   ██║",
        "╚═════╝    ╚═╝   ╚═╝  ╚═╝ ╚════╝    ╚═╝",
    ],
    "Kevin": [
        "██╗  ██╗███████╗██╗   ██╗██╗███╗  ██╗",
        "██║ ██╔╝██╔════╝██║   ██║██║████╗ ██║",
        "█████═╝ █████╗  ╚██╗ ██╔╝██║██╔██╗██║",
        "██╔═██╗ ██╔══╝   ╚████╔╝ ██║██║╚████║",
        "██║ ╚██╗███████╗  ╚██╔╝  ██║██║ ╚███║",
        "╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝╚═╝  ╚══╝",
    ],
    "Mike": [
        "███╗   ███╗██╗██╗  ██╗███████╗",
        "████╗ ████║██║██║ ██╔╝██╔════╝",
        "██╔████╔██║██║█████═╝ █████╗",
        "██║╚██╔╝██║██║██╔═██╗ ██╔══╝",
        "██║ ╚═╝ ██║██║██║ ╚██╗███████╗",
        "╚═╝     ╚═╝╚═╝╚═╝  ╚═╝╚══════╝",
    ],
    "Alyssa": [
        " █████╗ ██╗   ██╗   ██╗ ██████╗ ██████╗ █████╗",
        "██╔══██╗██║   ╚██╗ ██╔╝██╔════╝██╔════╝██╔══██╗",
        "███████║██║    ╚████╔╝ ╚█████╗ ╚█████╗ ███████║",
        "██╔══██║██║     ╚██╔╝   ╚═══██╗ ╚═══██╗██╔══██║",
        "██║  ██║███████╗ ██║   ██████╔╝██████╔╝██║  ██║",
        "╚═╝  ╚═╝╚══════╝ ╚═╝   ╚═════╝ ╚═════╝ ╚═╝  ╚═╝",
    ],
    "Tom": [
        "████████╗ █████╗ ███╗   ███╗",
        "╚══██╔══╝██╔══██╗████╗ ████║",
        "   ██║   ██║  ██║██╔████╔██║",
        "   ██║   ██║  ██║██║╚██╔╝██║",
        "   ██║   ╚█████╔╝██║ ╚═╝ ██║",
        "   ╚═╝    ╚════╝ ╚═╝     ╚═╝",
    ],
    "Anna": [
        " █████╗ ███╗  ██╗███╗  ██╗ █████╗",
        "██╔══██╗████╗ ██║████╗ ██║██╔══██╗",
        "███████║██╔██╗██║██╔██╗██║███████║",
        "██╔══██║██║╚████║██║╚████║██╔══██║",
        "██║  ██║██║ ╚███║██║ ╚███║██║  ██║",
        "╚═╝  ╚═╝╚═╝  ╚══╝╚═╝  ╚══╝╚═╝  ╚═╝",
    ],
    "Dave": [
        "██████╗  █████╗ ██╗   ██╗███████╗",
        "██╔══██╗██╔══██╗██║   ██║██╔════╝",
        "██║  ██║███████║╚██╗ ██╔╝█████╗",
        "██║  ██║██╔══██║ ╚████╔╝ ██╔══╝",
        "██████╔╝██║  ██║  ╚██╔╝  ███████╗",
        "╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝",
    ],
}
npc_names = []
for _ in range(5):
    n = random.choice(names)
    npc_names.append(n)
    names.remove(n)
easy_stats = {"Type": "Easy", "base_dmg": 1, "max_dmg": 16, "name": npc_names[0], "extra_hp": 0, "title": "Novice Adventurer"}
medium_stats = {
    "Type": "Medium",
    "base_dmg": 6,
    "max_dmg": 20,
    "name": npc_names[1],
    "extra_hp": 15,
    "title": "Skilled Adventurer",
}
hard_stats = {"Type": "Hard", "base_dmg": 8, "max_dmg": 28, "name": npc_names[2], "extra_hp": 25, "title": "Expert Adventurer"}
random_stats = {
    "Type": "Random",
    "base_dmg": random.randint(1, 10),
    "max_dmg": random.randint(16, 28),
    "name": npc_names[3],
    "extra_hp": random.randint(0, 25),
    "title": "Mysterious Traveller",
}

npcs = {
    "1": easy_stats,
    "2": medium_stats,
    "3": hard_stats,
    "4": random_stats,
}

durability = 7
opponent_skip = False
temp_counter = 0
bonus_dmg = False
bonus_amt = 0
bet_count = 0
opponent_weak = False
weak_amt = 0
npc_choice = None
bleed = False
bleed_turns = 0
chosen_weapon = "Fist"
oblivion_active = False


def skip():
    print("Press enter to continue...", end="", flush=True)
    input()
    sys.stdout.write("\033[F\033[K")
    sys.stdout.flush()


def shop_enter():
    global user_coins
    global user_inventory

    print_animation(
        f"Before the match begins, you visit the store. You find some items for sale. You have {user_coins} coins, buy what you need."
    )
    while True:
        if user_coins < 25:
            print_animation("You don't have enough money to buy anything else, you leave the store.")
            break
        buy_choice_1 = input(
            """
 __| |________________| |__ 
(__| |________________| |__)
   | |                | |
   | | 1: Weapons     | |
   | | 2: Usables     | |   
   | | 3: Sidearms    | |
   | | 4: Artifacts   | |
   | | 5: Spellstones | |
 __| |________________| |__ 
(__|_|________________|_|__)
   | |                | |

Press q to leave the shop

"""
        )
        if buy_choice_1 == "1":
            buy_choice = input(
                """
The store currently has these weapons in stock:

 __| |_______________________________| |__
(__| |_______________________________| |__)
   | |                               | |
   | | 1: Iron Greatsword - 50 coins | |
   | | 2: Silver Dagger - 50 coins   | |   
 __| |_______________________________| |__ 
(__|_|_______________________________|_|__)
   | |                               | |

Press q to leave the shop
Press b to go back

"""
            )
        elif buy_choice_1 == "2":
            buy_choice = input(
                """
The store currently has these usables in stock:

 __| |_______________________________| |__
(__| |_______________________________| |__)
   | |                               | |
   | | 1: Health Potion - 25 coins   | |
   | | 2: Strength Potion - 50 coins | |
   | | 3: Weakness potion - 50 coins | | 
 __| |_______________________________| |__ 
(__|_|_______________________________|_|__)
   | |                               | |

Press q to leave the shop
Press b to go back

"""
            )
        elif buy_choice_1 == "3":
            buy_choice = input(
                """
The store currently has these sidearms in stock:

 __| |_______________________________| |__
(__| |_______________________________| |__)
   | |                               | |
   | | 1: Slingshot - 25 coins       | |
 __| |_______________________________| |__ 
(__|_|_______________________________|_|__)
   | |                               | |

Press q to leave the shop
Press b to go back

"""
            )
        elif buy_choice_1 == "4":
            buy_choice = input(
                """
The store currently has these sidearms in stock:

 __| |__________________________________| |__
(__| |__________________________________| |__)
   | |                                  | |
   | | 1: Archangel's Smite - 125 coins | |
   | | 2: Bloody Chalice - 125 coins    | |
 __| |__________________________________| |__ 
(__|_|__________________________________|_|__)
   | |                                  | |

Press q to leave the shop
Press b to go back

"""
            )
        elif buy_choice_1 == "5":
            buy_choice = input(
                """
The store currently has these spellstones in stock:

 __| |______________________________________| |__
(__| |______________________________________| |__)
   | |                                      | |
   | | 1: The Shard of Oblivion - 150 coins | |
 __| |______________________________________| |__ 
(__|_|______________________________________|_|__)
   | |                                      | |

Press q to leave the shop
Press b to go back
"""
            )
        if buy_choice_1 == "q" or buy_choice == "q":
            print_animation("You don't find anything useful, and leave the store.")
            break
        elif buy_choice == "b":
            continue
        elif shop[buy_choice_1][buy_choice][1] > user_coins:
            print_animation("You can't afford this...")
        else:
            user_inventory.append(shop[buy_choice_1][buy_choice][0])
            user_coins -= shop[buy_choice_1][buy_choice][1]
            print_animation(f"You have: {[i for i in user_inventory if i != 'Fist']}")
            print_animation(f"You have: {user_coins} coins left")


def start_menu():
    global user_coins
    global user_inventory
    global bet_count
    global npcs
    global npc_choice
    global opponent_hp
    global weapons
    global chosen_weapon
    global oblivion_active
    print_animation("After days of travel, you find yourself at a village.")
    skip()
    print_animation("You head to the arena, but you are stopped by an old man, offering a gamble.")
    skip()
    print_animation("He offers to flip a coin, and double any money you give him if you guess what it lands on.")
    print_animation("If you don't, you lose the money.")
    skip()
    bet_choice = input("Do you agree to the bet (y/n): ")
    if bet_choice == "y":
        bet_amt = int(input("How much do you want to bet: "))
        if bet_amt > user_coins:
            print_animation("You don't have this many coins...")
        else:
            bet_count = bet_amt
            coin_land = random.choice(["h", "t"])
            coin_choice = input("Do you choose heads or tails: ")
            print_animation(f"You guessed {coin_choice}. The coin landed on {coin_land}")
            if coin_choice == coin_land:
                print_animation(f"You won the bet, along with {bet_count} coins!")
                user_coins += bet_count
            else:
                print_animation(f"You lost the bet, along with {bet_count} coins...")
                user_coins -= bet_count

    else:
        print_animation("You decline the old man's offer, and continue.")
    skip()
    shop_enter()
    skip()
    if "The Shard of Oblivion" in user_inventory:
        oblivion_active = True
    x = [k for k in user_inventory if k in ["Iron Greatsword", "Silver Dagger"]]
    if len(x) > 0:
        print_animation("Choose the weapon you want to equip for this battle.")
        weapon_choice = int(input(f"You have these weapons: {x}\n")) - 1
        chosen_weapon = x[weapon_choice]
        print_animation(f"You equipped a {chosen_weapon}!")
        skip()
    npc_choice = input(
        f"""
You enter the arena. Before you begin, you are allowed to choose your opponent.
1: {npc_names[0]} - Easy
2: {npc_names[1]} - Medium
3: {npc_names[2]} - Hard
4: {npc_names[3]} - Random

Type 'info num' to see their individual stats.
"""
    )
    while True:
        if npc_choice.startswith("info") or int(npc_choice) in [1, 2, 3, 4]:
            if npc_choice.startswith("info"):
                info_choice = npc_choice.split(" ")[1]
                if info_choice in npcs.keys():
                    if int(info_choice) != 4:
                        print_animation(
                            f"""
{npcs[info_choice]["name"]}'s Stats:

Name: {npcs[info_choice]["name"]}
Age: {random.randint(16, 32)}
Skillset: {npcs[info_choice]["title"]}

Combat Skills:
Base Damage: {npcs[info_choice]["base_dmg"]}
Max Damage: {npcs[info_choice]["max_dmg"]}
Health: {100+npcs[info_choice]["extra_hp"]}
"""
                        )
                    else:
                        print_animation(
                            f"""
{npcs[info_choice]["name"]}'s Stats:

Name: {npcs[info_choice]["name"]}
Age: Unknown, but looks to be around {random.randint(16, 32)}
Skillset: {npcs[info_choice]["title"]}

Combat Skills:
Base Damage: Unknown
Max Damage: Unknown
Health: Unknown
"""
                        )
                skip()
                npc_choice = input(
                    f"""
You enter the arena. Before you begin, you are allowed to choose your opponent.
1: {npc_names[0]} - Easy
2: {npc_names[1]} - Medium
3: {npc_names[2]} - Hard
4: {npc_names[3]} - Random

Type 'info num' to see their individual stats.
"""
                )
                continue
            else:
                print_animation(f"You chose to fight {npcs[npc_choice]['name']}. Good luck.")
                opponent_hp += npcs[npc_choice]["extra_hp"]
                break

        else:
            print_animation("Huh?")
            npc_choice = input(
                f"""
You enter the arena. Before you begin, you are allowed to choose your opponent.
1: {npc_names[0]} - Easy
2: {npc_names[1]} - Medium
3: {npc_names[2]} - Hard
4: {npc_names[3]} - Random

Type 'info num' to see their individual stats.
"""
            )
            continue


def consumable_use_check(item_index):

    global user_hp
    global shown_items
    global bonus_dmg
    global bonus_amt
    global opponent_hp
    global opponent_weak
    global weak_amt

    if shown_items[item_index] == "Health Potion":
        consumables.remove(consumables[consumables.index(shown_items[item_index])])
        heal_amt = random.randint(12, 20)
        user_hp += heal_amt
        print_animation(f"You healed {heal_amt}. You now have {user_hp} hp.")
    elif shown_items[item_index] == "Strength Potion":
        consumables.remove(consumables[consumables.index(shown_items[item_index])])
        bonus_dmg = True
        bonus_amt = random.randint(8, 12)
        print_animation(f"You feel stronger. You will now do more damage next turn.")

    elif shown_items[item_index] == "Weakness potion":
        consumables.remove(consumables[consumables.index(shown_items[item_index])])
        opponent_weak = True
        weak_amt = random.randint(8, 12)
        print_animation(
            f"You throw the potion of weakness on {npcs[npc_choice]['name']}. He will now do less damage next turn."
        )

    skip()


def artifact_use_check(item_index):
    global user_hp
    global shown_items
    global bonus_dmg
    global bonus_amt
    global opponent_hp
    global opponent_weak
    global weak_amt
    if shown_items[item_index] == "Archangel's Smite":
        my_roll = random.choice(["heads", "tails"])
        my_choice_roll = input(
            "A devil approaches you from the shadows. He presents you with two choices, heads. and tails. Nothing more... nothing less...\n(heads/tails)\n"
        )
        print_animation(
            f'The devil moves his head to your ear, you whisper to him, in the softest of tones, "I choose {my_choice_roll}".'
        )
        skip()
        print_animation(
            "He smiles wearily and reaches into his sleeve. He draws out an old, withered coin. You take one final breath and close your eyes, hoping for the best."
        )
        skip()
        if my_roll == my_choice_roll:
            print_animation(
                f'You open your eyes, and the devil has vanished. You spot the coin on the ground, and on it, in blood red letters, "{my_choice_roll}"'
            )
            skip()
            print_animation(
                f"You breathe a sigh of relief, and suddenly the ground begins to shake, a large skeletal hand emerges from a crack in the ground and throws a deadly spear at {npcs[npc_choice]['name']}, with pinpoint accuracy."
            )
            skip()
            print_animation(
                f"The dagger from the depths pierces {npcs[npc_choice]['name']}'s leg, yet it remains unresponsive. The hand disappears, and the fight still continues."
            )
            skip()
            dmg_smite = random.randint(50, 75)
            opponent_hp -= dmg_smite
            print_animation(
                f"The archangel did {dmg_smite} damage to {npcs[npc_choice]['name']}. {npcs[npc_choice]['name']} now has {opponent_hp if opponent_hp>0 else 0}hp left"
            )
        else:
            print_animation(
                f'You open your eyes, and the devil has vanished. You spot the coin on the ground, and on it, in blood red letters, "{my_roll}"'
            )
            skip()
            print_animation(
                "Before you have time to think, the ground starts to shake. A large skeletal hand emerges from a crack in the ground and hurls a black spear straight at you, with pinpoint accuracy."
            )
            skip()
            print_animation(
                "The projectile, however, stabs into your leg. You reel backwards in pain, injured, but still alive. The fight continues."
            )
            dmg_smite = random.randint(50, 75)
            user_hp -= dmg_smite
            skip()
            print_animation(f"The archangel did {dmg_smite} damage to you. You now have {user_hp if user_hp>0 else 0}hp left")
        artifacts.remove(artifacts[artifacts.index(shown_items[item_index])])
    elif shown_items[item_index] == "Bloody Chalice":
        print_animation(
            "You look into the old bag that a traveller had given you before you started your journey. It had appeared empty, but now you see a glimmer of silver at the bottom."
        )
        skip()
        print_animation(
            "You reach into the bag and pull out the peculiar silver chalice you purchased at the shop. Before your eyes the chalice starts filling itself up with a blood red liquid, tempting you to take a sip."
        )
        skip()
        print_animation("You greedily pour the entire contents of the chalice into your mouth. It is slightly bitter.")
        skip()
        survive_chance = random.choice(["survive", "de"])
        print_animation("Suddenly, you feel a burning sensation rising up from your chest.")
        skip()
        if survive_chance == "die":
            print_animation(
                "You reel backwards in pain, coughing up a little of the liquid, which appears to burn the very rocks in front of you."
            )
            skip()
            print_animation("You take a flask of water and gulp it down, and slowly the pain receeds. But the damage is done.")
            skip()
            print_animation("You have no choice but to continue the battle. You pick up your sword, and the battle continues.")
            skip()
            dmg_chalice = random.randint(30, 50)
            user_hp -= dmg_chalice
            print_animation(f"The chalice did {dmg_chalice} damage to you. You now have {user_hp if user_hp>0 else 0}hp left")
        else:
            print_animation(
                "You fear the worst, but then you feel an incredible burst of strength. You confidently pick up your sword and continue the battle."
            )
            skip()
            input("Your damage will be greatly increased next turn.")
            bonus_dmg = True
            bonus_amt = 32
        artifacts.remove(artifacts[artifacts.index(shown_items[item_index])])
        skip()


def item_use_check(item_index):
    global user_inventory
    global durability
    global opponent_skip
    global shown_items
    global user_hp
    global opponent_hp
    global bonus_dmg
    global bonus_amt
    if shown_items[item_index] == "Slingshot":
        hit_chance = random.randint(1, 100)
        if hit_chance > 10:
            print_animation(
                f"You rolled a {hit_chance}, You use the slingshot to hit {npcs[npc_choice]['name']} with a rock, he appears stunned."
            )
            opponent_skip = True
            break_chance2 = random.randint(1, 7)
            if break_chance2 == durability - 4:
                usable_items.remove(usable_items[usable_items.index(shown_items[item_index])])
                sling_count = len([i for i in shown_items if i == "Slingshot"])
                print_animation(f"Your Slingshot broke! You have {sling_count} remaining.")

        else:
            print_animation(
                f"You rolled a {hit_chance}, You use the slingshot to hit {npcs[npc_choice]['name']} with a pebble. It does nothing."
            )
    else:
        print_animation("Huh?")


def attack():
    global opponent_hp
    global durability
    global bonus_dmg
    global bonus_amt
    global bleed
    global bleed_turns
    global chosen_weapon

    move_choice = input("Do you want to attack high/middle/low: ")
    opponent_choice = random.choice(["h", "m", "l"])
    if move_choice != opponent_choice:
        if chosen_weapon == "Iron Greatsword":
            damage = random.randint(12, 20)
            break_chance = random.randint(1, 7)
            if break_chance == durability:
                user_inventory.remove("Iron Greatsword")
                sword_count = len([i for i in user_inventory if i == "Iron Greatsword"])
                chosen_weapon = "Fist" if sword_count else "Iron Greatsword"
                print_animation(f"Your Iron Greatsword broke! You have {sword_count} remaining.")
        elif chosen_weapon == "Silver Dagger":
            damage = random.randint(8, 14)
            if not bleed:
                bleed = random.choice([True, False])
                if bleed:
                    break_chance = random.randint(1, 4)
                    bleed_turns += random.randint(1, 3)
                    print_animation(
                        f"Your dagger cuts into {npcs[npc_choice]['name']}'s skin, causing a deep wound. {npcs[npc_choice]['name']} winces in pain, but continues the fight."
                    )
            break_chance = random.randint(1, 7)
            if break_chance == durability:
                user_inventory.remove("Silver Dagger")
                sword_count = len([i for i in user_inventory if i == "Silver Dagger"])
                chosen_weapon = "Fist" if sword_count else "Silver Dagger"
                print_animation(f"Your Silver Dagger broke! You have {sword_count} remaining.")
        elif chosen_weapon == "Fist":
            damage = random.randint(1, 26)
        if bonus_dmg:
            damage += bonus_amt
            print_animation(
                f"You hit {npcs[npc_choice]['name']} for {damage-bonus_amt} damage!",
                f"You also did a bonus of {bonus_amt} to deal a total of {damage} damage",
            )
            bonus_dmg = False
            bonus_amt = 0
        else:
            print_animation(f"You hit {npcs[npc_choice]['name']} for {damage} damage!")
        opponent_hp -= damage
    else:
        print_animation(f"{npcs[npc_choice]['name']} defended your attack")
    print_animation(f"{npcs[npc_choice]['name']} has {opponent_hp if opponent_hp>0 else 0} health remaining.")


def use():
    global shown_items
    if len(shown_items) > 0:
        item_index = (
            int(
                input(
                    f"""
You have these usable items: {shown_items}
Type the index of the item to use it.
"""
                )
            )
            - 1
        )
        if shown_items[item_index] in consumables:
            consumable_use_check(item_index)
        elif shown_items[item_index] in usable_items:
            item_use_check(item_index)
        elif shown_items[item_index] in artifacts:
            artifact_use_check(item_index)
    else:
        print_animation("You have no items to use.")
    shown_items = consumables + usable_items + artifacts


def run():
    run_chance = random.randint(1, 100)
    if run_chance > 66:
        print_animation(f"You rolled a {run_chance}. You escaped...")
        exit()
    else:
        print_animation(f"You rolled a {run_chance}. You couldnt escape...")


def change_weapon():
    global chosen_weapon
    k = [i for i in user_inventory if i in {"Iron Greatsword", "Silver Dagger", "Fist"}]
    k.remove(chosen_weapon)
    if len(k) > 0:
        print_animation(f"You have these weapons available: {k}")
        equip_ch = int(input("Which weapon do you want to equip: "))
        chosen_weapon = k[equip_ch - 1]
        print_animation(f"You have equipped: {chosen_weapon}")
    else:
        print_animation("You have no other weapons available.")


def user_turn():
    choice = input("Do you want to attack/run/use/equip: ")
    if choice == "a":
        attack()
    elif choice == "r":
        run()
    elif choice == "u":
        use()
    elif choice == "e":
        change_weapon()
    else:
        print_animation("Huh?")


def opponent_turn():
    global opponent_skip
    global user_hp
    global temp_counter
    global opponent_weak
    global weak_amt
    global npcs
    global npc_choice
    global bleed
    global bleed_turns
    global opponent_hp

    if not opponent_skip:
        opponent_choice = random.choice(["h", "m", "l"])
        my_choice = input(f"{npcs[npc_choice]['name']} is attacking you, do you want to defend high/middle/low: ")
        if my_choice != opponent_choice:
            damage = random.randint(npcs[npc_choice]["base_dmg"], npcs[npc_choice]["max_dmg"])
            if opponent_weak:
                user_hp -= damage - weak_amt
                print_animation(f"{npcs[npc_choice]['name']} hit you for {damage} damage!")
                print_animation(
                    f"But since {npcs[npc_choice]['name']} was weakened, he hit you for {weak_amt} less damage to total {damage - weak_amt} damage."
                )
                opponent_weak = False
                weak_amt = 0
            else:
                user_hp -= damage
                print_animation(f"{npcs[npc_choice]['name']} hit you for {damage} damage!")
            if bleed:
                bleed_turns -= 1
                if bleed_turns > 0:
                    print_animation(
                        f"The stab from your Silver Dagger makes {npcs[npc_choice]['name']} flinch with pain. Blood falls to the ground."
                    )
                    opponent_hp -= 4
                    print_animation(f"{npcs[npc_choice]['name']} takes 4 bleeding damage.")
                    print_animation(f"{npcs[npc_choice]['name']} has {opponent_hp} hp left.")
                else:
                    bleed = False
                    bleed_turns = 0
        else:
            print_animation(f"You defended {npcs[npc_choice]['name']}'s attack")
        print_animation(f"You have {user_hp if user_hp> 0 else 0} health remaining.")

    else:
        print_animation("Its your turn again:")
        if temp_counter >= 1:
            opponent_skip = False
            temp_counter = 0
        temp_counter += 1


def oblivion_shard():
    global user_hp
    global oblivion_active
    respawn_hp = random.randint(20, 30)
    user_hp += respawn_hp
    oblivion_active = False
    print_animation(f"{npcs[npc_choice]['name']}'s Blade pierces through your chest.")
    skip()
    print_animation(f"You feel faint. You collapse on the ground, wincing in pain.")
    skip()
    print_animation(
        "You start to feel something warm in your pocket. You slowly reach in and pull out the obsidian shard you purchased earlier."
    )
    skip()
    print_animation("The shard starts glowing with intense radiance, which envelops the arena.")
    skip()
    print_animation("You see the wound in your chest beginning to fade. You slowly stand up, feeling stronger.")
    skip()
    print_animation("The shard suddenly shatters, and you feel normal again.")
    skip()
    print_animation("The fight continues.")
    skip()
    print_animation(f"You have been reanimated by the shard of oblivion! You now have {respawn_hp} hp.")
    skip()


print_animation("Welcome to...\n\n\n", delay1=0.4)
print(
    """

 █████╗  █████╗  █████╗ ██╗       ██████╗ ██████╗  ██████╗   ████████╗██╗  ██╗██╗███╗  ██╗ ██████╗ 
██╔══██╗██╔══██╗██╔══██╗██║       ██╔══██╗██╔══██╗██╔════╝   ╚══██╔══╝██║  ██║██║████╗ ██║██╔════╝ 
██║  ╚═╝██║  ██║██║  ██║██║       ██████╔╝██████╔╝██║  ██╗      ██║   ███████║██║██╔██╗██║██║  ██╗ 
██║  ██╗██║  ██║██║  ██║██║       ██╔══██╗██╔═══╝ ██║  ╚██╗     ██║   ██╔══██║██║██║╚████║██║  ╚██╗
╚█████╔╝╚█████╔╝╚█████╔╝███████╗  ██║  ██║██║     ╚██████╔╝     ██║   ██║  ██║██║██║ ╚███║╚██████╔╝
 ╚════╝  ╚════╝  ╚════╝ ╚══════╝  ╚═╝  ╚═╝╚═╝      ╚═════╝      ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚══╝ ╚═════╝ 

"""
)
input("Press enter to start your journey!\n\n\n\n\n")
start_menu()
weapons = [i for i in user_inventory if i in ["Iron Greatsword", "Silver Dagger", "Fist"]]
consumables = [i for i in user_inventory if i in ["Health Potion", "Strength Potion", "Weakness potion"]]
usable_items = [i for i in user_inventory if i in ["Slingshot"]]
artifacts = [i for i in user_inventory if i in ["Archangel's Smite", "Bloody Chalice"]]
spellstones = [i for i in user_inventory if i in ["The Shard of Oblivion", "Ethereal Prism"]]

shown_items = consumables + usable_items + artifacts
while True:
    user_turn()
    if user_hp <= 0:
        if oblivion_active:
            oblivion_shard()
            continue
        else:
            print(
                f"""
██╗   ██╗ █████╗ ██╗   ██╗   ██╗      █████╗  ██████╗████████╗   ████████╗ █████╗   ██╗    {cool_names[npcs[npc_choice]['name']][0]}
╚██╗ ██╔╝██╔══██╗██║   ██║   ██║     ██╔══██╗██╔════╝╚══██╔══╝   ╚══██╔══╝██╔══██╗  ╚═╝    {cool_names[npcs[npc_choice]['name']][1]}
 ╚████╔╝ ██║  ██║██║   ██║   ██║     ██║  ██║╚█████╗    ██║         ██║   ██║  ██║         {cool_names[npcs[npc_choice]['name']][2]}
  ╚██╔╝  ██║  ██║██║   ██║   ██║     ██║  ██║ ╚═══██╗   ██║         ██║   ██║  ██║         {cool_names[npcs[npc_choice]['name']][3]}
   ██║   ╚█████╔╝╚██████╔╝   ███████╗╚█████╔╝██████╔╝   ██║         ██║   ╚█████╔╝  ██╗    {cool_names[npcs[npc_choice]['name']][4]}
   ╚═╝    ╚════╝  ╚═════╝    ╚══════╝ ╚════╝ ╚═════╝    ╚═╝         ╚═╝    ╚════╝   ╚═╝    {cool_names[npcs[npc_choice]['name']][5]}
    """
            )
        break
    if opponent_hp <= 0:
        print(
            f"""

██╗   ██╗ █████╗ ██╗   ██╗  ██████╗ ███████╗ █████╗ ████████╗  ██╗    {cool_names[npcs[npc_choice]['name']][0]}
╚██╗ ██╔╝██╔══██╗██║   ██║  ██╔══██╗██╔════╝██╔══██╗╚══██╔══╝  ╚═╝    {cool_names[npcs[npc_choice]['name']][1]}
 ╚████╔╝ ██║  ██║██║   ██║  ██████╦╝█████╗  ███████║   ██║            {cool_names[npcs[npc_choice]['name']][2]}
  ╚██╔╝  ██║  ██║██║   ██║  ██╔══██╗██╔══╝  ██╔══██║   ██║            {cool_names[npcs[npc_choice]['name']][3]}
   ██║   ╚█████╔╝╚██████╔╝  ██████╦╝███████╗██║  ██║   ██║     ██╗    {cool_names[npcs[npc_choice]['name']][4]}
   ╚═╝    ╚════╝  ╚═════╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝     ╚═╝    {cool_names[npcs[npc_choice]['name']][5]}
"""
        )
        break
    opponent_turn()
    if user_hp <= 0:
        if oblivion_active:
            oblivion_shard()
        else:
            print(
                f"""
██╗   ██╗ █████╗ ██╗   ██╗   ██╗      █████╗  ██████╗████████╗   ████████╗ █████╗   ██╗    {cool_names[npcs[npc_choice]['name']][0]}    
╚██╗ ██╔╝██╔══██╗██║   ██║   ██║     ██╔══██╗██╔════╝╚══██╔══╝   ╚══██╔══╝██╔══██╗  ╚═╝    {cool_names[npcs[npc_choice]['name']][1]}
 ╚████╔╝ ██║  ██║██║   ██║   ██║     ██║  ██║╚█████╗    ██║         ██║   ██║  ██║         {cool_names[npcs[npc_choice]['name']][2]}
  ╚██╔╝  ██║  ██║██║   ██║   ██║     ██║  ██║ ╚═══██╗   ██║         ██║   ██║  ██║         {cool_names[npcs[npc_choice]['name']][3]}
   ██║   ╚█████╔╝╚██████╔╝   ███████╗╚█████╔╝██████╔╝   ██║         ██║   ╚█████╔╝  ██╗    {cool_names[npcs[npc_choice]['name']][4]}
   ╚═╝    ╚════╝  ╚═════╝    ╚══════╝ ╚════╝ ╚═════╝    ╚═╝         ╚═╝    ╚════╝   ╚═╝    {cool_names[npcs[npc_choice]['name']][5]}  
"""
            )
        break
    if opponent_hp <= 0:
        print(
            f"""

██╗   ██╗ █████╗ ██╗   ██╗  ██████╗ ███████╗ █████╗ ████████╗  ██╗    {cool_names[npcs[npc_choice]['name']][0]}
╚██╗ ██╔╝██╔══██╗██║   ██║  ██╔══██╗██╔════╝██╔══██╗╚══██╔══╝  ╚═╝    {cool_names[npcs[npc_choice]['name']][1]}
 ╚████╔╝ ██║  ██║██║   ██║  ██████╦╝█████╗  ███████║   ██║            {cool_names[npcs[npc_choice]['name']][2]}
  ╚██╔╝  ██║  ██║██║   ██║  ██╔══██╗██╔══╝  ██╔══██║   ██║            {cool_names[npcs[npc_choice]['name']][3]}
   ██║   ╚█████╔╝╚██████╔╝  ██████╦╝███████╗██║  ██║   ██║     ██╗    {cool_names[npcs[npc_choice]['name']][4]}
   ╚═╝    ╚════╝  ╚═════╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝     ╚═╝    {cool_names[npcs[npc_choice]['name']][5]}
"""
        )
        break
