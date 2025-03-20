from guess_game.guesser import guess_the_game
from gaming_luck.gaming_luck import gaming_luck_meter
from recommend_game.recommend_game import recommend_game
import builtins

# Gaming Luck
print("Gaming Luck Example:\n")

game_genres = [
    "FPS",
    "Strategy",
    "Puzzle"
]

original_input = builtins.input
for genre in game_genres:
    builtins.input = lambda _: genre
    print(f"Selected genre: {genre}")
    print(gaming_luck_meter())
builtins.input = original_input

# Recommend Game
print("\nRecommend Game Example:\n")

game_genres = [
    "RPG",
    "Shooter",
    "Horror"
]

original_input = builtins.input
for genre in game_genres:
    builtins.input = lambda _: genre
    print(f"Selected genre: {genre}")
    recommend_game()
    print()
builtins.input = original_input

# Guess Game
print("\nGame Guesser Example:\n")

descriptions = [
    "A silent hero, a green outfit, a princess in distress.",
    "A blue blur dashes through loops, collecting golden rings and battling an evil doctor.",
    "You wake up in a vault, the world outside is in ruins, and your choices define humanity's fate.",
    "A space marine takes on demons from hell with an arsenal of devastating weapons.",
    "A father and daughter-like duo navigate a post-apocalyptic world filled with danger."
]

for desc in descriptions:
    print(desc)
    print(guess_the_game(desc))

# Recommend Game
print("\nRecommend Game Example:\n")

game_genres = [
    "RPG",
    "Shooter",
    "Horror"
]

original_input = builtins.input
for genre in game_genres:
    builtins.input = lambda _: genre
    print(f"Selected genre: {genre}")
    recommend_game()
    print()
builtins.input = original_input