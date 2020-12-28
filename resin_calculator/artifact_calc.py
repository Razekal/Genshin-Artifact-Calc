__Author__ = "William Schuy"
__Date__ = "Dec 7th 2020"

#Program Purpose: To calculate the estimated Resin, Mora, and Artifact EXP requirements of finding an artifact you want in Genshin Impact.
# 
#

valid_main_stats_by_slot = {
    "feather": "atk",
    "flower": "hp",
    "circlet": ["hp%", "def%", "atk%", "elemental mastery", "crit rate", "crit damage", "healing%"],
    "timepiece": ["hp%", "def%", "atk%", "elemental mastery", "recharge"],
    "goblet": ["hp%", "def%", "atk%", "elemental mastery", "elemental damage", "physical damage"]
}

class Artifact:
    def __init__(self, rarity, artifact_set, artifact_slot, main_stat, off_stats):
        self.rarity = rarity
        self.artifact_set = artifact_set
        self.artifact_slot = artifact_slot
        self.main_stat = main_stat
        self.off_stats = off_stats

def initializeArtifact(rarity, artifact_set, artifact_slot, main_stat, off_stats):
    target = Artifact(rarity, artifact_set, artifact_slot, main_stat, off_stats)
    return target

def user_input(message):
    user_response = input(message)
    user_response = user_response.lower()
    return user_response

def greeting():
    print("Welcome to the Artifact Calculator.\n")

def select_artifact_slot():
    valid_slot = False
    slots = ["circlet", "timepiece", "goblet", "feather", "flower"]
    while valid_slot == False:
        artifact_slot = user_input("What slot is your artifact?\n")
        if artifact_slot in slots:
            valid_slot = True
        else:
            print("Invalid artifact slot. Options are \"circlet\", \"timepiece\", \"goblet\", \"feather\", or \"flower\"\n")
    
    return artifact_slot

def select_artifact_rarity():
    rarity = user_input("What Rarity are you looking for?\n")
    #print("preloop" + rarity) #debug print
    while rarity != "3" and rarity != "4" and rarity != "5": 
        rarity = user_input("Invalid. What Rarity?\n")
        #print(rarity) #debug print
    return int(rarity)

def roll_artifact_main_stat(artifact_slot):
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
            if main_stat in valid_main_stats_by_slot[artifact_slot]:
                valid_stat = True
            else:
                print("Invalid choice.\n")
    return main_stat

#def rollInitialOffStat(string mainStat)
def select_off_stats(rarity, main_stat):
    total_rolls = (2*rarity)-1
    selected_rolls = 0
    sub_stats = ["hp", "hp%", "atk", "atk%", "def%", "def", "elemental mastery", "recharge%", "crit rate", "crit damage"]
    off_stats = ["", "", "", ""]
    starting_rolls = user_input("Do you want the artifact to drop with full sub-stats?")
    if starting_rolls == "no":
        total_rolls = total_rolls - 1 #Relevant when off stat upgrades are implemented
    while selected_rolls < 3:
        valid_choice = False
        while valid_choice == False:
            stat_choice = user_input("what substat do you want?\n")
            if stat_choice in sub_stats:
                valid_choice = True
            else: 
                print("Invalid Choice\n") 
        selected_rolls = selected_rolls + 1
        off_stats[selected_rolls] = stat_choice
    return off_stats
### Come back to this later, get the initial set up first. Create off_stat_upgrade() and implement there.

#    while selected_rolls >= 4:
#        print("Current stats are:\n")
#        for x in off_stats:
#            counter = 1
#            print(counter + ": " + x + "\n")
#        user_input("What stat do you want to upgrade?")
###

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
        if artifact_set in valid_sets:
            valid_choice = True
        else:
            print("Invalid Choice\n")
    return artifact_set

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
