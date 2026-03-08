def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str, low: int, high: int):

    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    if value < low or value > high:
        return False, None, f"Guess must be between {low} and {high}."

    return True, value, None


def check_guess(guess, secret):

    if guess == secret:
        return "Win"

    if guess > secret:
        return "Too High"

    return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        points = max(100 - attempt_number * 10, 10)
        return current_score + points

    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
