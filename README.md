![Build Status](https://github.com/software-students-spring2025/3-python-package-atajo-devs/actions/workflows/build.yml/badge.svg)

# VideoGameDay

## Description
A fun Python package for gamers! Get video game recommendations, trivia, guessing challenges, and a gaming luck meter to predict your gaming fate.

## Team Members:
- [Lily Fu](https://github.com/fulily0325)<br>
- [JiaLiang Tang](https://github.com/JialiangTang1)<br>
- [Peng Jiang](https://github.com/PengJiang-Victor)<br>
- [Jinzhi Cao](https://github.com/eth3r3aI)<br>

## PyPI Package

## Installation

1. Install pip in local environment

2. Install the package
    ```
    pip install VideoGameDay
    ```
3. Import functions
    ```
    from VideoGameDay import *
    ```

## Features

Examples in the python file: [Example.py](https://github.com/software-students-spring2025/3-python-package-atajo-devs/blob/main/example.py)

**This package includes four exciting gaming-related functions:**

### 1. Game Guessing

This function is about to guess video games based on a given cryptic description. It compares the input description to a set of predefined hints and returns the closest matching game.

Matches the input description to known game hints using similarity comparison. Returns the closest matching game title. If no close match is found, selects a random game from a predefined list.

#### **Usage Example:**

Pass a cryptic game description as a string to get the best-matching game:

```
description = "A silent hero, a green outfit, a princess in distress."
print(guess_the_game(description))
```

Example Output:
```
The answer is The Legend of Zelda!
```

### 2. Gaming Luck Meter

This function predicts how lucky you will be in your gaming session today. It allows you to select a game genre and then generates a randomized luck percentage based on weighted probabilities, favoring higher luck outcomes.  

#### **Usage Example:**

Run the function to select a game genre and receive your luck prediction:  

```
🎮 Choose your game type today:
  [FPS] - First-Person Shooter
  [RPG] - Role-Playing Game
  [Strategy] - Strategy/Tactics
  [Racing] - Racing Game
  [Fighting] - Fighting Game
  [MMO] - Massively Multiplayer Online
  [Survival] - Survival Game
  [Horror] - Horror Game
  [Sandbox] - Sandbox/Open World
  [Puzzle] - Puzzle/Logic Game
Enter your choice: FPS
```

Example Output:
```
🎮 You're playing「First-Person Shooter」today! 
   Your gaming luck is「51%」.
🔫 Decent accuracy today, but expect some missed shots and a few annoying campers.
```
### 3. Recommend game
Run the function to select a game genre and discover a game to play:

```
What kind of games would you like to play?
0. RPG
1. Shooter
2. Horror
3. Platformer
4. Open-World/Action-Adventure
5. Puzzle
6. Sandbox
7. Random
```

Example Output:
```
You should play Elden Ring!
```
### 4. Funfacts about one game
By importing the package, you can get a random fun fact about certain game specified.
Example usage:
```
from src.fun_facts import get_fun_facts

print(get_fun_facts("Elden Ring"))  # Works normally
print(get_fun_facts("Baldurs Gate 3"))  # Fuzzy match suggests "Baldur's Gate 3"
print(get_fun_facts("Doom"))  # No match found
```
Example output:
```
🎮 Fun fact about Elden Ring: One of the most iconic bosses, Malenia, has defeated millions of players worldwide.

Did you mean 'Baldur's Gate 3'?
🎮 Fun fact: Baldur's Gate 3 was in early access for nearly three years before its full release in 2023.

❌ Sorry, I don't have fun facts for 'Doom'. Try another game!
```


## Link to this package on pypi
https://pypi.org/project/VideoGameDay/


