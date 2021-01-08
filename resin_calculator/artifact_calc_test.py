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

def test_validate_artifact_slots():
    assert artifact_calc.validate_artifact_slot("circlet") == True
    assert artifact_calc.validate_artifact_slot("flower") == True
    assert artifact_calc.validate_artifact_slot("timepiece") == True
    assert artifact_calc.validate_artifact_slot("feather") == True
    assert artifact_calc.validate_artifact_slot("goblet") == True
    assert artifact_calc.validate_artifact_slot("goble") == False
    assert artifact_calc.validate_artifact_slot("goblett") == False
    assert artifact_calc.validate_artifact_slot(1) == False
    assert artifact_calc.validate_artifact_slot("time-piece") == False
    
def test_validate_main_stat():
    assert artifact_calc.validate_main_stat("circlet", "hp%") == True
    assert artifact_calc.validate_main_stat("circlet", "def%") == True
    assert artifact_calc.validate_main_stat("circlet", "atk%") == True
    assert artifact_calc.validate_main_stat("circlet", "elemental mastery") == True
    assert artifact_calc.validate_main_stat("circlet", "crit rate") == True
    assert artifact_calc.validate_main_stat("circlet", "crit damage") == True
    assert artifact_calc.validate_main_stat("circlet", "healing%") == True
    assert artifact_calc.validate_main_stat("timepiece", "hp%") == True
    assert artifact_calc.validate_main_stat("timepiece", "def%") == True
    assert artifact_calc.validate_main_stat("timepiece", "atk%") == True
    assert artifact_calc.validate_main_stat("timepiece", "elemental mastery") == True
    assert artifact_calc.validate_main_stat("timepiece", "recharge") == True
    assert artifact_calc.validate_main_stat("goblet", "hp%") == True
    assert artifact_calc.validate_main_stat("goblet", "def%") == True
    assert artifact_calc.validate_main_stat("goblet", "atk%") == True
    assert artifact_calc.validate_main_stat("goblet", "elemental mastery") == True
    assert artifact_calc.validate_main_stat("goblet", "elemental damage") == True
    assert artifact_calc.validate_main_stat("goblet", "physical damage") == True
    assert artifact_calc.validate_main_stat("circlet", "elemental damage") == False
    assert artifact_calc.validate_main_stat("circlet", "physical damage") == False
    assert artifact_calc.validate_main_stat("circlet", "recharge") == False
    assert artifact_calc.validate_main_stat("circlet", "hp") == False
    assert artifact_calc.validate_main_stat("circlet", "hp %") == False
    assert artifact_calc.validate_main_stat("circlet", "elemental damage") == False
    assert artifact_calc.validate_main_stat("timepiece", "crit rate") == False
    assert artifact_calc.validate_main_stat("timepiece", "crit damage") == False
    assert artifact_calc.validate_main_stat("timepiece", "healing%") == False
    assert artifact_calc.validate_main_stat("goblet", "crit rate") == False
    assert artifact_calc.validate_main_stat("goblet", "crit damage") == False
    assert artifact_calc.validate_main_stat("goblet", "healing%") == False
    assert artifact_calc.validate_main_stat("timepiece", "elemental damage") == False
    assert artifact_calc.validate_main_stat("timepiece", "physical damage") == False   
    assert artifact_calc.validate_main_stat("circlet", "") == False
    

def test_validate_set_selection():
    assert artifact_calc.validate_set_selection(5, "gladiator's") == True
    assert artifact_calc.validate_set_selection(5, "wanderer's troupe") == True
    assert artifact_calc.validate_set_selection(5, "viridescent venerer") == True
    assert artifact_calc.validate_set_selection(5, "thundering fury") == True
    assert artifact_calc.validate_set_selection(5, "thundersoother") == True
    assert artifact_calc.validate_set_selection(5, "crimson witch of flames") == True
    assert artifact_calc.validate_set_selection(5, "lavawalker") == True
    assert artifact_calc.validate_set_selection(5, "archaic petra") == True
    assert artifact_calc.validate_set_selection(5, "retracing bolide") == True
    assert artifact_calc.validate_set_selection(5, "maiden beloved") == True
    assert artifact_calc.validate_set_selection(5, "noblesse oblige") == True
    assert artifact_calc.validate_set_selection(5, "bloodstained chivalry") == True
    assert artifact_calc.validate_set_selection(5, "instructor") == False
    assert artifact_calc.validate_set_selection(5, "berserker") == False
    assert artifact_calc.validate_set_selection(5, "exile") == False
    assert artifact_calc.validate_set_selection(5, "resolution of sojourner") == False
    assert artifact_calc.validate_set_selection(5, "martial artist") == False
    assert artifact_calc.validate_set_selection(5, "defender's will") == False
    assert artifact_calc.validate_set_selection(5, "tiny miracle") == False
    assert artifact_calc.validate_set_selection(5, "brave heart") == False
    assert artifact_calc.validate_set_selection(5, "gambler") == False
    assert artifact_calc.validate_set_selection(5, "scholar") == False
    assert artifact_calc.validate_set_selection(5, "prayer") == False    
    assert artifact_calc.validate_set_selection(5, "gladiator's") == True
    assert artifact_calc.validate_set_selection(4, "wanderer's troupe") == True
    assert artifact_calc.validate_set_selection(4, "viridescent venerer") == True
    assert artifact_calc.validate_set_selection(4, "thundering fury") == True
    assert artifact_calc.validate_set_selection(4, "thundersoother") == True
    assert artifact_calc.validate_set_selection(4, "crimson witch of flames") == True
    assert artifact_calc.validate_set_selection(4, "lavawalker") == True
    assert artifact_calc.validate_set_selection(4, "archaic petra") == True
    assert artifact_calc.validate_set_selection(4, "retracing bolide") == True
    assert artifact_calc.validate_set_selection(4, "maiden beloved") == True
    assert artifact_calc.validate_set_selection(4, "noblesse oblige") == True
    assert artifact_calc.validate_set_selection(4, "bloodstained chivalry") == True
    assert artifact_calc.validate_set_selection(4, "instructor") == True
    assert artifact_calc.validate_set_selection(4, "berserker") == True
    assert artifact_calc.validate_set_selection(4, "exile") == True
    assert artifact_calc.validate_set_selection(4, "resolution of sojourner") == True
    assert artifact_calc.validate_set_selection(4, "martial artist") == True
    assert artifact_calc.validate_set_selection(4, "defender's will") == True
    assert artifact_calc.validate_set_selection(4, "tiny miracle") == True
    assert artifact_calc.validate_set_selection(4, "brave heart") == True
    assert artifact_calc.validate_set_selection(4, "gambler") == True
    assert artifact_calc.validate_set_selection(4, "scholar") == True
    assert artifact_calc.validate_set_selection(4, "prayer") == True
    assert artifact_calc.validate_set_selection(4, "pray") == False
    assert artifact_calc.validate_set_selection(4, 5) == False


    