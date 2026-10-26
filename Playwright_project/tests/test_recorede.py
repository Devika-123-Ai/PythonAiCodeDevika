import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.locator("body").click()
    page.locator("body").click()
    page.locator("body").click()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("rama")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("12345")
    page.get_by_role("button", name="Login").click()
    expect(page.locator("form")).to_contain_text("Username")
