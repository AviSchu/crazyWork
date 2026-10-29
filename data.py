INITIAL_GAMES = [
    {
        "id": 1,
        "name": "Catan",
        "min_players": 3,
        "max_players": 4,
        "duration": 60,
        "tags": ["strategy", "trading"],
    },
    {
        "id": 2,
        "name": "Codenames",
        "min_players": 4,
        "max_players": 8,
        "duration": 15,
        "tags": ["party", "words"],
    },
    {
        "id": 3,
        "name": "Ticket to Ride",
        "min_players": 2,
        "max_players": 5,
        "duration": 45,
        "tags": ["family", "strategy"],
    },
]


def add_game(games_list, name, min_p, max_p, duration, tags):
  if not name or min_p > max_p or duration <= 0:
    raise ValueError("Invalid game parameters.")
  new_id = max([g["id"] for g in games_list], default=0) + 1
  game = {
      "id": new_id,
      "name": name,
      "min_players": int(min_p),
      "max_players": int(max_p),
      "duration": int(duration),
      "tags": tags,
  }
  games_list.append(game)
  return game