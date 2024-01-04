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
        await page.goto("https://demoqa.com/radio-button")

        # Actions
        await page.locator("#yesRadio").set_checked(True, force=True)
        await page.screenshot(path="screenshots/radios.png")

        # Assertions
        await expect(page.locator(".text-success")).to_have_text("Yes")

        # Stop tracing
        await context.tracing.stop(path="logs/radios-trace.zip")

        # Closing browser
        await browser.close()


asyncio.run(main())
