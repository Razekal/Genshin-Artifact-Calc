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
    print(target.rarity)
    print(target.artifactSet)
    print(target.artifactSlot)
    print(target.mainStat)
    print(target.offStatOne)
    print(target.offStatTwo)
    print(target.offStatThree)
    print(target.offStatFour)


#def greeting()
#def rollArtifactSlot()
#def rollArtifactMainStat(string artifactSlot)
#def rollInitialOffStat(string mainStat)
#def rollOffStat(string offStat)
#def desiredArtifactInput()
def main():
    initializeArtifact(5, "Sojourner", "Circlet", "Critical Rate", "Attack", "Defense", "Elemental Mastery", "HP")
    return 0

if __name__ == "__main__":
    main()
