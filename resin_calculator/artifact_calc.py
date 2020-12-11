__Author__ = "William Schuy"
__Date__ = "Dec 7th 2020"

#Program Purpose: To calculate the estimated Resin, Mora, and Artifact EXP requirements of finding an artifact you want in Genshin Impact.
# 
#

class Artifact:
    def __init__(self, rarity, artifactSet, artifactSlot, mainStat, offStatOne, offStatTwo, offStatThree, offStatFour):
        self.rarity = rarity
        self.artifactSet = artifactSet
        self.artifactSlot = artifactSlot
        self.mainStat = mainStat
        self.offStatOne = offStatOne
        self.offStatTwo = offStatTwo
        self.offStatThree = offStatThree
        self.offStatFour = offStatFour

def initializeArtifact(rarity, artifactSet, artifactSlot, mainStat, offStatOne, offStatTwo, offStatThree, offStatFour):
    target = Artifact(rarity, artifactSet, artifactSlot, mainStat, offStatOne, offStatTwo, offStatThree, offStatFour)
    return target

def userInput(message):
    userResponse = input(message)
    userResponse = userResponse.lower()
    return userResponse

def greeting():
    print("Welcome to the Artifact Calculator.\n")

def rollArtifactSlot():
    artifactSlot = userInput("What slot is your artifact?\n")
    while artifactSlot != "circlet" and artifactSlot != "goblet" and artifactSlot != "flower" and artifactSlot != "timepiece" and artifactSlot != "feather":
       artifactSlot = userInput("Invalid type. What Slot is your artifact?")
    return artifactSlot

def setArtifactRarity():
    rarity = userInput("What Rarity are you looking for?\n")
    print("preloop" + rarity)
    while rarity != "4" and rarity != "5":
        rarity = userInput("Invalid. What Rarity?\n")
        print(rarity)
    return rarity

def rollArtifactMainStat(string artifactSlot)
    if artifactSlot = "circlet":
        pass
    elif artifactSlot = "goblet"
        pass
    elif artifactSlot = "feather"
        pass
    elif artifactSlot = "timepiece"
        pass
    elif artifactSlot = "flower"
        pass
    return 0 #needs variable to return

def setArtifactMainStat():
    mainStat = userInput("What Main Stat for the artifact are you looking for?") #Needs conditionals
    return mainStat

#def rollInitialOffStat(string mainStat)
#def rollOffStat(string offStat)
#def desiredArtifactInput()
def main():
    artifact = initializeArtifact("", "", "", "", "", "", "", "")
    greeting()
    artifact.rarity = setArtifactRarity()
    artifact.artifactSlot = setArtifactSlot()
    artifact.mainStat = setArtifactMainStat()
    print(artifact.artifactSlot)
    return 0

if __name__ == "__main__":
    main()
