import os
from playwright.sync_api import sync_playwright

def verify_ui():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get absolute path to the HTML file
        cwd = os.getcwd()
        file_path = f"file://{cwd}/airdrop-calculator.html"

        print(f"Navigating to {file_path}")
        page.goto(file_path)

        # Take a screenshot of the whole page
        page.screenshot(path="verification/airdrop_ui.png", full_page=True)
        print("Screenshot saved to verification/airdrop_ui.png")

        browser.close()

if __name__ == "__main__":
    verify_ui()
