from guess_game.guesser import guess_the_game
from gaming_luck.gaming_luck import gaming_luck_meter
from recommend_game.recommend_game import recommend_game
import builtins

# Guess Game
print("Game Guesser Example:")

# Gaming Luck
print("\nGaming Luck Example:\n")

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