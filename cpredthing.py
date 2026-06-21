import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageDraw, ImageFont

################################################

# TODO:
# TKinter window
# Write on image with Pillow - Done

################################################

# TKinter
root = tk.Tk()


tk.Label(root, text="Cyberpunk RED Character Sheet Maker - by DrSkillful").grid(row=0, column=3)

# Variables

eddies = 2550
skill_points = 86

# Stats

stats = ["Intelligence", "Reflexes", "Dexterity", "Tech", "Cool", "Will", "Luck", "Move", "Body", "Empathy", "HP", "Humanity"]
statEntry = []
skillEntry = []
weapons = []
armors = []
purchase_gear = []
intel, ref, dex, tech, cool, will, luck, move, body, emp, hp, hum = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
stats_choice = [intel, ref, dex, tech, cool, will, luck, move, body, emp, hp, hum]
charname = ""
role_choice = ""
part = 0

skill_category_pretty = ["Awareness", "Body", "Control", "Education", "Fighting", "Performance", "Ranged", "Social", "Technique"]

prettyall = ["Concentration (WILL)", "Conceal/Reveal Object (INT)", "Lip Reading (INT)", "Perception (INT)", "Tracking (INT)", "Athletics (DEX)", "Contortionist (DEX)", "Dance (DEX)", "Endurance (WILL)", "Reist Torture/Drugs (WILL)", "Stealth (DEX)", "Drive Land Vehicle (REF)", "Pilot Air Vehicle x2(REF)", "Pilot Sea Vehicle (REF)", "Riding (REF)", "Accounting (INT)", "Animal Handling (INT)", "Bureaucracy (INT)", "Business (INT)", "Composition (INT)", "Criminology (INT)", "Cryptography (INT)", "Deduction (INT)", "Education (INT)", "Gamble (INT)", "Language (INT)", "Library Search (INT)", "Local Expert (INT)", "Science (INT)", "Tactics (INT)", "Wilderness Survival (INT)", "Brawling (DEX)", "Evasion (DEX)", "Marital Arts x2(DEX)", "Melee Weapon (DEX)", "Acting (COOL)", "Play Instrument (TECH)","Archery (REF)", "Autofire x2(REF)", "Handgun (REF)", "Heavy Weapons x2(REF)", "Shoulder Arms (REF)", "Bribery (COOL)", "Conversation (EMP)", "Human Perception (EMP)", "Interrogation (COOL)", "Persuasion (COOL)", "Personal Grooming (COOL)", "Streetwise (COOL)", "Trading (COOL)", "Wardrobe & Style (COOL)", "Air Vehicle Tech (TECH)", "Basic Tech (TECH)", "Cybertech (TECH)", "Demolitions x2(TECH)", "Electronics/Security Tech x2(TECH)", "First Aid (TECH)", "Forgery (TECH)" ,"Land Vehicle Tech (TECH)", "Paint/Sculpt/Draw (TECH)", "Paramedic x2(TECH)", "Photography/Film (TECH)", "Pick Lock (TECH)", "Pick Pocket (TECH)", "Sea Vehicle Tech (TECH)", "Weapons Tech (TECH)"]

cheap, everyday, costly, premium, expensive, v_expensive = 10, 20, 50, 100, 500, 1000

weapon_costs = [costly, costly, premium, expensive, costly, premium, premium, premium, premium, expensive, expensive, expensive, premium, expensive, expensive,premium, v_expensive, 5000, premium, expensive, 5000, 10000, expensive, 5000, 5000, expensive, premium, premium, 5000]

weapon_types = ["Light Melee Weapon", "Medium Melee Weapon", "Heavy Melee Weapon", "Very Heavy Melee Weapon", "Medium Pistol", "Heavy Pistol", "Very Heavy Pistol", "SMG", "Heavy SMG", "Shotgun", "Assault Rifle", "Sniper Rifle", "Bows & Crossbows", "Grenade Launcher", "Rocket Launcher", "Air Pistol", "Battleglove", "Constitution Arms Hurricane Assault Weapon", "Dartgun", "Flamethrower", "Kendachi Mono-Three", "Malorian Arms 3516", "Microwaver", "Militech 'Cowboy' U-56 Grenade Launcher", "Rhinemetall EMG-86 Railgun", "Shrieker", "Stun Baton", "Stun Gun", "Tsunami Arms Helix"]

