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
        await page.goto("https://demoqa.com/buttons")

        # Double Click
        await page.locator("#doubleClickBtn").dblclick()
        await expect(page.locator("#doubleClickMessage")).to_have_text("You have done a double click")
        await page.screenshot(path="screenshots/doubleClick.png")

        # Right Click
        await page.locator("#rightClickBtn").click(button="right")
        await expect(page.locator("#rightClickMessage")).to_have_text("You have done a right click")
        await page.screenshot(path="screenshots/rightClick.png")

        # Dynamic Click
        await page.get_by_role("button", name="Click Me", exact=True).click()
        await expect(page.locator("#dynamicClickMessage")).to_have_text("You have done a dynamic click")
        await page.screenshot(path="screenshots/dynamicClick.png")

        # Stop tracing
        await context.tracing.stop(path="logs/buttons-trace.zip")

        # Closing browser
        await browser.close()

asyncio.run(main())
