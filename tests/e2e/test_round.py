"""RPS-001 round and replay against the real rules over local HTTP."""

import pytest
from playwright.sync_api import Page, expect

import app as web

pytestmark = pytest.mark.e2e


def test_round_and_replay(page: Page, live_server, monkeypatch):
    """Fix only randomness, then verify two independent rounds in Chromium."""
    monkeypatch.setattr(web.random, "choice", lambda _moves: "scissors")
    page.goto(live_server)
    expect(page.get_by_role("status")).to_have_count(0)

    page.get_by_role("button", name="Rock", exact=True).click()
    expect(page.get_by_role("heading", name="You win!", exact=True)).to_be_visible()
    expect(page.locator('[data-outcome="win"]')).to_be_visible()
    choices = page.get_by_label("This round’s choices")
    expect(choices.locator(".choice-value").nth(0)).to_contain_text("Rock")
    expect(choices.locator(".choice-value").nth(1)).to_contain_text("Scissors")

    page.get_by_role("button", name="Paper", exact=True).click()
    expect(
        page.get_by_role("heading", name="Computer wins", exact=True)
    ).to_be_visible()
    expect(page.locator('[data-outcome="lose"]')).to_be_visible()
    expect(choices.locator(".choice-value").nth(0)).to_contain_text("Paper")
    expect(choices.locator(".choice-value").nth(1)).to_contain_text("Scissors")
    expect(page.get_by_role("status")).to_have_count(0)
