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