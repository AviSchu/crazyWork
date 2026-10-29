import os
import sys
import unittest

# Add project root directory to sys.path
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from data import INITIAL_GAMES, add_game
from logic import rank_games


class TestGameOrganizer(unittest.TestCase):

  def test_rank_games_normal(self):
    """Normal Scenario: Standard player count, duration, and tag filtering."""
    results = rank_games(
        INITIAL_GAMES, player_count=4, max_time=30, preferred_tag="party"
    )
    self.assertTrue(len(results) > 0)
    self.assertEqual(results[0]["name"], "Codenames")

  def test_rank_games_empty_data(self):
    """Empty Data / Initial State: Rank games on an empty initial dataset."""
    results = rank_games([], player_count=3, max_time=60)
    self.assertEqual(results, [])

  def test_rank_games_invalid_input(self):
    """Invalid User Input: Non-positive player count or negative duration."""
    self.assertEqual(
        rank_games(INITIAL_GAMES, player_count=0, max_time=60), []
    )
    self.assertEqual(
        rank_games(INITIAL_GAMES, player_count=-2, max_time=60), []
    )
    self.assertEqual(
        rank_games(INITIAL_GAMES, player_count=3, max_time=-15), []
    )

  def test_rank_games_boundary_cases(self):
    """Boundary Case: Testing exact player counts (min/max) and exact duration limit."""
    # Min player count limit (Ticket to Ride min = 2)
    min_results = rank_games(INITIAL_GAMES, player_count=2, max_time=60)
    self.assertTrue(any(g["name"] == "Ticket to Ride" for g in min_results))

    # Max player count limit (Catan max = 4)
    max_results = rank_games(INITIAL_GAMES, player_count=4, max_time=60)
    self.assertTrue(any(g["name"] == "Catan" for g in max_results))

    # Exact time limit equality (Ticket to Ride takes exactly 45 mins)
    exact_time_results = rank_games(INITIAL_GAMES, player_count=2, max_time=45)
    self.assertTrue(
        any(g["name"] == "Ticket to Ride" for g in exact_time_results)
    )

    # Exceeded duration bound by 1 minute
    under_time_results = rank_games(INITIAL_GAMES, player_count=2, max_time=44)
    self.assertFalse(
        any(g["name"] == "Ticket to Ride" for g in under_time_results)
    )

  def test_add_game_valid(self):
    """Normal Scenario: Successfully add a new game to the collection."""
    test_games = list(INITIAL_GAMES)
    new_game = add_game(
        test_games, "Carcassonne", 2, 5, 35, ["tile-placement"]
    )

    self.assertEqual(new_game["name"], "Carcassonne")
    self.assertEqual(new_game["id"], 4)
    self.assertEqual(len(test_games), 4)

  def test_add_game_invalid_inputs(self):
    """Invalid Input: Empty name, invalid player range, or non-positive duration."""
    test_games = list(INITIAL_GAMES)

    # Empty game name
    with self.assertRaises(ValueError):
      add_game(test_games, "", 2, 4, 30, ["strategy"])

    # min_players > max_players
    with self.assertRaises(ValueError):
      add_game(test_games, "Invalid Range", 5, 2, 30, ["strategy"])

    # Duration <= 0
    with self.assertRaises(ValueError):
      add_game(test_games, "Zero Duration", 2, 4, 0, ["strategy"])


if __name__ == "__main__":
  unittest.main()