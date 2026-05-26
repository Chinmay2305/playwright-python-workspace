from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        user_data_dir="userdata",
        headless=False
    )
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.fill("textarea[name='q']", "Playwright Python")
    page.keyboard.press("Enter")
    page.wait_for_timeout(3000)
    page.screenshot(path="Full_Page.png", full_page=True)