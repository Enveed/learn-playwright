import pytest
from playwright.sync_api import Browser, expect


@pytest.fixture(scope="session")
def create_context(browser: Browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com")

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("input[type='submit']").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    context.storage_state(path=".auth/auth.json")
    context.close()


@pytest.fixture(scope="function", autouse=True)
def context(create_context, browser: Browser):
    context = browser.new_context(storage_state=".auth/auth.json")
    yield context
    context.close()
