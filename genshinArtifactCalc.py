__Author__ = "William Schuy"
__Date__ = "Dec 7th 2020"

#Program Purpose: To calculate the estimated Resin, Mora, and Artifact EXP requirements of finding an artifact you want in Genshin Impact.
# 
#

class Artifact:
    def __init__(self, rarity, artifactSet, artifactSlot, mainStat, offStatA, secondOffStat, thirdOffStat, fourthOffStat):
        self.rarity = rarity
        self.artifactSet = artifactSet
        self.artifactSlot = artifactSlot
        self.mainStat = mainStat
        self.offStatA = offStatA
        self.secondOffStat = secondOffStat
        self.thirdOffStat = thirdOffStat
        self.fourthOffStat = fourthOffStat

def initializeArtifact(rarity, artifactSet, artifactSlot, mainStat, offStatA, secondOffStat, thirdOffStat, fourthOffStat):
    target = Artifact(rarity, artifactSet, artifactSlot, mainStat, offStatA, secondOffStat, thirdOffStat, fourthOffStat)
    print(target.rarity)
    print(target.artifactSet)
    print(target.artifactSlot)
    print(target.mainStat)
    print(target.offStatA)
    print(target.secondOffStat)
    print(target.thirdOffStat)
    print(target.fourthOffStat)



#def greeting()
#def rollArtifactSlot()
#def rollArtifactMainStat(string artifactSlot)
#def rollInitialOffStat(string mainStat)
#def rollOffStat(string offStat)
#def desiredArtifactInput()
def main():
    initializeArtifact(5, "Sojourner", "Circlet", "Critical Rate", "Attack", "Defense", "Elemental Mastery", "HP")
    return 0

main()