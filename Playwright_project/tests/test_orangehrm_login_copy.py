import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("button", name="Upgrade")).to_be_visible()
    page.get_by_role("link", name="Dashboard").click()
    page.get_by_role("link", name="Recruitment").click()

    