weapon_inventory = []

armor_costs = [everyday, costly, premium, v_expensive, premium, expensive, expensive, 5000, premium]

armor_types = ["Leathers", "Kevlar", "Light Armorjack", "Bodyweight Suit", "Medium Armorjack", "Heavy Armorjack", "Flack", "Metalgear", "Bulletproof Shield"]

armor_inventory = []

gear_types = ["Agent","Airhypo","Anti-Smog Breathing Mask","Audio Recorder","Auto Level Dampening Ear Protectors","Binoculars","Braindance Viewer","Bug Detector","Carryall","Chemical Analyzer","Computer","Cyberdeck","Disposable Cell Phone","Drum Synthesizer","Duct Tape Electric Guitar/Other Instrument","Flashlight","Food Stick","Glow Paint","Glow Stick","Grapple Gun","Handcuffs","Homing Tracer","Inflatable Bed & Sleep-bag","Kibble Pack","Lock Picking Set","Medscanner","Medtech Bag","Memory Chip","MRE","Personal CarePak","Pocket Amplifier","Radar Detector","Radiation Suit","Radio","Communicator","Radio Scanner/Music Player","Road Flare","Rope (60m/yd)","Scrambler/ Descrambler","Smart Glasses","Tech Bag","Techscanner","Techtool","Tent and Camping Equipment","Vial of Biotoxin","Vial of Poison","Video Camera","Virtuality Goggles"]

gear_costs = [premium, costly, everyday, premium, v_expensive, costly, v_expensive, expensive, everyday, v_expensive, costly, expensive, costly, expensive, everyday, expensive, everyday, cheap, everyday, cheap, premium, costly, expensive, everyday, cheap, everyday, v_expensive, premium, cheap, cheap, everyday, costly, expensive, v_expensive, premium, costly, cheap, everyday, expensive, expensive, expensive, v_expensive, premium, costly, expensive, premium, premium, premium]

gear_inventory = []



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
air_vehicle, basic, cyber, demo, electronics_security, first_aid, forgery ,land_vehicle, paintsculptdraw, para, photo_film, pick_lock, pick_pocket, sea_vehicle, weaponstech = 0, 0, 0, 0, 0, 2, 0 ,0 ,0 ,0, 0, 0, 0, 0, 0

# skill vars

skills_all = [conc, conceal_reveal, lip_read, perc, track, athletics, contort, dance, endurance, resist, stealth, drive_land, pilot_air, pilot_sea, riding, acc, animal_handling, bureau, business, comp, criminology, cyrptography, deduction, edu, gamble, lang, lib_search, local_exp, sci, tact, wild_surv, brawl, evasion, marital_arts, melee_weapon, acting, playinstrument, archery, autofire, handgun, heavy_weapons, shoulder_arms, bribe, convo, human_perc, interog, pers, personal_grooming, streetwise, trading, ward_n_style, air_vehicle, basic, cyber, demo, electronics_security, first_aid, forgery, land_vehicle, paintsculptdraw, para, photo_film, pick_lock, pick_pocket, sea_vehicle, weaponstech]

# images

image_first_page = Image.open("assets/1-1.png")
image_second_page = Image.open("assets/1-2.png")
image_third_page = Image.open("assets/1-3.png")

################################################

# Tkinter window stuff

tk.Label(root, text="Stats:").grid(row=1, column=1)
tk.Label(root, text="Skills:").grid(row=1, column=6)
tk.Label(root, text="Character Name:").grid(row=15, column=0)
tk.Label(root, text="Role:").grid(row=17, column=0)

role = ttk.Combobox(
    root,
    values=["Rockerboy", "Solo", "Netrunner", "Tech", "Medtech", "Media", "Exec", "Lawman", "Fixer", "Nomad"],
    state="readonly"
)
role.grid(row=17, column=1)

