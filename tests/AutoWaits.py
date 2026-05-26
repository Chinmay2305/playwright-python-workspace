from playwright.sync_api import Page

def test_auto_wait_example(page:Page):
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")

    page.click("button")

    text=page.inner_text("#finish")

    print("Text found:", text)

    assert "Hello World!" in text