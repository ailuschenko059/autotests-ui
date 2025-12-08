from pickle import FALSE

import pytest
from playwright.sync_api import sync_playwright, Page, Playwright,expect


@pytest.fixture()
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()


@pytest.fixture(scope="session", autouse=FALSE)
def initialize_browser_state(playwright: Playwright) -> Page:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        playwright = context.new_page()
        playwright.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = playwright.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        username_input = playwright.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        password_input = playwright.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        registration_button = playwright.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        context.storage_state(path="browser-state.json")


@pytest.fixture(scope="function")
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        playwright = context.new_page()
        playwright.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        return playwright


