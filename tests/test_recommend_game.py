"""Test module for game recommendation system using pytest and mocking."""
# test_recommend_game.py
import pytest
from unittest.mock import patch
from recommend_game import recommend_game, validate_input

# Sample game data for testing
TEST_GENRES = ["RPG", "Shooter", "Horror"]
TEST_GAMES = {
    "RPG": ["The Witcher 3", "Final Fantasy"],
    "Shooter": ["DOOM", "Halo"],
    "Horror": ["Resident Evil", "Silent Hill"]
}

def test_validate_input_valid_numbers():
    """Test numeric input validation."""
    assert validate_input("0") == ("RPG", 1)
    assert validate_input("1") == ("Shooter", 1)
    assert validate_input("2") == ("Horror", 1)
    assert validate_input("3") == (TEST_GENRES[0], 1)  # Random choice

def test_validate_input_valid_text():
    """Test text input validation."""
    assert validate_input("RPG") == ("RPG", 1)
    assert validate_input("shooter") == ("Shooter", 1)
    assert validate_input("HORROR") == ("Horror", 1)
    assert validate_input("random") == (TEST_GENRES[0], 1)

def test_validate_input_invalid():
    """Test invalid input handling."""
    assert validate_input("invalid") == (None, 0)
    assert validate_input("99") == (None, 0)
    assert validate_input("") == (None, 0)

@patch('recommend_game.get_game_categories')
@patch('recommend_game.get_game_dict')
def test_recommendation_flow(mock_dict, mock_cat):
    """Test full recommendation flow with valid input."""
    mock_cat.return_value = TEST_GENRES
    mock_dict.return_value = TEST_GAMES

    with patch('builtins.input', return_value='0'):
        with patch('builtins.print') as mock_print:
            recommend_game()
            mock_print.assert_called_with(f"You should play {TEST_GAMES['RPG'][0]}!")

@patch('recommend_game.get_game_categories')
@patch('recommend_game.get_game_dict')
def test_invalid_then_valid_input(mock_dict, mock_cat):
    """Test recovery from invalid input."""
    mock_cat.return_value = TEST_GENRES
    mock_dict.return_value = TEST_GAMES

    with patch('builtins.input', side_effect=['invalid', '1']):
        with patch('builtins.print') as mock_print:
            recommend_game()
            mock_print.assert_called_with(f"You should play {TEST_GAMES['Shooter'][0]}!")

@patch('recommend_game.get_game_categories')
@patch('recommend_game.get_game_dict')
def test_random_selection(mock_dict, mock_cat):
    """Test random selection functionality."""
    mock_cat.return_value = TEST_GENRES
    mock_dict.return_value = TEST_GAMES

    with patch('builtins.input', return_value=str(len(TEST_GENRES))):
        with patch('builtins.print') as mock_print:
            recommend_game()
            args, _ = mock_print.call_args
            assert args[0].startswith("You should play")

if __name__ == "__main__":
    pytest.main(["-v", "test_recommend_game.py"])