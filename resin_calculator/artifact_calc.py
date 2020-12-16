__Author__ = "William Schuy"
__Date__ = "Dec 7th 2020"

#Program Purpose: To calculate the estimated Resin, Mora, and Artifact EXP requirements of finding an artifact you want in Genshin Impact.
# 
#

class Artifact:
    def __init__(self, rarity, artifact_set, artifact_slot, main_stat, off_stat_one, off_stat_two, off_stat_three, off_stat_four):
        self.rarity = rarity
        self.artifact_set = artifact_set
        self.artifact_slot = artifact_slot
        self.main_stat = main_stat
        self.off_stat_one = off_stat_one
        self.off_stat_two = off_stat_two
        self.off_stat_three = off_stat_three
        self.off_stat_four = off_stat_four

def initializeArtifact(rarity, artifact_set, artifact_slot, main_stat, off_stat_one, off_stat_two, off_stat_three, off_stat_four):
    target = Artifact(rarity, artifact_set, artifact_slot, main_stat, off_stat_one, off_stat_two, off_stat_three, off_stat_four)
    return target

def user_input(message):
    user_response = input(message)
    user_response = user_response.lower()
    return user_response

def greeting():
    print("Welcome to the Artifact Calculator.\n")

def select_artifact_slot():
    artifact_slot = user_input("What slot is your artifact?\n")
    while artifact_slot != "circlet" and artifact_slot != "goblet" and artifact_slot != "flower" and artifact_slot != "timepiece" and artifact_slot != "feather":
       artifact_slot = user_input("Invalid type. What Slot is your artifact?")
    return artifact_slot

def select_artifact_rarity():
    rarity = user_input("What Rarity are you looking for?\n")
    print("preloop" + rarity)
    while rarity != "4" and rarity != "5":
        rarity = user_input("Invalid. What Rarity?\n")
        print(rarity)
    return rarity

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
#def desiredArtifactInput()
def main():
    artifact = initializeArtifact("", "", "", "", "", "", "", "")
    greeting()
    artifact.rarity = select_artifact_rarity()
    artifact.artifact_slot = select_artifact_slot()
    artifact.mainStat = select_artifact_main_stat()
    print(artifact.artifact_slot)
    return 0

if __name__ == "__main__":
    main()
