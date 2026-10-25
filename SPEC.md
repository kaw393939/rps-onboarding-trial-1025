# Rock, Paper, Scissors

## RPS-001: Play a round

**Purpose:** one person plays a quick round against the computer.

- Choose rock, paper, or scissors. The computer chooses one move for that round.
- Display both choices and the result: **You win!**, **Computer wins**, or **It’s a tie**.
- Choosing again starts an independent round. No score or saved history.
- Keep the supplied interface and server. Name/color changes can wait until the rules work.

### Expected results

Results are from the **player’s perspective**. `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie`. Inputs are the lowercase moves below; the supplied server rejects other choices.

| Player | Computer | Expected return |
| --- | --- | --- |
| rock | rock | tie |
| rock | paper | lose |
| rock | scissors | win |
| paper | rock | win |
| paper | paper | tie |
| paper | scissors | lose |
| scissors | rock | lose |
| scissors | paper | win |
| scissors | scissors | tie |

### Agreed plan

- Keep the supplied server/interface. Implement equal moves as tie, the three winning pairs as win, and the remaining valid pairs as lose in game.py. The server already rejects invalid or missing moves.
- Add all nine literal outcomes as deterministic unit cases in tests/test_game.py. Include a real POST with player Rock and computer Paper: it must show both choices and Computer wins. Reuse the supplied negative request cases.
- In tests/e2e/test_round.py, fix only the computer choice to Scissors. Play Rock for a win, then Paper for a loss in the same browser journey using the real rule function and supplied live_server/page fixtures.
- Run the full check.py and review the diff before browser review. Keep scoring, styling, dependencies, and shared checks unchanged.

### Checks

Before coding, agree this small test plan with AI:

| Level | Cases and evidence |
| --- | --- |
| Unit — positive | All nine literal expected results above, including valid losses and ties. |
| Integration — positive | A submitted round uses the real rule function and displays both choices and the correct result. Fix the computer choice for the test. |
| Integration — negative | Reuse supplied missing/unsupported-move tests: HTTP 400 and a helpful explanation, without calling the rules. A crash is not the intended result. |
| E2E — positive | Add a real-browser round and replay in tests/e2e/test_round.py using the supplied live_server/page fixtures. Fix only the computer choice; use real rules and real HTTP. |

Use `unit`, `integration`, and `e2e` pytest markers. Run `.venv/bin/python check.py` for Black, Pylint, fast tests, and browser checks; then review the diff. Keep shared settings and meaningful assertions intact. The student still plays, inspects a rule and its test, and gives feedback. Browser automation does not establish every aspect of usability or application performance.

### Work record

- Issue: [RPS-001: Play a round](https://github.com/kaw393939/rps-onboarding-trial-1025/issues/1).
- Implementation: [game.py](game.py) implements one round. [Rule/request tests](tests/test_game.py) cover the nine literal outcomes and a real Rock/Paper loss; [browser tests](tests/e2e/test_round.py) cover a real win and replay. Existing negative request cases remain in [shell tests](tests/test_shell.py).
- Checks: `.venv/bin/python check.py` passed Black, Pylint, 22 non-browser cases and 2 Chromium cases. Computer Use browser review observed Rock/Rock tie, Paper/Rock win, keyboard Tab/Enter Rock/Scissors win, and Scissors/Rock loss with replay. These are agent-enacted observations, not a human student review. No desktop-app interaction was tested.
