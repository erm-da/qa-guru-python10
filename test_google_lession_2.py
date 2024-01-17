from selene import browser, have, be


def test_google_search_with_valid_result():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google_search_without_results():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('OOOOBBBBAAAAHHHHHHIIIII').press_enter()
    browser.element(('[id="botstuff"]')).should(have.text("ничего не найдено."))