# Build a game you can trust—with AI

This is a **self-paced, guided first lab**. Make one round of Rock, Paper, Scissors work, then show why you trust the result. You will agree on a short spec, guide an AI coding agent, use automatic checks, and review its work.

Start with **your GitHub copy → SSH clone → local AI project**. The steps below use **ChatGPT desktop in Codex mode**, terminal Git, and a browser. **VS Code is optional.** This path needs no API key, separate Codex CLI, or classroom demonstration.

**Try → Decide → Build → Check → Keep.** If you stop, return to this README at the last checkpoint you completed. [Visual overview](https://kaw393939.github.io/218_spec/).

## 1. Try the starter

**First, get the repo into your AI project.** Use your existing class SSH setup in macOS Terminal or Ubuntu/WSL on Windows. The agent will help check Python and prepare the app after you open the folder.

On [the starter](https://github.com/kaw393939/is218-rps-starter), choose **Use this template → Create a new repository**. Use your account, name it `my-rps`, choose **Public**, leave **Include all branches** off, and leave the optional Copilot prompt blank. Already made your copy? Open it and skip creating another.

In your projects folder, replace `YOUR-USERNAME` below. If you chose another repository name, replace `my-rps` too. **Run one command at a time; stop if one fails.** `pwd` must end in your repository's folder name, and both lines from `git remote -v` must identify **your copy** using `git@github.com:`.

```sh
git clone git@github.com:YOUR-USERNAME/my-rps.git
cd my-rps
pwd
git remote -v
```

In **ChatGPT desktop**, select **Codex** from the ChatGPT dropdown. Open this cloned folder as a **local project** with **⌘O on Mac / Ctrl+O on Windows**. Start a chat in that project, choose **Work in → This computer**, and leave **Worktree** off. On Windows, first follow the [one-time WSL app setup](https://kaw393939.github.io/218_spec/setup.html#windows-wsl).

Ask:

> Read README.md, AGENTS.md, and SPEC.md from this project. Confirm the folder. Briefly explain what I will build and what is already supplied. Guide me through setup one checkpoint at a time: verify the class Python, prepare the environment, run the starter checks, and help me open the unfinished game. Explain each step briefly as we go. Do not implement the rules, commit, or push yet.

**Connection checkpoint:** the agent names your cloned folder and explains the task from its files. It should not need you to upload or paste them. [Using another coding agent?](https://kaw393939.github.io/218_spec/setup.html#another-coding-agent)

Let it verify **Python 3.12.x**, prepare `.venv`, install the pinned requirements and Chromium, and run `.venv/bin/python check.py`. Ask it to explain errors and the smallest fix; [Python help](https://kaw393939.github.io/218_spec/setup.html#python-version) covers the class setup. Expect **PASS** at each check and **STARTER BASELINE ONLY**: the missing game rules are not verified yet.

When ready, use your original **class terminal**, still in the clone, to start the game:

```sh
.venv/bin/python run.py
```

Open the printed address, usually **http://127.0.0.1:5050**. Click a move: expect both choices and **“Starter: game rules not built yet.”** A missing winner is the task, not a failed setup. Leave this terminal running the game; code edits reload automatically. Use the AI project's separate terminal for checks and Git.

**Checkpoint:** your agent is connected to the clone, the starter checks pass, and you can see the game's unfinished notice. Stuck? [Setup help](https://kaw393939.github.io/218_spec/setup.html).

**Returning later?** In your class terminal, `cd` to this existing clone and run `.venv/bin/python run.py` again. Reopen the same project/chat in ChatGPT desktop and continue at your last checkpoint; do not clone or install again. If the game is already running, leave that server running.

## 2. Decide with your coding agent

Continue in this same project chat. Before asking AI, predict player **Rock** against computer **Paper** and say why. Then ask:

> Read AGENTS.md and SPEC.md. Explain RPS-001 and propose a short plan. Include valid and invalid cases, what to test as a unit, through a request, and in a real browser. Do not edit yet. Keep scoring for later.

Compare its answer with the nine-matchup table. A valid loss is a **positive** case; a missing or unsupported move is a **negative** case. Ask about anything you cannot explain. [Short introduction to the checks](https://kaw393939.github.io/218_spec/checks.html).

When you agree, ask:

> Save our agreed plan under “Agreed plan” in SPEC.md. Preserve the expected results. Do not edit the app yet.

Open **New tab → Terminal** in ChatGPT desktop. This terminal should be in your cloned folder. Keep using it for checks and Git:

```sh
pwd
cat SPEC.md
```

Confirm the path and saved plan. Setup and the baseline checks were completed in Step 1; keep using this same clone.

In **your GitHub repository → Issues → New issue**, create **“RPS-001: Play a round”**. Describe the scope and checks you agreed on; you can ask the agent for a short draft. Review before posting. Give its URL to the agent and ask it to put that link in **SPEC.md → Work record**.

**Checkpoint:** `SPEC.md` contains your agreed plan and issue link. No transfer between AI apps or manual code copying is needed.

## 3. Build and let AI check first

In the app's terminal:

```sh
git status --short --branch
git switch -c rps-001
```

Before switching, expect the `main` branch and your intended `M SPEC.md` edit. That uncommitted plan carries onto the new `rps-001` branch. If the branch exists, use `git switch rps-001`.

In the **same AI chat**, ask:

> Compare our saved plan with the code and supplied fixtures. Explain conflicts or needed changes before editing; do not restart the whole plan. If it fits, implement RPS-001 and its agreed tests. Run .venv/bin/python check.py, review the diff against SPEC.md, and fix problems without weakening checks. Report actual results and remaining human checks. Do not commit or push.

Review file/command approval requests. The prepared checks use **Black** for formatting, **Pylint** for Python analysis, and **pytest** for behavior, including a small real-browser journey. The agent should add nine rule cases, a real request/result check, and a browser round with replay—not repeat every case through the browser.

**Checkpoint:** AI reports actual commands/results and what remains for you. Passing unchanged starter tests alone is not enough.

## 4. Check and give feedback

Open the server's printed address again, then choose a move. Play several rounds. Do both choices and the result make sense? Can you play again? Try Tab and Enter too; in Safari, use Option+Tab if Tab skips buttons.

In the app's terminal:

```sh
.venv/bin/python check.py
git status --short
git diff
cat tests/test_game.py
cat tests/e2e/test_round.py
```

Press `q` if Git opens a scrolling view. `??` means a new, untracked file: `git diff` does not show it yet, so inspect the two test files above too. Find the assertion for your predicted matchup and compare it with the spec; check that the browser test plays again using real rules. You can open files in the app with **⌘P / Ctrl+P**, or optionally inspect them in VS Code.

Tell the agent what you actually did and saw. For a mismatch, describe the action, expected result, and observed result; ask for a focused fix and retest. [Worked failure example](https://kaw393939.github.io/218_spec/checks.html#when-a-check-fails) shows how.

During fixes, `.venv/bin/python check.py --fast` skips the browser. Use the full command before review and the PR. For formatting, `.venv/bin/python -m black *.py tests` applies the shared style; inspect its edits. Do not remove meaningful assertions or disable checks just to pass.

Ask the agent to replace starter status in **SPEC.md → Work record** with actual checks, your browser observations, and real code/test links. Preserve the plan and issue. Do not record checks nobody performed.

**Checkpoint:** you can connect one requirement to its code and a meaningful test. You have tried the result yourself.

## 5. Keep the reviewed change

Expect `game.py`, `tests/test_game.py`, `tests/e2e/test_round.py`, and `SPEC.md`. Ask about other changed files before keeping them.

```sh
git add game.py tests/test_game.py tests/e2e/test_round.py SPEC.md
git diff --cached
git commit -m "RPS-001: play a round"
git push -u origin rps-001
```

In **your GitHub repository → Pull requests → New pull request**, use base `main` and compare `rps-001`. Describe the result and actual checks; add **`Closes #N`** with your issue number. In **Files changed**, verify the added tests use real rules rather than just the supplied stubs. Wait for **Python checks** to pass, then merge when it matches the spec.

**Done:** the game works locally, the PR is merged, its issue is closed, and the spec links to code and actual checks. Return to the **class terminal running the game** and stop it with Ctrl+C. No website deployment or extra reflection document is required.

**Next, with less guidance:** [choose another small feature](NEXT.md). Try first-to-two scoring, explain why a move won, or personalize the game. Choose one, write your own short request and test plan, and use a separate issue/PR.
