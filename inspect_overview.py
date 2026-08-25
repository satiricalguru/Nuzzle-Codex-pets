from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1440, "height": 1000})
    page.goto("http://127.0.0.1:4173", wait_until="networkidle")
    page.screenshot(path="/tmp/nuzzle-overview.png", full_page=True)
    browser.close()
