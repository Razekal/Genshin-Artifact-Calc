__Author__ = "William Schuy"
__Date__ = "Dec 7th 2020"

#Program Purpose: To calculate the estimated Resin, Mora, and Artifact EXP requirements of finding an artifact you want in Genshin Impact.
# 
#Todo: Set up upgrade counter for offstats. split validations to own functions.



valid_main_stats_by_slot = {
    "feather": "atk",
    "flower": "hp",
    "circlet": ["hp%", "def%", "atk%", "elemental mastery", "crit rate", "crit damage", "healing%"],
    "timepiece": ["hp%", "def%", "atk%", "elemental mastery", "recharge"],
    "goblet": ["hp%", "def%", "atk%", "elemental mastery", "elemental damage", "physical damage"]
}

#Not sure if valid substats should be placed in the sub stat validation function, or if I should leave as is.
valid_sub_stats = ["atk", "hp", "def", "atk%", "hp%", "def%", "elemental mastery", "crit rate", "crit damage", "recharge"]

class Artifact:
    def __init__(self, rarity, artifact_set, artifact_slot, main_stat, off_stats):
        self.rarity = rarity
        self.artifact_set = artifact_set
        self.artifact_slot = artifact_slot
        self.main_stat = main_stat
        self.off_stats = off_stats


def user_input(message):
    user_response = input(message)
    user_response = user_response.lower() #converts all inputs to lowercase to error-proof user inputs
    return user_response

def greeting():
    print("Welcome to the Artifact Calculator.\n")

def select_artifact_slot():
    valid_slot = False
    valid_artifact_slots = ["circlet", "timepiece", "goblet", "feather", "flower"]
    while valid_slot == False:
        artifact_slot = user_input("What slot is your artifact?\n")
        if validate_artifact_slots(artifact_slot, valid_artifact_slots):
            return artifact_slot
        else:
            print("Invalid artifact slot. Options are \"circlet\", \"timepiece\", \"goblet\", \"feather\", or \"flower\"\n")

def validate_artifact_slots(artifact_slot, valid_slots):
    return artifact_slot in valid_slots

def validate_rarity(rarity):
    return rarity == "3" or rarity == "4" or rarity == "5"

def select_artifact_rarity():

    valid_rarity = False
    while valid_rarity == False:
        rarity = user_input("What Rarity are you looking for?\n")
        if validate_rarity(rarity):
            return int(rarity)
        else:
            print("invalid rarity\n")


def roll_artifact_main_stat(artifact_slot): #framework for math logic later
    if artifact_slot == "circlet":
        pass
    elif artifact_slot == "goblet":
        pass
    elif artifact_slot == "feather":
        pass
    elif artifact_slot == "timepiece":
        pass
    elif artifact_slot == "flower":
        pass
    return 0 #needs variable to return

def select_artifact_main_stat(artifact_slot):
    main_stat = ""
    valid_stat = False
    if artifact_slot == "flower":
        print("Flowers can only be flat HP")
        return "HP"
    elif artifact_slot == "feather":
        print("Feathers can only be flat Attack")
        return "ATK"
    else:
        print("What Main Stat for the artifact are you looking for?\n")
        while valid_stat == False:
            main_stat = user_input("options are " + ", ".join(valid_main_stats_by_slot[artifact_slot]))
            if validate_main_stat(artifact_slot, main_stat):
                return main_stat
            else:
                print("Invalid choice.\n")

def validate_main_stat(slot, main_stat):
    return main_stat in valid_main_stats_by_slot[slot]

#def rollInitialOffStat(string mainStat)

def select_off_stats(rarity, main_stat):
    selected_rolls = 0
    if rarity == 4:
        selected_rolls += 1 #causes off_stat selection to loop one less time
    off_stats = []
    starting_rolls = user_input("Do you want the artifact to drop with full sub-stats?")
    if starting_rolls == "no":
        selected_rolls += 1 #causes off_stat selection to loop one less time
    while selected_rolls <= 3:
        valid_choice = False
        while valid_choice == False:
            stat_choice = user_input("what substat do you want?\n")
            if validate_off_stats(stat_choice, off_stats, main_stat):
                valid_choice = True
                selected_rolls += 1
                off_stats.append(stat_choice)
            else: 
                print("Invalid Choice\n") 
    return off_stats

def validate_off_stats(stat_choice, off_stats, main_stat):
    return stat_choice in valid_sub_stats and stat_choice != main_stat and stat_choice not in off_stats

#def select_off_stat_upgrade(off_stats):
    

def select_artifact_set(rarity):
    valid_sets = ["gladiator's", "wanderer's troupe", "viridescent venerer", "thundering fury", "thundersoother"
                  "crimson witch of flames", "lavawalker", "archaic petra", "retracing bolide", "maiden beloved"
                  "noblesse oblige", "bloodstained chivalry"]
    if rarity < 5:
        valid_sets = valid_sets + ["instructor", "berserker", "exile", "resolution of sojourner", "martial artist", "defender's will", 
                      "tiny miracle", "brave heart", "gambler", "scholar", "prayer"]
    valid_choice = False
    while valid_choice == False:
        artifact_set = user_input("What set are you looking for?")
        if validate_set_selection(artifact_set, valid_sets):
            return artifact_set
        else:
            print("Invalid Choice\n")

def validate_set_selection(artifact_set, valid_sets):
    return artifact_set in valid_sets

def desired_artifact_input():
    rarity = select_artifact_rarity()
    artifact_set = select_artifact_set(rarity)
    artifact_slot = select_artifact_slot()
    main_stat = select_artifact_main_stat(artifact_slot)
    off_stats = select_off_stats(rarity, main_stat)
    target_artifact = Artifact(rarity, artifact_set, artifact_slot, main_stat, off_stats)
    return target_artifact



def main():
    greeting()
    created_artifact = desired_artifact_input()
    print("\n\n\n"+ created_artifact.artifact_set)
    print(created_artifact.rarity)
    print(created_artifact.main_stat)
    print(created_artifact.artifact_slot)
    print(created_artifact)
    for x in created_artifact.off_stats:
        print(x)
    return 0

if __name__ == "__main__":
    main()
