import json
from PIL import Image, ImageDraw, ImageFont
import os

################################################

# TODO:
# TKinter window
# Write on image with Pillow

################################################

# Variables

eddies = 2550
skill_points = 86
roles = ["Rockerboy", "Solo", "Netrunner", "Tech", "Medtech", "Media", "Exec", "Lawman", "Fixer", "Nomad"]

# Stats

stats = ["Intelligence", "Reflexes", "Dexterity", "Tech", "Cool", "Will", "Luck", "Move", "Body", "Empathy", "HP", "Humanity"]
intel, ref, dex, tech, cool, will, luck, move, body, emp, hp, hum = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
stats_choice = [intel, ref, dex, tech, cool, will, luck, move, body, emp, hp, hum]
wrong = False
stats_sure = ""
stat_selection_process = True
skill_selection_process = True
shopping_process = True

# Skills

skill_category = ["Awareness [0]", "Body [1]", "Control [2]", "Education [3]", "Fighting [4]", "Performance [5]", "Ranged [6]", "Social [7]", "Technique [8]"]
awareness_skills = ["Concentration (WILL) [0]", "Conceal/Reveal Object (INT) [1]", "Lip Reading (INT) [2]", "Perception (INT) [3]", "Tracking (INT) [4]"]
body_skills = ["Athletics (DEX) [5]", "Contortionist (DEX) [6]", "Dance (DEX) [7]", "Endurance (WILL) [8]", "Reist Torture/Drugs (WILL) [9]", "Stealth (DEX) [10]"]
control_skills = ["Drive Land Vehicle (REF) [11]", "Pilot Air Vehicle x2(REF) [12]", "Pilot Sea Vehicle (REF) [13]", "Riding (REF) [14]"]
education_skills = ["Accounting (INT) [15]", "Animal Handling (INT) [16]", "Bureaucracy (INT) [17]", "Business (INT) [18]", "Composition (INT) [19]", "Criminology (INT) [20]", "Cryptography (INT) [21]", "Deduction (INT) [22]", "Education (INT) [23]", "Gamble (INT) [24]", "Language (INT) [25]", "Library Search (INT) [26]", "Local Expert (INT) [27]", "Science (INT) [28]", "Tactics (INT) [29]", "Wilderness Survival (INT) [30]"]
fight_skills = ["Brawling (DEX) [31]", "Evasion (DEX) [32]", "Marital Arts 2x(DEX) [33]", "Melee Weapon (DEX) [34]"]
performance_skills = ["Acting (COOL) [35]", "Play Instrument (TECH) [36]"]
ranged_weapon_skills = ["Archery (REF) [37]", "Autofire 2x(REF) [38]", "Handgun (REF) [39]", "Heavy Weapons 2x(REF) [40]", "Shoulder Arms (REF) [41]"]
social_skills = ["Bribery (COOL) [42]", "Conversation (EMP) [43]", "Human Perception (EMP) [44]", "Interrogation (COOL) [45]", "Persuasion (COOL) [46]", "Personal Grooming (COOL) [47]", "Streetwise (COOL) [48]", "Trading (COOL) [49]", "Wardrobe & Style (COOL) [50]"]
technique_skills = ["Air Vehicle Tech (TECH) [51]", "Basic Tech (TECH) [52]", "Cybertech (TECH) [53]", "Demolitions 2x(TECH) [54]", "Electronics/Security Tech 2x(TECH) [55]", "First Aid (TECH) [56]", "Land Vehicle Tech (TECH) [57]", "Paint/Sculpt/Draw (TECH) [58]", "Paramedic 2x(TECH) [59]", "Photography/Film (TECH) [60]", "Pick Lock (TECH) [61]", "Pick Pocket (TECH) [62]", "Sea Vehicle Tech (TECH) [63]", "Weapons Tech (TECH) [64]"]

skill_category_pretty = ["Awareness", "Body", "Control", "Education", "Fighting", "Performance", "Ranged", "Social", "Technique"]

prettyall = ["Concentration (WILL)", "Conceal/Reveal Object (INT)", "Lip Reading (INT)", "Perception (INT)", "Tracking (INT)", "Athletics (DEX)", "Contortionist (DEX)", "Dance (DEX)", "Endurance (WILL)", "Reist Torture/Drugs (WILL)", "Stealth (DEX)", "Drive Land Vehicle (REF)", "Pilot Air Vehicle x2(REF)", "Pilot Sea Vehicle (REF)", "Riding (REF)", "Accounting (INT)", "Animal Handling (INT)", "Bureaucracy (INT)", "Business (INT)", "Composition (INT)", "Criminology (INT)", "Cryptography (INT)", "Deduction (INT)", "Education (INT)", "Gamble (INT)", "Language (INT)", "Library Search (INT)", "Local Expert (INT)", "Science (INT)", "Tactics (INT)", "Wilderness Survival (INT)", "Brawling (DEX)", "Evasion (DEX)", "Marital Arts 2x(DEX)", "Melee Weapon (DEX)", "Acting (COOL)", "Play Instrument (TECH)","Archery (REF)", "Autofire 2x(REF)", "Handgun (REF)", "Heavy Weapons 2x(REF)", "Shoulder Arms (REF)", "Bribery (COOL)", "Conversation (EMP)", "Human Perception (EMP)", "Interrogation (COOL)", "Persuasion (COOL)", "Personal Grooming (COOL)", "Streetwise (COOL)", "Trading (COOL)", "Wardrobe & Style (COOL)", "Air Vehicle Tech (TECH)", "Basic Tech (TECH)", "Cybertech (TECH)", "Demolitions 2x(TECH)", "Electronics/Security Tech 2x(TECH)", "First Aid (TECH)", "Land Vehicle Tech (TECH)", "Paint/Sculpt/Draw (TECH)", "Paramedic 2x(TECH)", "Photography/Film (TECH)", "Pick Lock (TECH)", "Pick Pocket (TECH)", "Sea Vehicle Tech (TECH)", "Weapons Tech (TECH)"]

