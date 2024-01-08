import pytest
from playwright.sync_api import Browser, expect


@pytest.fixture(scope="session")
def create_context(browser: Browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("")

    expect(page).to_have_url("")

    context.storage_state(path=".auth/auth.json")
    context.close()


@pytest.fixture(scope="function", autouse=True)
def context(create_context, browser: Browser):
    context = browser.new_context(storage_state=".auth/auth.json")
    yield context
    context.close()
