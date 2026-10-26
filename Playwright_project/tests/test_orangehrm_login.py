import re
from playwright.sync_api import Page
from pages.orangehrm_login import Loginpage
from pages.orangehrm_homepage import Homepage

def test1(page: Page) -> None:
    login_page = Loginpage(page)
    home_page = Homepage(page)
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()

    # expect(home_page.is_upgrade_button_visible()).to_be_true()
    home_page.is_upgrade_button_visible()
    home_page.click_performance()
    home_page.click_dashboard()
    