# 0 - 4 // Awareness Array
conc, conceal_reveal, lip_read, perc, track = 2, 0, 0, 2, 0
# 5 - 10 // Body Array
athletics, contort, dance, endurance, resist, stealth = 2, 0, 0, 0, 0, 2
# 11 - 14 // Control Array
drive_land, pilot_air, pilot_sea, riding = 0, 0, 0, 0
# 15 - 30 // Education Array
acc, animal_handling, bureau, business, comp, criminology, cyrptography, deduction, edu, gamble, lang, lib_search, local_exp, sci, tact, wild_surv = 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0 ,0
# 31 - 34 // Fighting Array
brawl, evasion, marital_arts, melee_weapon = 2, 2, 0, 0
# 35 - 36 // Performance Array
acting, playinstrument = 0, 0
# 37 - 41 // Ranged Array
archery, autofire, handgun, heavy_weapons, shoulder_arms = 0, 0, 0, 0, 0
# 42 - 50 // Social Array
bribe, convo, human_perc, interog, pers, personal_grooming, streetwise, trading, ward_n_style = 0, 2, 2, 0, 2, 0, 0, 0, 0
# 51 - 64 // Technique Array
air_vehicle, basic, cyber, demo, electronics_security, first_aid, land_vehicle, paintsculptdraw, para, photo_film, pick_lock, pick_pocket, sea_vehicle, weapons = 0, 0, 0, 0, 0, 2, 0 ,0 ,0 ,0, 0, 0, 0, 0

# skill vars

skills_all = [conc, conceal_reveal, lip_read, perc, track, athletics, contort, dance, endurance, resist, stealth, drive_land, pilot_air, pilot_sea, riding, acc, animal_handling, bureau, business, comp, criminology, cyrptography, deduction, edu, gamble, lang, lib_search, local_exp, sci, tact, wild_surv, brawl, evasion, marital_arts, melee_weapon, acting, playinstrument, archery, autofire, handgun, heavy_weapons, shoulder_arms, bribe, convo, human_perc, interog, pers, personal_grooming, streetwise, trading, ward_n_style, air_vehicle, basic, cyber, demo, electronics_security, first_aid, land_vehicle, paintsculptdraw, para, photo_film, pick_lock, pick_pocket, sea_vehicle, weapons]

all_categories = [awareness_skills, body_skills, control_skills, education_skills, fight_skills, performance_skills, ranged_weapon_skills, social_skills, technique_skills]

# array lengths

length_awareness = len(awareness_skills)
length_body = len(body_skills)
length_control = len(control_skills)
length_education = len(education_skills)
length_fight = len(fight_skills)
length_performance = len(performance_skills)
lenght_ranged = len(ranged_weapon_skills)
lenght_social = len(social_skills)
lenght_techniques = len(technique_skills)

# prices

cheap, everyday, costly, premium, expensive, v_expensive = 10, 20, 50, 100, 500, 1000
inventory, weapon_inventory, armor_inventory, programs = [], [], [], []

# images

image_first_page = Image.open("assets/1-1.png")
image_second_page = Image.open("assets/1-2.png")
image_third_page = Image.open("assets/1-3.png")

################################################

# functions

################################################

# Stat point assignment

def statchoice():
    # Global and Local variables
    stat_points = 62
    global wrong,stats_choice, intel, ref, dex, tech, cool, will, luck, move, body, emp
    stats_choice = [intel, ref, dex, tech, cool, will, luck, move, body, emp]
    wrong = False
    global stats_sure

    for j in range(10):
        print("Remaining points: ", stat_points)
        print("Input how many points you want to put (min 2, max 8) in", stats[j])
        stats_choice[j] = int(input("Points: "))
        if stats_choice[j] > 8 or stats_choice[j] < 2:
           print("Invalid input")
           wrong = True

        while wrong:
            print("Input how many points you want to put (min 2, max 8) in", stats[j])
            stats_choice[j] = int(input("Points: "))
            if stats_choice[j] > 8 or (stats_choice[j] < 2):
                print("Invalid input")
            else:
                wrong = False
        stat_points -= stats_choice[j]

