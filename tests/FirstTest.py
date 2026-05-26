from playwright.sync_api import Page

def test_google(page: Page):
    page.goto("https://www.google.com")
    page.fill("textarea[name='q']", "Playwright Python")
    page.press("textarea[name='q']", "Enter")
    page.wait_for_timeout(3000)