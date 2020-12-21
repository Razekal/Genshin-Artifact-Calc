__Author__ = "William Schuy"
__Date__ = "Dec 7th 2020"

#Program Purpose: To calculate the estimated Resin, Mora, and Artifact EXP requirements of finding an artifact you want in Genshin Impact.
# 
#

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
            print("Invalid artifact slot. Options are \"circlet\", \"timepiece\", \"goblet\", \"feather\", or \"flower\"")
    
    return artifact_slot

def select_artifact_rarity():
    rarity = user_input("What Rarity are you looking for?\n")
#    print("preloop" + rarity) #debug print
    while rarity != "4" and rarity != "5":
        rarity = user_input("Invalid. What Rarity?\n")
#        print(rarity) #debug print
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

def select_artifact_main_stat():
    main_stat = user_input("What Main Stat for the artifact are you looking for?") #Needs conditionals
    return main_stat

#def rollInitialOffStat(string mainStat)
#def rollOffStat(string offStat)
def desired_artifact_input():
    rarity = select_artifact_rarity()
    #off_stat_count = rarity_off_stat()
    artifact_set = 0#select_artifact_set()
    artifact_slot = select_artifact_slot()
    main_stat = select_artifact_main_stat()
    off_stats = 0#select_off_stats(off_stat_count)
    target_artifact = Artifact(rarity, artifact_slot, artifact_set, main_stat, off_stats)
    return target_artifact



def main():
    greeting()
    return 0

if __name__ == "__main__":
    main()
