import pytest
from playwright.sync_api import Page, expect

def test_health_check(page: Page):
    page.goto("https://www.saucedemo.com/inventory.html")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_add_items_to_cart(page: Page):
    page.goto("https://www.saucedemo.com/inventory.html")

    page.locator(".inventory_item:nth-child(1) button").click()
    page.locator(".inventory_item:nth-child(2) button").click()
    page.locator(".inventory_item:nth-child(3) button").click()

    expect(page.locator(".shopping_cart_badge")).to_have_text("3")

def test_cart_page(page: Page):
    page.goto("https://www.saucedemo.com/cart.html")

    expect(page.locator(".cart_item")).to_have_count(3)

def test_checkout_journey(page: Page):
    page.goto("https://www.saucedemo.com/cart.html")
    page.locator("#checkout").click()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

    page.locator("#first-name").fill("John")
    page.locator("#last-name").fill("Doe")
    page.locator("#postal-code").fill("12000")
    page.locator("#continue").click()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    expect(page.locator(".cart_item")).to_have_count(3)

    page.locator("#finish").click()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    expect(page.locator(".complete-text")).to_have_text("Your order has been dispatched, and will arrive just as fast as the pony can get there!")
