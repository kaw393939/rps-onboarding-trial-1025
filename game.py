"""Rules for one independent Rock, Paper, Scissors round. See SPEC.md."""


def determine_winner(player: str, computer: str) -> str:
    """Return 'win', 'lose', or 'tie' from the player's perspective.

    The supplied web page accepts only 'rock', 'paper', and 'scissors'.
    The expected results are recorded in SPEC.md.
    """
    if player == computer:
        return "tie"
    beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    if beats[player] == computer:
        return "win"
    return "lose"