def skillselection():
    global skill_category
    global awareness_skills, body_skills, control_skills, education_skills, fight_skills, performance_skills, ranged_weapon_skills, social_skills, technique_skills
    global conc, conceal_reveal, lip_read, perc, track, athletics, contort, dance, endurance, resist, stealth, drive_land, pilot_air, pilot_sea, riding, acc, animal_handling, bureau, business, comp, criminology, cyrptography, deduction, edu, gamble, lang, lib_search, local_exp, sci, tact, wild_surv, brawl, evasion, marital_arts, melee_weapon, acting, playinstrument, archery, autofire, handgun, heavy_weapons, shoulder_arms, bribe, convo, human_perc, interog, pers, personal_grooming, streetwise, trading, ward_n_style, air_vehicle, basic, cyber, demo, electronics_security, first_aid, land_vehicle, paintsculptdraw, para, photo_film, pick_lock, pick_pocket, sea_vehicle, weapons
    global skills_all
    global skill_points
    skill_points = 64
    global wrong
    choice_done = False

    print("Automatically assigned 2 points to: ", awareness_skills[0], awareness_skills[3], body_skills[0], body_skills[5], education_skills[8], fight_skills[0], fight_skills[1], social_skills[1], social_skills[2], social_skills[4], technique_skills[5])

    while not choice_done:
        print("Remaining points: ", skill_points)
        print("Categories: ", skill_category)
        category_choice = int(input("Choose a category: "))

        print("Chosen Category: ", skill_category[category_choice])
        print("Available Skills: ", all_categories[category_choice])
        skill_choice = int(input("Choose a Skill: "))
        add_points = int(input("Add points (min 2 max 6): "))

        if add_points < 2 or add_points > 6 or skills_all[0] > 6 or skills_all[3] > 6 or skills_all[5] > 6 or skills_all[10] > 6 or skills_all[23] > 6 or skills_all[25] > 6 or skills_all[26] > 6 or skills_all[35] > 6 or skills_all[36] > 6 or skills_all[38] > 6 or skills_all[48] > 6:
            print("Invalid input")
            wrong = True
        while wrong:
            add_points = int(input("Add points (min 2 max 6): "))
            if add_points < 2 or add_points > 6:
                print("Invalid input")
            else:
                wrong = False
        skill_points -= add_points
        skills_all[skill_choice] = add_points

        confirm = input("Confirm Skills? (Enter no if you're not done) (Y/N): ")
        if confirm == "Y" or confirm == "y":
            if skill_points != 0:
                print("Please allocate all your skill points.")
                skill_points = 64
                choice_done = False
            else:
                choice_done = True
        elif confirm == "N" or confirm == "n":
            choice_done = False