role.set("Select your role...")

charName = tk.Entry(root)
charName.grid(row=15, column=1)

for i in range(10):
    statspin = horizontal_scale = Scale(root, from_=2, to=8, orient="horizontal")
    statspin.grid(row=i+2, column=1)
    tk.Label(root, text=stats[i]).grid(row=i+2, column=0)
    statEntry.append(statspin)

for i in range(len(skills_all)):
    if i == 0 or i == 3 or i == 5 or i == 10 or i == 23 or i == 56 or i == 31 or i == 32 or i == 43 or i == 44 or i == 46:
        skillspin = horizontal_scale = Scale(root, from_=2, to=6, orient="horizontal")
    else:
        skillspin = horizontal_scale = Scale(root, from_=0, to=6, orient="horizontal")

    if i < 22:
        tk.Label(root, text=prettyall[i]).grid(row=i + 2, column=3)
        skillspin.grid(row=i + 2, column=4)
    elif 22 <= i < 44:
        tk.Label(root, text=prettyall[i]).grid(row=i - 20, column=5)
        skillspin.grid(row=i - 20, column=6)
    elif 44 <= i < 66:
        tk.Label(root, text=prettyall[i]).grid(row=i - 42, column=7)
        skillspin.grid(row=i - 42, column=8)

    skillEntry.append(skillspin)

# new functions

