import pytest
import re
from gaming_luck.luck_data import GAME_TYPES
from gaming_luck.gaming_luck import gaming_luck_meter

GAME_GENRES = list(GAME_TYPES.keys())
GAME_GENRE_NAMES = list(GAME_TYPES.items())

def extract_luck_percentage(output: str):
    match = re.search(r"(\d+)%", output)
    return int(match.group(1)) if match else None

@pytest.mark.parametrize("game_type", GAME_GENRES)
def test_gaming_luck_output_format(game_type, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: game_type)
    
    result = gaming_luck_meter()

    assert isinstance(result, str), "Output should be a string"

    luck_percentage = extract_luck_percentage(result)

    assert luck_percentage is not None, "Luck percentage not found in output"
    assert 0 <= luck_percentage <= 100, "Luck percentage should be between 0 and 100"

def test_luck_distribution(monkeypatch):    
    luck_values = []
    test_runs = 1000
    
    monkeypatch.setattr("builtins.input", lambda _: "RPG")

    for _ in range(test_runs):
        result = gaming_luck_meter()
        luck_percentage = extract_luck_percentage(result)
        luck_values.append(luck_percentage)

    high_luck = sum(1 for luck in luck_values if luck >= 70)
    mid_luck = sum(1 for luck in luck_values if 40 <= luck < 70)
    low_luck = sum(1 for luck in luck_values if luck < 40)

    assert high_luck > mid_luck, "High luck values should be more frequent than mid luck values"
    assert mid_luck > low_luck, "Mid luck values should be more frequent than low luck values"

@pytest.mark.parametrize("game_type, full_name", GAME_GENRE_NAMES)
def test_correct_game_type_in_output(game_type, full_name, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: game_type)
    result = gaming_luck_meter()
    assert full_name in result, f"The game type '{full_name}' should appear in the output, but got: {result}"

def test_invalid_game_type(monkeypatch):
    inputs = iter(["RandomInvalidGenre", "FPS"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    result = gaming_luck_meter()

    assert "First-Person Shooter" in result, "The valid game type should be used after an invalid input."
    
def test_gaming_luck_randomness(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "RPG")
    results = {gaming_luck_meter() for _ in range(5)}

    assert len(results) > 1, "The function should produce different outputs, indicating randomness."