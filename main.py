from data import INITIAL_GAMES, add_game
from logic import rank_games


def main():
  games = INITIAL_GAMES
  while True:
    print("\n--- Game Night Organizer ---")
    print("1. Search & Get Recommendations")
    print("2. Add New Game")
    print("3. Exit")
    choice = input("Choose an option (1-3): ").strip()

    if choice == "1":
      try:
        p_count = int(input("Enter number of players: "))
        max_t = int(input("Enter max duration in minutes: "))
        tag = input("Enter preferred tag (or leave blank): ").strip()

        results = rank_games(games, p_count, max_t, tag)
        print(f"\nFound {len(results)} matching games:")
        for g in results:
          print(
              f"- {g['name']} ({g['min_players']}-{g['max_players']}"
              f" players, {g['duration']} mins) Tags: {', '.join(g['tags'])}"
          )
      except ValueError:
        print("Error: Please enter valid numbers for players and time.")

    elif choice == "2":
      name = input("Game name: ").strip()
      try:
        min_p = int(input("Min players: "))
        max_p = int(input("Max players: "))
        dur = int(input("Duration (mins): "))
        tags = input("Tags (comma separated): ").strip().split(",")
        tags = [t.strip().lower() for t in tags if t.strip()]

        add_game(games, name, min_p, max_p, dur, tags)
        print(f"Successfully added {name}!")
      except ValueError as e:
        print(f"Invalid input: {e}")

    elif choice == "3":
      print("Goodbye!")
      break
    else:
      print("Invalid choice, please select 1, 2, or 3.")


if __name__ == "__main__":
  main()