def gear_selection():
    global inventory, weapon_inventory, armor_inventory, programs
    global cheap, everyday, costly, premium, expensive, v_expensive
    global eddies
    shopping_gear = True
    shopping_weapons = True
    shopping_armor = True
    shopping_clothes = True
    shopping_programs = True

    while shopping_gear:
        print("+-------------------------------------+------------------------+\n|                Item                 |          Cost          |\n+-------------------------------------+------------------------+\n| Agent                               | 100eb (Premium)        |\n| Airhypo                             | 50eb (Costly)          |\n| Anti-Smog Breathing Mask            | 20eb (Everyday)        |\n| Audio Recorder                      | 100eb (Premium)        |\n| Auto Level Dampening Ear Protectors | 1,000eb (V. Expensive) |\n| Binoculars                          | 50eb (Costly)          |\n| Braindance Viewer                   | 1,000eb (V. Expensive) |\n| Bug Detector                        | 500eb (Expensive)      |\n| Carryall                            | 20eb (Everyday)        |\n| Chemical Analyzer                   | 1,000eb (V. Expensive) |\n| Computer                            | 50eb (Costly)          |\n| Cyberdeck                           | 500eb (Expensive)      |\n| Disposable Cell Phone               | 50eb (Costly)          |\n| Drum Synthesizer                    | 500eb (Expensive)      |\n| Duct Tape                           | 20eb (Everyday)        |\n| Electric Guitar/Other Instrument    | 500eb (Expensive)      |\n| Flashlight                          | 20eb (Everyday)        |\n| Food Stick                          | 10eb (Cheap)           |\n| Glow Paint                          | 20eb (Everyday)        |\n+-------------------------------------+------------------------+")
        print("+------------------------------------------+------------------------+\n|                   Item                   |          Cost          |\n+------------------------------------------+------------------------+\n| Glow Stick                               | 10eb (Cheap)           |\n| Grapple Gun                              | 100eb (Premium)        |\n| Handcuffs                                | 50eb (Costly)          |\n| Homing Tracer                            | 500eb (Expensive)      |\n| Inflatable Bed & Sleep-bag               | 20eb (Everyday)        |\n| Kibble Pack                              | 10eb (Cheap)           |\n| Lock Picking Set                         | 20eb (Everyday)        |\n| Medscanner                               | 1,000eb (V. Expensive) |\n| Medtech Bag                              | 100eb (Premium)        |\n| Memory Chip                              | 10eb (Cheap)           |\n| MRE                                      | 10eb (Cheap)           |\n| Personal CarePak                         | 20eb (Everyday)        |\n| Pocket Amplifier                         | 50eb (Costly)          |\n| Radar Detector                           | 500eb (Expensive)      |\n| Radiation Suit                           | 1,000eb (V. Expensive) |\n| Radio Communicator                       | 100eb (Premium)        |\n| Radio Scanner/Music Player               | 50eb (Costly)          |\n| Road Flare                               | 10b (Cheap)            |\n| Rope (60m/yd)                            | 20eb (Everyday)        |\n| Scrambler/Descrambler                    | 500eb (Expensive)      |\n| Smart Glasses                            | 500eb (Expensive)      |\n| Tech Bag                                 | 500eb (Expensive)      |\n| Techscanner                              | 1,000eb (V. Expensive) |\n| Techtool                                 | 100eb (Premium)        |\n| Tent and Camping Equipment               | 50eb (Costly)          |\n| Vial of Biotoxin                         | 500eb (Expensive)      |\n| Vial of Poison                           | 100eb (Premium)        |\n| Video Camera                             | 100eb (Premium)        |\n| Virtuality Goggles                       | 100eb (Premium)        |\n+------------------------------------------+------------------------+")

        print("Balance: ", eddies)
        choice = input("Choose an item (write the item name EXACTLY as it appears on the table): ")

        if choice.title() == "Agent" or choice.title() == "Audio Recorder" or choice.title() == "Grapple Gun" or choice.title() == "Medtech Bag" or choice.title() == "Radio Communicator" or choice.title() == "Vial of Poison" or choice.title() == "Video Camera" or choice.title() == "Vial of Biotoxin" or choice.title() == "Virtuality Goggles" or choice.title() == "Techtool":
            if eddies >= premium:
                eddies -= premium
                inventory.append(choice.title())
                print("Item added successfully!")
            else:
                print("You don't have enough eddies choom!")
        elif choice.title() == "Anti-Smog Breathing Mask" or choice.title() == "Carryall" or choice.title() == "Duct Tape" or choice.title() == "Flashlight" or choice.title() == "Glow Paint" or choice.title() == "Inflatable Bed & Sleep-bag" or choice.title() == "Lock Picking Set" or choice.title() == "Personal CarePak" or choice.title() == "Rope (60m/yd)":
            if eddies >= everyday:
                eddies -= everyday
                inventory.append(choice.title())
                print("Item added successfully!")
            else:
                print("You don't have enough eddies choom!")
        elif choice.title() == "Airhypo" or choice.title() == "Binoculars" or choice.title() == "Disposable Cell Phone" or choice.title() == "Computer" or choice.title() == "Handcuffs" or choice.title() == "Pocket Amplifier" or choice.title() == "Radio Scanner/Music Player" or choice.title() == "Tent and Camping Equipment":
            if eddies >= costly:
                eddies -= costly
                inventory.append(choice.title())
                print("Item added successfully!")
            else:
                print("You don't have enough eddies choom!")
        elif choice.title() == "Food Stick" or choice.title() == "Kibble Pack" or choice.title() == "Memory Chip" or choice.title() == "MRE" or choice.title() == "Road Flare":
            if eddies >= cheap:
                eddies -= cheap
                inventory.append(choice.title())
                print("Item added successfully!")
            else:
                print("You don't have enough eddies choom!")
        elif choice.title() == "Smart Glasses" or choice.title() == "Tech Bag" or choice.title() == "Bug Detector" or choice.title() == "Scrambler/Descrambler" or choice.title() == "Radar Detector" or choice.title() == "Electric Guitar/Other Instrument" or choice.title() == "Cyberdeck" or choice.title() == "Homing Tracer" or choice.title() == "Drum Synthesizer":
            if eddies >= expensive:
                eddies -= expensive
                inventory.append(choice.title())
                print("Item added successfully!")
            else:
                print("You don't have enough eddies choom!")
        elif choice.title() == "Techscanner" or choice.title() == "Radiation Suit" or choice.title() == "Medscanner" or choice.title() == "Auto Level Dampening Ear Protectors" or choice.title() == "Braindance Viewer" or choice.title() == "Chemical Analyzer":
            if eddies >= v_expensive:
                eddies -= v_expensive
                inventory.append(choice.title())
                print("Item added successfully!")
            else:
                print("You don't have enough eddies choom!")
        else:
            print("Invalid choice")

        end_shopping = input("Would you like to finish shopping GEAR? (Y/N): ")

        if end_shopping == "Y" or end_shopping == "Yes" or end_shopping == "yes" or end_shopping == "y":
            shopping_gear = False
            print("Inventory:", inventory)
        else:
            shopping_gear = True

    while shopping_weapons:
        print("+-------------------------+-----------------------------------------------------+---------------------+--------+------+-------------------+-------------------+\n|    Melee Weapon Type    |                Example Melee Weapons                | # of Hands Required | Damage |  ROF | Can be Concealed? |       Cost        |\n+-------------------------+-----------------------------------------------------+---------------------+--------+------+-------------------+-------------------+\n| Light Melee Weapon      | Combat Knife, Tomahawk                              | Varies by type      | 1d6    |    2 | YES               | 50eb (Costly)     |\n| Medium Melee Weapon     | Baseball Bat, Crowbar, Machete                      | Varies by type      | 2d6    |    2 | NO                | 50eb(Costly)      |\n| Heavy Melee Weapon      | Lead Pipe, Sword, Spiked Bat                        | Varies by type      | 3d6    |    2 | NO                | 100eb (Premium)   |\n| Very Heavy Melee Weapon | Chainsaw, Sledgehammer, Helicopter Blades, Naginata | Varies by type      | 4d6    |    1 | NO                | 500eb (Expensive) |\n+-------------------------+-----------------------------------------------------+---------------------+--------+------+-------------------+-------------------+")

        print("+-------------------+----------------+--------------------+-------------------+-------------------+----------------+-------------------+------------------+\n|    Weapon Type    |  Weapon Skill  | Single Shot Damage | Standard Magazine | Rate of Fire(ROF) | Hands Required | Can be Concealed? |       Cost       |\n+-------------------+----------------+--------------------+-------------------+-------------------+----------------+-------------------+------------------+\n| Medium Pistol     | Handgun        | 2d6                | 12(M Pistol)      |                2  |             1  | YES               | 50eb (Costly)    |\n| Heavy Pistol      | Handgun        | 3d6                | 8(H Pistol)       |                2  |             1  | YES               | 100eb(Premium)   |\n| Very Heavy Pistol | Handgun        | 4d6                | 8(VH Pistol)      |                1  |             1  | NO                | 100eb(Premium)   |\n| SMG               | Handgun        | 2d6                | 30(M Pistol)      |                1  |             1  | YES               | 100eb(Premium)   |\n| Heavy SMG         | Handgun        | 3d6                | 40(H Pistol)      |                1  |             1  | NO                | 100eb(Premium)   |\n| Shotgun           | Shoulder Arms  | 5d6                | 4(Slug)           |                1  |             2  | NO                | 500eb(Expensive) |\n| Assault Rifle     | Shoulder Arms  | 5d6                | 25(Rifle)         |                1  |             2  | NO                | 500eb(Expensive) |\n| Sniper Rifle      | Shoulder Arms  | 5d6                | 4(Rifle)          |                1  |             2  | NO                | 500eb(Expensive) |\n| Bows & Crossbows  | Archery        | 4d6                | N/A(Arrow)        |                1  |             2  | NO                | 100eb(Premium)   |\n| Grenade Launcher  | Heavy Weapons  | 6d6                | 2(Grenade)        |                1  |             2  | NO                | 500eb(Expensive) |\n| Rocket Launcher   | Heavy Weapons  | 8d6                | 1(Rocket)         |                1  |             2  | NO                | 500eb(Expensive) |\n+-------------------+----------------+--------------------+-------------------+-------------------+----------------+-------------------+------------------+")

        print("+--------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+\n|                   Weapon                   |                                                             Description and Data                                                             |          Cost           |\n+--------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+\n| Air Pistol                                 | Very Heavy Pistol that fires paint (and acid!) balls.                                                                                        | 100eb (Premium)         |\n| Battleglove                                | Heavy gauntlet. Contains three Cyberarm/Cyberlimb option slots.                                                                              | 1,000eb (V. Expensive)  |\n| Constitution Arms Hurricane Assault Weapon | Shotgun w/ 2 ROF. Requires BODY 11+ to fire.                                                                                                 | 5,000eb (Luxury)        |\n| Dartgun                                    | Very Heavy Pistol that fires Non-Basic Arrows.                                                                                               | 100eb (Premium)         |\n| Flamethrower                               | Shotgun that fires incendiary shells. Fired with the Heavy Weapons Skill.                                                                    | 500eb (Expensive)       |\n| Kendachi                                   | Mono-Three Two-Handed Very Heavy Melee Weapon. Ignores armor lower than SP11                                                                 | 5,000eb (Luxury)        |\n| Malorian Arms 3516                         | Excellent Quality Very Heavy Pistol famously wielded by Johnny Silverhand. Does 5d6 damage.                                                  | 10,000eb (Super Luxury) |\n| Microwaver                                 | Very Heavy Pistol that can shut down cyberware and carried electronics.                                                                      | 500eb (Expensive)       |\n| Militech 'Cowboy' U-56 Grenade Launcher    | Grenade Launcher w/ 2 ROF. Requires BODY 11+ to fire.                                                                                        | 5,000eb (Luxury)        |\n| Rhinemetall EMG-86 Railgun                 | Assault Rifle that ignore armor lower than SP 11. Fired with the Heavy Weapons Skill. Requires BODY 11+ to fire.                             | 5,000eb (Luxury)        |\n| Shrieker                                   | Very Heavy Pistol that causes the Damaged Ear Critical Injury.                                                                               | 500eb (Expensive)       |\n| Stun Baton                                 | A 'less lethal' Medium Melee Weapon.                                                                                                         | 100eb (Premium)         |\n| Stun Gun                                   | A 'less lethal' Heavy Pistol.                                                                                                                | 100eb (Premium)         |\n| Tsunami Arms Helix                         | Assault Rifle that only fires in Autofire mode (with a higher Autofire multiplier than a standard Assault Rifle). Requires BODY 11+ to fire. | 5,000eb (Luxury)        |\n+--------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+-------------------------+")

        print("Balance: ", eddies)
        choice = input("Choose a weapon (use weapon type if melee): ")

        if choice.title() == "Heavy Pistol" or choice.title() == "Very Heavy Pistol" or choice.upper() == "SMG" or choice.title() == "Heavy SMG" or choice.title() == "Bow" or choice.title() == "Crossbow" or choice.title() == "Air Pistol" or choice.title() == "Dartgun" or choice.title() == "Stun Gun" or choice.title() == "Stun Baton":
            if eddies >= premium:
                eddies -= premium
                weapon_inventory.append(choice.title())
                print("Item added successfully!")
            else:
                print("You don't have enough eddies choom!")
        elif choice.title() == "Light Melee Weapon" or choice == "Medium Melee Weapon" or choice.title() == "Medium Pistol":
            if eddies >= costly:
                eddies -= costly
                weapon_inventory.append(choice.title())
                print("Item added successfully!")
            else:
                print("You don't have enough eddies choom!")
        elif choice.title() == "Shotgun" or choice.title() == "Assault Rifle" or choice.title() == "Sniper Rifle" or choice.title() == "Grenade Launcher" or choice.title() == "Rocket Launcher" or choice.title() == "Flamethrower" or choice.title() == "Microwaver" or choice.title() == "Shrieker":
            if eddies >= expensive:
                eddies -= expensive
                weapon_inventory.append(choice.title())
                print("Item added successfully!")
            else:
                print("You don't have enough eddies choom!")
        elif choice.title() == "Constitution Arms Hurricane Assault Weapon" or choice.title() == "Kendachi" or choice.title() == "Militech 'Cowboy' U-56 Grenade Launcher" or choice.title() == "Rhinemetall EMG-86 Railgun" or choice.title() == "Tsunami Arms Helix":
            if eddies >= v_expensive*5:
                eddies -= v_expensive*5
                weapon_inventory.append(choice.title())
                print("Item added successfully!")
            else:
                print("You don't have enough eddies choom!")
        elif choice.title() == "Malorian Arms 516":
            if eddies >= v_expensive*10:
                eddies -= v_expensive*10
                weapon_inventory.append(choice.title())
                print("Item added successfully, rockerboy")
            else:
                print("You don't have enough eddies choom!")
        else:
            print("Invalid choice")

        end_shopping = input("Would you like to finish shopping WEAPONS? (Y/N): ")

        if end_shopping == "Y" or end_shopping == "Yes" or end_shopping == "yes" or end_shopping == "y":
            shopping_weapons = False
            print("Inventory:", weapon_inventory)
        else:
            shopping_weapons = True

    while shopping_armor:
        print("+--------------------+----------------------------------+-----------------------------------+------------------+\n|    Armor Type      |    Damage Stopping Power (SP)    |     Armor Penalty(Minimum 0)      |       Cost       |\n+--------------------+----------------------------------+-----------------------------------+------------------+\n| Leathers           | 4                                | None                              | 20eb(Everyday)   |\n| Light Armorjack    | 11                               | None                              | 50eb(Costly)     |\n| Bodyweight Suit    | 11                               | None                              | 100eb(Premium)   |\n| Medium Armorjack   | 12                               | -2 REF, DEX, and MOVE             | 100eb(Premium)   |\n| Heavy Armorjack    | 13                               | -2 REF, DEX, and MOVE             | 500eb(Expensive) |\n| Flak               | 15                               | -4 REF, DEX, and MOVE             | 500eb(Expensive) |\n| Metalgear®         | 18                               | -4 REF, DEX, and MOVE             | 5,000eb(Luxury)  |\n| Bulletproof Shield | 10 HP, which isreduced by damage | None, but always takes up one arm | 100eb(Premium)   |\n+--------------------+----------------------------------+-----------------------------------+------------------+")

        print("Balance: ", eddies)
        choice = input("Choose an armor: ")

        if choice.title() == "Leathers":
            if eddies >= everyday:
                eddies -= everyday
                armor_inventory.append(choice.title())
                print("Item added successfully!")
            else:
                print("You don't have enough eddies choom!")
        elif choice.title() == "Light Armorjack":
            if eddies >= costly:
                eddies -= costly
                armor_inventory.append(choice.title())
                print("Item added successfully!")
            else:
                print("You don't have enough eddies choom!")
        elif choice.title() == "Bodyweight Suit" or choice.title() == "Medium Armorjack" or choice.title() == "Bulletproof Shield":
            if eddies >= premium:
                eddies -= premium
                armor_inventory.append(choice.title())
                print("Item added successfully!")
            else:
                print("You don't have enough eddies choom!")
        elif choice.title() == "Heavy Armorjack" or choice.title() == "Flak":
            if eddies >= expensive:
                eddies -= expensive
                armor_inventory.append(choice.title())
                print("Item added successfully!")
            else:
                print("You don't have enough eddies choom!")
        elif choice.title() == "Metalgear":
            if eddies >= v_expensive*5:
                eddies -= v_expensive*5
                armor_inventory.append(choice.title())
                print("Item added successfully!")
            else:
                print("You don't have enough eddies choom!")
        else:
            print("Invalid choice")

        end_shopping = input("Would you like to finish shopping WEAPONS? (Y/N): ")

        if end_shopping == "Y" or end_shopping == "Yes" or end_shopping == "yes" or end_shopping == "y":
            shopping_armor = False
            print("Inventory:", armor_inventory)
        else:
            shopping_armor = True

    if role_choice == 3:
        while shopping_programs:
            print("Insert programs here, I ain't coding them rn")