# Image writing and generation
def draw_image():
    bconc, bconceal, blip, bperc, btrack = stats_choice[5] + skills_all[0], stats_choice[0] + skills_all[1], \
                                           stats_choice[
                                               0] + skills_all[2], stats_choice[0] + skills_all[3], stats_choice[0] + \
                                           skills_all[4]

    bathletics, bcontort, bdance, bendurance, bresist, bstealth = stats_choice[2] + skills_all[5], stats_choice[2] + \
                                                                  skills_all[6], stats_choice[2] + skills_all[7], \
                                                                  stats_choice[5] + skills_all[8], stats_choice[5] + \
                                                                  skills_all[9], stats_choice[2] + skills_all[10]

    bdrive_land, bpilot_air, bpilot_sea, briding = stats_choice[1] + skills_all[11], stats_choice[1] + skills_all[12], \
                                                   stats_choice[1] + skills_all[13], stats_choice[1] + skills_all[14]

    bacc, banimal_handling, bbureau, bbusiness, bcomp, bassecriminology, bcyrptography, bdeduction, bedu, bgamble, blang, blib_search, blocal_exp, bsci, btact, bwild_surv = \
        stats_choice[0] + skills_all[15], stats_choice[0] + skills_all[16], stats_choice[0] + skills_all[17], \
        stats_choice[0] + \
        skills_all[18], stats_choice[0] + skills_all[19], stats_choice[0] + skills_all[20], stats_choice[0] + \
        skills_all[21], \
        stats_choice[0] + skills_all[22], stats_choice[0] + skills_all[23], stats_choice[0] + skills_all[24], \
        stats_choice[0] + \
        skills_all[25], stats_choice[0] + skills_all[26], stats_choice[0] + skills_all[27], stats_choice[0] + \
        skills_all[28], \
        stats_choice[0] + skills_all[29], stats_choice[0] + skills_all[30]

    bbrawl, bevasion, bmarital_arts, bmelee_weapon = stats_choice[2] + skills_all[31], stats_choice[2] + skills_all[32], \
                                                     stats_choice[2] + skills_all[33], stats_choice[2] + skills_all[34]

    bacting, bplayinstrument = stats_choice[4] + skills_all[35], stats_choice[3] + skills_all[36]

    barchery, bautofire, bhandgun, bheavy_weapons, bshoulder_arms = stats_choice[1] + skills_all[37], stats_choice[1] + \
                                                                    skills_all[38], stats_choice[1] + skills_all[39], \
                                                                    stats_choice[1] + skills_all[40], stats_choice[1] + \
                                                                    skills_all[41]

    bbribe, bconvo, bhuman_perc, binterog, bpers, bpersonal_grooming, bstreetwise, btrading, bward_n_style = \
    stats_choice[
        4] + \
    skills_all[42], \
    stats_choice[
        9] + \
    skills_all[43], \
    stats_choice[
        9] + \
    skills_all[44], \
    stats_choice[
        4] + \
    skills_all[45], \
    stats_choice[
        4] + \
    skills_all[46], \
    stats_choice[
        4] + \
    skills_all[47], \
    stats_choice[
        4] + \
    skills_all[48], \
    stats_choice[
        4] + \
    skills_all[49], \
    stats_choice[
        4] + \
    skills_all[50]

    bair_vehicle, bbasic, bcyber, bdemo, belectronics_security, bfirst_aid, bforgery, bland_vehicle, bpaintsculptdraw, bpara, bphoto_film, bpick_lock, bpick_pocket, bsea_vehicle, bweapons = \
        stats_choice[3] + skills_all[51], stats_choice[3] + skills_all[52], stats_choice[3] + skills_all[53], \
        stats_choice[3] + \
        skills_all[54], stats_choice[3] + skills_all[55], stats_choice[3] + skills_all[56], stats_choice[3] + \
        skills_all[57], \
        stats_choice[3] + skills_all[58], stats_choice[3] + skills_all[59], stats_choice[3] + skills_all[60], \
        stats_choice[3] + \
        skills_all[61], stats_choice[3] + skills_all[62], stats_choice[3] + skills_all[63], stats_choice[3] + \
        skills_all[64], \
        stats_choice[3] + skills_all[65]

    basecalc = [bconc, bconceal, blip, bperc, btrack, bathletics, bcontort, bdance, bendurance, bresist, bstealth,
                bdrive_land, bpilot_air, bpilot_sea, briding, bacc, banimal_handling, bbureau, bbusiness, bcomp,
                bassecriminology, bcyrptography, bdeduction, bedu, bgamble, blang, blib_search, blocal_exp, bsci, btact,
                bwild_surv, bbrawl, bevasion, bmarital_arts, bmelee_weapon, bacting, bplayinstrument, barchery,
                bautofire, bhandgun, bheavy_weapons, bshoulder_arms, bbribe, bconvo, bhuman_perc, binterog, bpers,
                bpersonal_grooming, bstreetwise, btrading, bward_n_style, bair_vehicle, bbasic, bcyber, bdemo,
                belectronics_security, bfirst_aid, bforgery, bland_vehicle, bpaintsculptdraw, bpara, bphoto_film,
                bpick_lock,
                bpick_pocket, bsea_vehicle, bweapons]

    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)

    if part == 1:
        draw = ImageDraw.Draw(image_first_page)
        position_y = 196
        position_y_skills = 205

        draw.text((176,648), role_choice, font=font, fill=(0,0,0))
        draw.text((197, 574), charname, font=font, fill=(0,0,0))

        for o in range(12):
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
            position_y += 120 - o
            position_stats = (635, position_y)

            if o < 10:
                if o == 0:
                    position_y = 196
                    position_stats = (635, position_y)
                if o == 6 or o == 9:
                    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
                    position_y += 20
                    position_stats = (675, position_y)
                draw.text(position_stats, str(stats_choice[o]), font=font, fill=(0, 0, 0))
            else:
                draw.text((323, 1384), str(hp), font=font, fill=(0, 0, 0))
                draw.text((444, 1263), str(hum), font=font, fill=(0, 0, 0))

        # first column writings
        for k in range(25):
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
            position_y_skills += 39
            position_stats_skills = (1094, position_y_skills)

            if k == 0:
                position_y_skills = 200
                position_stats_skills = (1094, position_y_skills)

            if k == 5 or k == 11 or k == 25 or k == 15:
                position_y_skills += 46
                position_stats_skills = (1094, position_y_skills)

            if k == 0 or k == 8 or k == 9:
                draw.text(position_stats_skills, str(stats_choice[5]), font=font, fill=(0, 0, 0))
            elif 0 < k < 5 or 14 < k < 25:
                draw.text(position_stats_skills, str(stats_choice[0]), font=font, fill=(0, 0, 0))
            elif k == 5 or k == 6 or k == 7 or k == 10:
                draw.text(position_stats_skills, str(stats_choice[2]), font=font, fill=(0, 0, 0))
            elif 10 < k < 15:
                draw.text(position_stats_skills, str(stats_choice[1]), font=font, fill=(0, 0, 0))

        for i in range(25):
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
            position_y_skills += 39
            position_level_skills = (1031, position_y_skills)

            if i == 0:
                position_y_skills = 200
                position_level_skills = (1031, position_y_skills)

            if i == 4 or i == 10 or i == 24 or i == 14:
                position_y_skills += 46

            draw.text(position_level_skills, str(skills_all[i]), font=font, fill=(0, 0, 0))

        for i in range(25):
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
            position_y_skills += 39
            position_base_skills = (1162, position_y_skills)

            if i == 0:
                position_y_skills = 200
                position_base_skills = (1162, position_y_skills)

            if i == 4 or i == 10 or i == 24 or i == 14:
                position_y_skills += 46

            draw.text(position_base_skills, str(basecalc[i]), font=font, fill=(0, 0, 0))

        # last column writings

        for i in range(26):
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
            position_y_skills += 39
            position_stats_skills = (2080, position_y_skills)

            if i == 0:
                position_y_skills = 200
                position_stats_skills = (2080, position_y_skills)

            if i == 2 or i == 11:
                position_y_skills += 44
                position_stats_skills = (2080, position_y_skills)

            if i == 0 or i == 1:
                draw.text(position_stats_skills, str(stats_choice[1]), font=font, fill=(0, 0, 0))
            elif i == 2 or 4 < i < 11:
                draw.text(position_stats_skills, str(stats_choice[4]), font=font, fill=(0, 0, 0))
            elif i == 3 or i == 4:
                draw.text(position_stats_skills, str(stats_choice[9]), font=font, fill=(0, 0, 0))
            elif 10 < i < 27:
                position_y_skills += 1
                draw.text(position_stats_skills, str(stats_choice[3]), font=font, fill=(0, 0, 0))

        for i in range(26):
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
            position_y_skills += 39
            position_level_skills = (2016, position_y_skills)

            if i == 0:
                position_y_skills = 200
                position_level_skills = (2016, position_y_skills)

            if i == 1 or i == 10:
                position_y_skills += 44

            if i == 14:
                position_y_skills += 10

            draw.text(position_level_skills, str(skills_all[i+40]), font=font, fill=(0, 0, 0))

            if i == 26:
                break

        for i in range(26):
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
            position_y_skills += 39
            position_base_skills = (2148, position_y_skills)

            if i == 0:
                position_y_skills = 200
                position_base_skills = (2148, position_y_skills)

            if i == 1 or i == 10:
                position_y_skills += 44

            if i == 14:
                position_y_skills += 10

            draw.text(position_base_skills, str(basecalc[i+40]), font=font, fill=(0, 0, 0))

            if i == 26:
                break

        # middle column

        for i in range(21):
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
            position_y_skills += 39
            position_stats_skills = (1590, position_y_skills)

            if i == 0:
                position_y_skills = 239
                position_stats_skills = (1590, position_y_skills)

            if i == 4 or i == 7 or i == 16:
                position_y_skills += 43
                position_stats_skills = (1590, position_y_skills)

            if i == 11 or i == 15 or i == 18:
                position_y_skills += 40
                position_stats_skills = (1590, position_y_skills)

            if i < 11:
                draw.text(position_stats_skills, str(stats_choice[0]), font=font, fill=(0, 0, 0))
            elif 10 < i < 15:
                position_y_skills += 2
                draw.text(position_stats_skills, str(stats_choice[2]), font=font, fill=(0, 0, 0))
            elif i == 15:
                draw.text(position_stats_skills, str(stats_choice[4]), font=font, fill=(0, 0, 0))
            elif i == 16 or i == 17:
                draw.text(position_stats_skills, str(stats_choice[3]), font=font, fill=(0, 0, 0))
            elif 17 < i < 21:
                draw.text(position_stats_skills, str(stats_choice[1]), font=font, fill=(0, 0, 0))
        image_first_page.show()

        if part == 2:
            drawsecond = ImageDraw.Draw(image_second_page)

