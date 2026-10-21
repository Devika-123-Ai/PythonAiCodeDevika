from playwright.sync_api import Page ,expect

def test_verifyPageurl(page:Page):
    page.goto("https://www.google.com/")

    myurl = page.url
    print("Url of the application",myurl)

    expect (page).to_have_url(myurl)

def test_verifyTitle(page:Page):
    page.goto("https://www.google.com/")

    mytitle = page.title()
    print("Page title is ",mytitle)
    expect (page).to_have_title(mytitle)
