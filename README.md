# Genshin Artifact Calc

_Genshin Impact is a game with an emphasis on open world exploration, with a character progression system deeply tied to Artifacts you can loot from dungeons and bosses. However, the progression in Genshin Impact is limited by a timegated resource called Resin. The goal of this program is to determine roughly how much resin it would take to find an ideal artifact that the user is looking for so they can expect roughly how long it will take to acquire the item of choice (or how many dollars it would cost to mitigate the time requirement)_

## Usage

Run the program with:
```
python resin_calculator/artifact_calc.py
```
Follow the prompts to describe your ideal artifact. The program will calculate
how much resin you will need, on average, to find that artifact.

## Development

Tests can be run using `pytest`:
```
pip3 install pytest pytest-cov
pytest --cov=artifact_calc # in project root
```
