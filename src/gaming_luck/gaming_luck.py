import random
from .luck_data import GAME_TYPES, LUCK_MESSAGES

def gaming_luck_meter() -> str:
    
    print("🎮 Choose your game type today:")
    for key, value in GAME_TYPES.items():
        print(f"  [{key}] - {value}")

    chosen_game = None
    while chosen_game not in GAME_TYPES:
        chosen_game = input("Enter your choice: ").strip()
        if chosen_game not in GAME_TYPES:
            print("❌ Invalid choice. Please select a valid game type.")

    luck_ranges = {
        "high": list(range(70, 101)),
        "mid": list(range(40, 70)),
        "low": list(range(0, 40)),
    }

    chosen_range = random.choices(
        population=["high", "mid", "low"],
        weights=[0.6, 0.35, 0.05], 
        k=1
    )[0]

    luck = random.choice(luck_ranges[chosen_range])

    if luck >= 70:
        luck_level = "high"
    elif luck >= 40:
        luck_level = "mid"
    else:
        luck_level = "low"

    message = LUCK_MESSAGES[chosen_game][luck_level]

    return f"\n🎮 You're playing「{GAME_TYPES[chosen_game]}」today! \n   Your gaming luck is「{luck}%」.\n{message}\n"

if __name__ == "__main__":
    print(gaming_luck_meter())