def readvalues():
    global stats_choice, intel, ref, dex, tech, cool, will, luck, move, body, emp, hp, hum, role_choice, statEntry,skillEntry,charname,part
    stats_choice = [intel, ref, dex, tech, cool, will, luck, move, body, emp]
    charname = charName.get()
    role_choice = role.get()
    totalStats = 0
    totalSkills = 0

    for i in range(10):
        totalStats += int(statEntry[i].get())

    for i in range(65):
        if i == 12 or i == 38 or i == 33 or i == 54 or i == 55 or i == 59 or i == 38 or i == 40:
            totalSkills += int(skillEntry[i].get()) + int(skillEntry[i].get())
        else:
            totalSkills += int(skillEntry[i].get())

    if totalStats == 62:
        for i in range(10):
            stats_choice[i] = int(statEntry[i].get())

        hp = 10 + (body+will)/2
        hum = emp*10
    elif totalStats > 62:
        ourMessage = "Your Stat point total exceeds 62. Please reallocate your stats."
        messageVar = Message(root, text=ourMessage)
        messageVar.config(bg="red")
        messageVar.grid(row=20, column=1)
        button1 = tk.Button(root, text="OK", command=lambda: [messageVar.destroy(), button1.destroy()])
        button1.grid(row=21, column=1)
    else:
        ourMessage = "Your Stat point total is lower than 62. Please reallocate your stats."
        messageVar = Message(root, text=ourMessage)
        messageVar.config(bg="red")
        messageVar.grid(row=20, column=1)
        button1 = tk.Button(root, text="OK", command=lambda: [messageVar.destroy(), button1.destroy()])
        button1.grid(row=21, column=1)

    if totalSkills == 86:
        for i in range(len(skills_all)):
            skills_all[i] = int(skillEntry[i].get())
    elif totalSkills > 86:
        errorskills = "Your Skill level total exceeds 86. Please reallocate your stats."
        skillserror = Message(root, text=errorskills)
        skillserror.config(bg="red")
        skillserror.grid(row=22, column=1)
        buttonskills = tk.Button(root, text="OK", command=lambda: [skillserror.destroy(), buttonskills.destroy()])
        buttonskills.grid(row=23, column=1)
    else:
        errorskills = "Your Skill level total is below 86. Please reallocate your stats."
        skillserror = Message(root, text=errorskills)
        skillserror.config(bg="red")
        skillserror.grid(row=22, column=1)
        buttonskills = tk.Button(root, text="OK", command=lambda: [skillserror.destroy(), buttonskills.destroy()])
        buttonskills.grid(row=23, column=1)

    if totalSkills == 86 and totalStats == 62:
        part += 1
        draw_image()
        submit.destroy()
        gearshopping()
        ourMessage = "Successfully saved skills and stats!\nTime to shop gear!"
        messageVar = Message(root, text=ourMessage)
        messageVar.config(bg="lightgreen")
        messageVar.grid(row=20, column=9)
        button1 = tk.Button(root, text="OK", command=lambda: [gearshopping,root.destroy()])
        button1.grid(row=21, column=9)

