import unittest
from VideoGameDay.recommend_game import validate_input
from VideoGameDay.game_data import get_game_categories

class TestRecommendGame(unittest.TestCase):

    def test_validate_input_valid_numeric(self):
        """Test if a valid numeric input returns the correct genre."""
        genres = get_game_categories()
        for i in range(len(genres)):
            genre, valid = validate_input(str(i))  # Convert index to string
            self.assertEqual(genre, genres[i])
            self.assertEqual(valid, 1)

    def test_validate_input_valid_text(self):
        """Test if a valid genre name (case-insensitive) returns the correct genre."""
        genres = get_game_categories()
        for genre in genres:
            genre_lower = genre.lower()
            result, valid = validate_input(genre_lower)
            self.assertEqual(result, genre)
            self.assertEqual(valid, 1)

    def test_validate_input_invalid(self):
        """Test if an invalid input returns (None, 0)."""
        invalid_inputs = ["invalid", "-1", "100", "notagenre"]
        for invalid in invalid_inputs:
            result, valid = validate_input(invalid)
            self.assertIsNone(result)
            self.assertEqual(valid, 0)

if __name__ == "__main__":
    unittest.main()
