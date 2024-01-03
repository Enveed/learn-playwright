import asyncio
from playwright.async_api import async_playwright, expect


async def main():
    async with async_playwright() as p:
        # Launch Browser
        browser = await p.chromium.launch(headless=False)
        # Create a new independent browser session
        context = await browser.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        # Create a new page in browser context
        page = await context.new_page()

        await page.set_viewport_size({"width": 1920, "height": 1080})
        await page.goto("https://demoqa.com/checkbox")

        # Actions
        await page.locator('label[for="tree-node-home"]').check()
        await page.screenshot(path="screenshots/checkboxes.png")

        # Assertions
        await page.locator('label[for="tree-node-home"]').is_checked() is True
        await expect(page.locator("#result")).to_have_text("You have selected :homedesktopnotescommandsdocumentsworkspacereactangularveuofficepublicprivateclassifiedgeneraldownloadswordFileexcelFile")

        # Stop tracing
        await context.tracing.stop(path="logs/checkboxes-trace.zip")

        # Closing browser
        await browser.close()

asyncio.run(main())
