import re

import io

import artifact_calc

def test_validate_rarity():
    assert artifact_calc.validate_rarity("4") == True
    assert artifact_calc.validate_rarity("s") == False
    assert artifact_calc.validate_rarity(4) == False
    assert artifact_calc.validate_rarity("5") == True
    assert artifact_calc.validate_rarity("3") == True
    assert artifact_calc.validate_rarity("2") == False
    assert artifact_calc.validate_rarity("1") == False
    assert artifact_calc.validate_rarity("6") == False

def test_validate_set_selection_five():
    valid_sets = ["gladiator's", "wanderer's troupe", "viridescent venerer", "thundering fury", "thundersoother"
                  "crimson witch of flames", "lavawalker", "archaic petra", "retracing bolide", "maiden beloved"
                  "noblesse oblige", "bloodstained chivalry"]
    assert artifact_calc.validate_set_selection("gladiator's", valid_sets) == True
    assert artifact_calc.validate_set_selection("instructor", valid_sets) == False
    
def test_validate_set_selection_four():
    valid_sets = ["gladiator's", "wanderer's troupe", "viridescent venerer", "thundering fury", "thundersoother"
                  "crimson witch of flames", "lavawalker", "archaic petra", "retracing bolide", "maiden beloved"
                  "noblesse oblige", "bloodstained chivalry"]
    #Copy paste from code for if rarity <= 4:
    valid_sets = valid_sets + ["instructor", "berserker", "exile", "resolution of sojourner", "martial artist", "defender's will", 
                              "tiny miracle", "brave heart", "gambler", "scholar", "prayer"]
    assert artifact_calc.validate_set_selection("gladiator's", valid_sets) == True
    assert artifact_calc.validate_set_selection("instructor", valid_sets) == True
    

    