role_choice = int(input("Choose your role [Rockerboy(1), Solo(2), Netrunner(3), Tech(4), Medtech(5), Media(6), Exec(7), Lawman(8), Fixer(9), Nomad(10)]: "))
role_choice = roles[role_choice-1]
print("Your role is:", role_choice)

role_sure = input("Are you sure? (y/n): ")

if role_sure == 'n' or role_sure == 'N' or role_sure == 'no' or role_sure == 'No':
    wrong = True
    while wrong:
        role_choice = int(input("Choose your role [Rockerboy(1), Solo(2), Netrunner(3), Tech(4), Medtech(5), Media(6), Exec(7), Lawman(8), Fixer(9), Nomad(10)]: "))
        role_choice = roles[role_choice - 1]
        print("Your role is:", role_choice)

        role_sure = input("Are you sure? (y/n): ")
        if role_sure == 'y' or role_sure == 'Y' or role_sure == 'yes' or role_sure == 'Yes':
            wrong = False

while stat_selection_process:
    statchoice()
    avg = (stats_choice[8] + stats_choice[5]) / 2
    hp = 10 + 5 * avg
    hum = stats_choice[9] * 10

    print("STATS:\nINT: ", stats_choice[0], "REF: ", stats_choice[1], "DEX: ", stats_choice[2], "TECH: ",
          stats_choice[3], "COOL: ", stats_choice[4], "\nWILL: ", stats_choice[5], "LUCK: ", stats_choice[6], "MOVE: ",
          stats_choice[7], "BODY: ", stats_choice[8], "EMP: ", stats_choice[9], "\n\nHUMANITY: ", hum, "HITPOINTS: ",
          hp)
    stats_sure = input("Are you sure? (y/n): ")


    if stats_sure == 'n' or stats_sure == 'N' or stats_sure == 'no' or stats_sure == 'No':
        wrong = True
        while wrong:
            statchoice()
            avg = (stats_choice[8] + stats_choice[5]) / 2
            hp = 10 + 5 * avg
            hum = stats_choice[9] * 10

            print("STATS:\nINT: ", stats_choice[0], "REF: ", stats_choice[1], "DEX: ", stats_choice[2], "TECH: ",
                  stats_choice[3], "COOL: ", stats_choice[4], "\nWILL: ", stats_choice[5], "LUCK: ", stats_choice[6],
                  "MOVE: ", stats_choice[7], "BODY: ", stats_choice[8], "EMP: ", stats_choice[9], "\n\nHUMANITY: ", hum,
                  "HITPOINTS: ", hp)
            stats_sure = input("Are you sure? (y/n): ")
            if stats_sure == 'y' or stats_sure == 'Y' or stats_sure == 'yes' or stats_sure == 'Yes':
                wrong = False
                stat_selection_process = False
    if stats_sure == 'y' or stats_sure == 'Y' or stats_sure == 'yes' or stats_sure == 'Yes':
        stat_selection_process = False