def gearshopping():
    global eddies
    gear = tk.Tk()
    gear.title("Gearshopping")
    gear.state("zoomed")
    buyme = PhotoImage(master=gear, file="assets/buybtn.png")

    tk.Label(gear, text="Weapons:").grid(row=1, column=1)
    tk.Label(gear, text="Cost").grid(row=1, column=2)
    tk.Label(gear, text="Armors:").grid(row=1, column=4)
    tk.Label(gear, text="Cost").grid(row=1, column=5)
    tk.Label(gear, text="Gear:").grid(row=12, column=4)
    tk.Label(gear, text="Cost").grid(row=12, column=5)
    tk.Label(gear, text="Gear:").grid(row=1, column=7)
    tk.Label(gear, text="Cost").grid(row=1, column=8)

    for i in range(len(weapon_types)):
        weapons.append(tk.IntVar(value=0))
        tk.Label(gear, text=weapon_types[i]).grid(row=i+2, column=1)
        tk.Label(gear, text=weapon_costs[i]).grid(row=i+2, column=2)
        tk.Checkbutton(gear, variable=weapons[i]).grid(row=i+2, column=3)

    for j in range(len(armor_types)):
        armors.append(tk.IntVar(value=0))
        tk.Label(gear, text=armor_types[j]).grid(row=j+2, column=4)
        tk.Label(gear, text=armor_costs[j]).grid(row=j + 2, column=5)
        tk.Checkbutton(gear, variable=armors[j]).grid(row=j + 2, column=6)

    for h in range(len(gear_types)):
        purchase_gear.append(tk.IntVar(value=0))
        if h < 18:
            tk.Label(gear, text=gear_types[h]).grid(row=h + 13, column=4)
            tk.Label(gear, text=gear_costs[h]).grid(row=h + 13, column=5)
            tk.Checkbutton(gear, variable=purchase_gear[h]).grid(row=h + 13, column=6)
        elif h > 18:
            tk.Label(gear, text=gear_types[h]).grid(row=h + 2 - 19, column=7)
            tk.Label(gear, text=gear_costs[h]).grid(row=h + 2 - 19, column=8)
            tk.Checkbutton(gear, variable=purchase_gear[h]).grid(row=h + 2 - 19, column=9)

    def buy():
        global eddies, part
        total = 0
        weapon_choices = []
        armor_choices = []
        gear_choices = []

        for i in range(len(weapon_types)):
            if weapons[i].get() == 1 and eddies > 0 and eddies > weapon_costs[i]:
                total += weapon_costs[i]
                if total < eddies:
                    weapon_choices.append(i)

        for i in range(len(armor_types)):
            if armors[i].get() == 1 and eddies > 0 and eddies > armor_costs[i]:
                total += armor_costs[i]
                if total < eddies:
                    armor_choices.append(i)

        for i in range(len(gear_types)):
            if purchase_gear[i].get() == 1 and eddies > 0 and eddies > gear_costs[i]:
                total += gear_costs[i]
                if total < eddies:
                    gear_choices.append(i)

        if total <= eddies != 0:
            for i in range(len(weapon_choices)):
                weapon_inventory.append(weapon_types[weapon_choices[i]])

            for i in range(len(armor_choices)):
                armor_inventory.append(armor_types[armor_choices[i]])

            for i in range(len(gear_choices)):
                gear_inventory.append(gear_types[gear_choices[i]])

            eddies -= total

            buymsg = "Items bought successfully!"
            buym = Message(gear, text=buymsg)
            buym.config(bg="light green")
            buym.grid(row=35, column=1)
            buttonbuy = tk.Button(gear, text="OK", command=lambda: [buym.destroy(), buttonbuy.destroy()])
            buttonbuy.grid(row=36, column=1)

            part = 2

        else:
            buymsg = "Purchase failed!"
            buym = Message(gear, text=buymsg)
            buym.config(bg="red")
            buym.grid(row=35, column=1)
            buttonbuy = tk.Button(gear, text="OK", command=lambda: [buym.destroy(), buttonbuy.destroy()])
            buttonbuy.grid(row=36, column=1)

        remain = tk.Label(gear, text=f'Total eddies remaining: {eddies}€$')
        remain.grid(row=37, column=1)


        print(weapon_inventory)
        print(armor_inventory)
        print(gear_inventory)

    tk.Label(gear, text="").grid(row=36, column=1)
    remain = tk.Label(gear, text=f'Total eddies remaining: {eddies}€$')
    remain.grid(row=37, column=1)
    buybutton = tk.Button(gear, command=buy, image = buyme, borderwidth=0, highlightthickness=0, relief="flat")
    buybutton.grid(row=37, column=2, columnspan=2)
    buybutton.image = buyme

    gear.mainloop()

submit = tk.Button(root, text="Create Character", width=15, command=readvalues)
submit.grid(row=19, column=1)

root.state('zoomed')
root.mainloop()

