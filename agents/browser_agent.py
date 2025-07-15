from playwright.sync_api import sync_playwright

def simulate_browser_actions():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto("https://example.com")
            title = page.title()
            browser.close()
            return f"Visited site. Page title: {title}"
    except Exception as e:
        return f"❌ Browser automation failed: {e}"