while skill_selection_process:
    skillselection()
    skills_sure = input("Are you sure about your skills? (y/n): ")

    # base calculations

    bconc, bconceal, blip, bperc, btrack = stats_choice[5] + skills_all[0], stats_choice[0] + skills_all[1], stats_choice[0] + skills_all[2], stats_choice[0] + skills_all[3], stats_choice[0] + skills_all[4]

    bathletics, bcontort, bdance, bendurance, bresist, bstealth = stats_choice[2] + skills_all[5], stats_choice[2] + skills_all[6], stats_choice[2] + skills_all[7], stats_choice[5] + skills_all[8], stats_choice[5] + skills_all[9], stats_choice[2] + skills_all[10]

    bdrive_land, bpilot_air, bpilot_sea, briding = stats_choice[1] + skills_all[11], stats_choice[1] + skills_all[12], stats_choice[1] + skills_all[13], stats_choice[1] + skills_all[14]

    bacc, banimal_handling, bbureau, bbusiness, bcomp, bassecriminology, bcyrptography, bdeduction, bedu, bgamble, blang, blib_search, blocal_exp, bsci, btact, bwild_surv = stats_choice[0] + skills_all[14], stats_choice[0] + skills_all[15], stats_choice[0] + skills_all[16], stats_choice[0] + skills_all[17], stats_choice[0] + skills_all[18], stats_choice[0] + skills_all[19], stats_choice[0] + skills_all[20], stats_choice[0] + skills_all[21], stats_choice[0] + skills_all[22], stats_choice[0] + skills_all[23], stats_choice[0] + skills_all[24], stats_choice[0] + skills_all[25], stats_choice[0] + skills_all[26], stats_choice[0] + skills_all[27], stats_choice[0] + skills_all[28], stats_choice[0] + skills_all[29]

    bbrawl, bevasion, bmarital_arts, bmelee_weapon = stats_choice[2] + skills_all[30], stats_choice[2] + skills_all[31], stats_choice[2] + skills_all[32], stats_choice[2] + skills_all[33]

    bacting, bplayinstrument = stats_choice[4] + skills_all[34], stats_choice[3] + skills_all[35]

    barchery, bautofire, bhandgun, bheavy_weapons, bshoulder_arms = stats_choice[1] + skills_all[36], stats_choice[1] + skills_all[37], stats_choice[1] + skills_all[38], stats_choice[1] + skills_all[39], stats_choice[1] + skills_all[40]

    bbribe, bconvo, bhuman_perc, binterog, bpers, bpersonal_grooming, bstreetwise, btrading, bward_n_style = stats_choice[4] + skills_all[41], stats_choice[9] + skills_all[42], stats_choice[9] + skills_all[43], stats_choice[4] + skills_all[44], stats_choice[4] + skills_all[45], stats_choice[4] + skills_all[46], stats_choice[4] + skills_all[47], stats_choice[4] + skills_all[48], stats_choice[4] + skills_all[49]

    bair_vehicle, bbasic, bcyber, bdemo, belectronics_security, bfirst_aid, bland_vehicle, bpaintsculptdraw, bpara, bphoto_film, bpick_lock, bpick_pocket, bsea_vehicle, bweapons = stats_choice[3] + skills_all[50], stats_choice[3] + skills_all[51], stats_choice[3] + skills_all[52], stats_choice[3] + skills_all[53], stats_choice[3] + skills_all[54], stats_choice[3] + skills_all[55], stats_choice[3] + skills_all[56], stats_choice[3] + skills_all[57], stats_choice[3] + skills_all[58], stats_choice[3] + skills_all[59], stats_choice[3] + skills_all[60], stats_choice[3] + skills_all[61], stats_choice[3] + skills_all[62], stats_choice[3] + skills_all[63]

    basecalc = [bconc, bconceal, blip, bperc, btrack, bathletics, bcontort, bdance, bendurance, bresist, bstealth,
                bdrive_land, bpilot_air, bpilot_sea, briding, bacc, banimal_handling, bbureau, bbusiness, bcomp,
                bassecriminology, bcyrptography, bdeduction, bedu, bgamble, blang, blib_search, blocal_exp, bsci, btact,
                bwild_surv, bbrawl, bevasion, bmarital_arts, bmelee_weapon, bacting, bplayinstrument, barchery,
                bautofire, bhandgun, bheavy_weapons, bshoulder_arms, bbribe, bconvo, bhuman_perc, binterog, bpers,
                bpersonal_grooming, bstreetwise, btrading, bward_n_style, bair_vehicle, bbasic, bcyber, bdemo,
                belectronics_security, bfirst_aid, bland_vehicle, bpaintsculptdraw, bpara, bphoto_film, bpick_lock,
                bpick_pocket, bsea_vehicle, bweapons]

    if skills_sure == 'n' or skills_sure == 'N' or skills_sure == 'no' or skills_sure == 'No':
        wrong = True
        while wrong:
            skillselection()
            skills_sure = input("Are you sure? (y/n): ")
            if skills_sure == 'y' or skills_sure == 'Y' or skills_sure == 'yes' or skills_sure == 'Yes':
                wrong = False
                skill_selection_process = False
                print("SKILLS:\n")
                for i in range(len(skills_all)):
                    print(prettyall[i], "\nLEVEL:", skills_all[i], "BASE:", basecalc[i], "\n")

                print("STATS:\nINT: ", stats_choice[0], "REF: ", stats_choice[1], "DEX: ", stats_choice[2], "TECH: ",
                      stats_choice[3], "COOL: ", stats_choice[4], "\nWILL: ", stats_choice[5], "LUCK: ",
                      stats_choice[6],
                      "MOVE: ", stats_choice[7], "BODY: ", stats_choice[8], "EMP: ", stats_choice[9], "\n\nHUMANITY: ", hum,
                      "HITPOINTS: ", hp)

    if skills_sure == 'y' or skills_sure == 'Y' or skills_sure == 'yes' or skills_sure == 'Yes':
        skill_selection_process = False
        print("SKILLS:\n")
        for i in range(len(skills_all)):
            print(prettyall[i], "\nLEVEL:", skills_all[i], "BASE:" , basecalc[i], "\n")

        print("STATS:\nINT: ", stats_choice[0], "REF: ", stats_choice[1], "DEX: ", stats_choice[2], "TECH: ",
              stats_choice[3], "COOL: ", stats_choice[4], "\nWILL: ", stats_choice[5], "LUCK: ", stats_choice[6],
              "MOVE: ", stats_choice[7], "BODY: ", stats_choice[8], "EMP: ", stats_choice[9], "\n\nHUMANITY: ", hum,
              "HITPOINTS: ", hp)

