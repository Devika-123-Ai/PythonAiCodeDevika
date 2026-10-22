import re
from playwright.sync_api import expect


def test_google(page):
    page.wait_for_timeout(3000)
    page.goto("https://www.google.com/ncr")
    try:
        page.get_by_role("button", name="I agree").click()
    except:
        print("No popups/no cookies")
    page.get_by_role("combobox", name="Search").fill("playwright")
    page.keyboard.press("Enter")
    expect(page).to_have_title(re.compile("playwright",re.IGNORECASE))
