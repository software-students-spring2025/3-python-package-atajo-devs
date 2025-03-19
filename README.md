# Team Members:
[Lily Fu](https://github.com/fulily0325)<br>
[JiaLiang Tang](https://github.com/JialiangTang1)<br>
[Peng Jiang](https://github.com/PengJiang-Victor)<br>
[Adam Cao](https://github.com/eth3r3aI)<br>

# Package Usage:
Output some fun facts about games.



## Game Guessing Function

### Description
This function is about to guess video games based on a given cryptic description. It compares the input description to a set of predefined hints and returns the closest matching game.

### Usage

#### Importing the Function
To use the function in your Python script, import it from the package:

from package_name import guess_the_game

#### Calling the Function
Pass a cryptic game description as a string to get the best-matching game:

description = "A silent hero, a green outfit, a princess in distress."
print(guess_the_game(description))

Example Output:
The answer is The Legend of Zelda!

### Functionality
Matches the input description to known game hints using similarity comparison.

Returns the closest matching game title.

If no close match is found, selects a random game from a predefined list.

