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
    assert artifact_calc.validate_artifact_slot("goble") == False
    assert artifact_calc.validate_artifact_slot("goblett") == False
    assert artifact_calc.validate_artifact_slot(1) == False
    assert artifact_calc.validate_artifact_slot("time-piece") == False
    
def test_validate_main_stat():
    assert artifact_calc.validate_main_stat("circlet", "hp%") == True
    assert artifact_calc.validate_main_stat("timepiece", "recharge") == True
    assert artifact_calc.validate_main_stat("goblet", "physical damage") == True
    assert artifact_calc.validate_main_stat("circlet", "elemental damage") == False
    assert artifact_calc.validate_main_stat("timepiece", "crit rate") == False
    assert artifact_calc.validate_main_stat("goblet", "crit rate") == False
    

def test_validate_set_selection():
    assert artifact_calc.validate_set_selection(5, "gladiator's") == True
    assert artifact_calc.validate_set_selection(5, "resolution of sojourner") == False
    assert artifact_calc.validate_set_selection(4, "bloodstained chivalry") == True
    assert artifact_calc.validate_set_selection(4, "instructor") == True
    assert artifact_calc.validate_set_selection(4, "5") == False

def test_validate_off_stats():
    assert artifact_calc.validate_off_stats("crit rate", [], "atk%") == True
    assert artifact_calc.validate_off_stats("crit rate", [], "crit rate") == False
    assert artifact_calc.validate_off_stats("crit rate", ["crit rate"], "atk%") == False
    assert artifact_calc.validate_off_stats("", [], "atk%") == False

    