"""RPS-001's literal rule examples and a request through the real rules."""

import pytest

import app as web
from game import determine_winner


@pytest.mark.unit
@pytest.mark.parametrize(
    ("player", "computer", "expected"),
    [
        ("rock", "rock", "tie"),
        ("rock", "paper", "lose"),
        ("rock", "scissors", "win"),
        ("paper", "rock", "win"),
        ("paper", "paper", "tie"),
        ("paper", "scissors", "lose"),
        ("scissors", "rock", "lose"),
        ("scissors", "paper", "win"),
        ("scissors", "scissors", "tie"),
    ],
)
def test_matchup(player, computer, expected):
    """Every valid matchup matches SPEC.md from the player's perspective."""
    assert determine_winner(player, computer) == expected


@pytest.mark.integration
def test_real_round_displays_player_loss(monkeypatch):
    """A real request connects the predicted Rock/Paper loss to the page."""
    monkeypatch.setattr(web.random, "choice", lambda _moves: "paper")
    with web.app.test_client() as client:
        response = client.post("/", data={"move": "rock"})

    page = response.get_data(as_text=True)
    assert response.status_code == 200
    assert 'data-outcome="lose"' in page
    assert "Computer wins" in page
    assert "You chose" in page and "Computer chose" in page
    assert '<p class="choice-value">Rock ' in page
    assert '<p class="choice-value">Paper ' in page
    assert "game rules not built yet" not in page
