def rank_games(records, player_count, max_time, preferred_tag=None):
  """Filters games by constraints and ranks them by preference match."""
  if not records or player_count <= 0 or max_time <= 0:
    return []

  filtered = []
  for game in records:
    # Constraint check: players and duration
    if (
        game["min_players"] <= player_count <= game["max_players"]
        and game["duration"] <= max_time
    ):
      score = 0
      # Core logic: reward matching preferred tag and shorter duration efficiency
      if preferred_tag and preferred_tag.lower() in [
          t.lower() for t in game["tags"]
      ]:
        score += 10
      # Tie breaker: closer duration to available time or simpler metrics
      filtered.append((score, game))

  # Sort by score descending, tie-break by shorter duration
  filtered.sort(key=lambda x: (-x[0], x[1]["duration"]))
  return [g for score, g in filtered]