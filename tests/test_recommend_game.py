"""Test module for game recommendation system using pytest and mocking."""
# test_recommend_game.py
import pytest
from unittest.mock import patch
from recommend_game.recommend_game import recommend_game

# Sample game data for testing
TEST_GENRES = ["RPG", "Shooter", "Horror", "Platformer", "Open-World/Action-Adventure", "Puzzle", "Sandbox"]
TEST_GAMES = {
    "RPG": ["The Witcher 3", "Final Fantasy"],
    "Shooter": ["DOOM", "Halo"],
    "Horror": ["Resident Evil", "Silent Hill"]
}

def test_recommendation_flow(mock_dict, mock_cat):
    """Test full recommendation flow with valid input."""
    mock_cat.return_value = TEST_GENRES
    mock_dict.return_value = TEST_GAMES

    with patch('builtins.input', return_value='0'):
        with patch('builtins.print') as mock_print:
            recommend_game()
            mock_print.assert_called_with(f"You should play {TEST_GAMES['RPG'][0]}!")

def test_invalid_then_valid_input(mock_dict, mock_cat):
    """Test recovery from invalid input."""
    mock_cat.return_value = TEST_GENRES
    mock_dict.return_value = TEST_GAMES

    with patch('builtins.input', side_effect=['invalid', '1']):
        with patch('builtins.print') as mock_print:
            recommend_game()
            mock_print.assert_called_with(f"You should play {TEST_GAMES['Shooter'][0]}!")

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
    pytest.main(["-v", "tests/test_recommend_game.py"])