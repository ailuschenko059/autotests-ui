from playwright.sync_api import sync_playwright, expect, Page
import pytest



def test_empty_courses_list(chromium_page_with_state: Page):

    check_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(check_title).to_be_visible()
    expect(check_title).to_have_text('Courses')

    check_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(check_icon).to_be_visible()

    check_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(check_text).to_be_enabled()
    expect(check_text).to_have_text('There is no results')

    check_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(check_description).to_be_enabled()
    expect(check_description).to_have_text('Results from the load test pipeline will be displayed here')



