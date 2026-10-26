

from playwright.sync_api import Page,expect
 
def test_builtin_locators(page:Page):
    page.goto("https://www.nopcommerce.com/")
    page.wait_for_timeout(5000)
    # page.get_by_alt_text()
    logo = page.get_by_alt_text("nopCommerce")
    expect(logo).to_be_visible()
    
    # page.get_by_text()
    page.goto("https://www.nopcommerce.com/en?srsltid=AYCX9vL3OOU_uzNaroVxwqhhE_bnuIQwGLsI5xT2syuApOpLSIxXRViH")
    page.wait_for_timeout(5000)
    test1 = page.get_by_text("Why nopCommerce")
    expect(test1).to_be_visible()
    
    # page.get_by_role()
    page.goto("https://www.nopcommerce.com/en?srsltid=AYCX9vI3dc7P_p_prnhe3iYYzRDBJv1ABeVs0xnIZNmpWCoy6znhb2mG")
    page.wait_for_timeout(5000)
    test2 = page.get_by_role ("link",name="Get started")
    expect(test2).to_be_visible()
        
    
    page.close()

     