gear_selection()

# This part of the code basically puts all the skills in a JSON file to be read later

data = {
            "STATS": dict(zip(stats, stats_choice)),
            "SKILLS:": skill_category_pretty,
            "First number is the level, second one is the Base":"Base is calculated as STAT+LEVEL",
            skill_category_pretty[0]: dict(zip(prettyall[0:5], zip(skills_all[0:5],  basecalc[0:5]))),
            skill_category_pretty[1]: dict(zip(prettyall[6:10], zip(skills_all[6:10], basecalc[6:10]))),
            skill_category_pretty[2]: dict(zip(prettyall[11:14], zip(skills_all[11:14], basecalc[11:14]))),
            skill_category_pretty[3]: dict(zip(prettyall[15:30], zip(skills_all[15:30], basecalc[15:30]))),
            skill_category_pretty[4]: dict(zip(prettyall[31:34], zip(skills_all[31:34], basecalc[31:34]))),
            skill_category_pretty[5]: dict(zip(prettyall[35:36], zip(skills_all[35:36], basecalc[35:36]))),
            skill_category_pretty[6]: dict(zip(prettyall[37:41], zip(skills_all[37:41], basecalc[37:41]))),
            skill_category_pretty[7]: dict(zip(prettyall[42:50], zip(skills_all[42:50], basecalc[42:50]))),
            skill_category_pretty[8]: dict(zip(prettyall[51:64], zip(skills_all[51:64], basecalc[51:64]))),
            "GEAR": inventory,
            "WEAPONS": weapon_inventory,
            "ARMOR": armor_inventory,
        }

