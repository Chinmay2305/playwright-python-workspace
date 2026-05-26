from playwright.sync_api import Page

def test_login(page: Page):
    page.goto("https://qa.aerfinity.acumenaviation.in/")
    page.fill("//input[@id='email']", "support@acumen.aero")
    page.fill("//input[contains(@id,'password')]", "Acumen@123")
    page.click("//button[contains(@class, 'MuiButtonBase-root') and contains(@class, 'MuiButton-containedPrimary') and contains(@class, 'MuiButton-fullWidth')]")
    page.wait_for_timeout(3000)