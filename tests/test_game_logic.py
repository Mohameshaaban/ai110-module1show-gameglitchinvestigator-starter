from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    hint_message_for_outcome,
    reset_game_state,
)

def test_winning_guess():
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_hint_message_mapping():
    assert hint_message_for_outcome("Win") == "🎉 Correct!"
    assert hint_message_for_outcome("Too High") == "📉 Go LOWER!"
    assert hint_message_for_outcome("Too Low") == "📈 Go HIGHER!"


def test_reset_game_state_resets_values_and_secret_range():
    low, high = get_range_for_difficulty("Easy")
    state = reset_game_state(low, high)

    assert state["attempts"] == 0
    assert state["score"] == 0
    assert state["status"] == "playing"
    assert state["history"] == []
    assert low <= state["secret"] <= high