# Create and write/Overwrite stat.json file

with open("stats.json", "w") as f:
    json.dump(data, f, indent=4)


# Image writing and generation

draw = ImageDraw.Draw(image_first_page)
position_y = 196
position_stats = (625, position_y)
position_y_skills = 205
position_stats_skills = (1094, position_y_skills)

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
draw.text((176,648), role_choice, font=font, fill=(0,0,0))

for i in range(10):
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
    position_y += 120 - i
    position_stats = (625, position_y)

    if i == 0:
        position_y = 196
        position_stats = (625, position_y)

    if i == 6 or i == 9:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
        position_y += 20
        position_stats = (670, position_y)

    draw.text(position_stats, str(stats_choice[i]), font=font, fill=(0,0,0))

for i in range(11):
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
    position_y_skills += 39
    position_stats_skills = (1094, position_y_skills)

    if i == 0:
        position_y_skills = 205
        position_stats_skills = (1094, position_y_skills)

    if i == 5:
        position_y_skills += 46
        position_stats_skills = (1094, position_y_skills)

    if i < 10:
        draw.text(position_stats_skills, str(stats_choice[i]), font=font, fill=(0, 0, 0))
    else:
        draw.text(position_stats_skills, str(stats_choice[i-1]), font=font, fill=(0, 0, 0))

image_first_page.show()