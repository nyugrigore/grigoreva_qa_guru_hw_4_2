from selene import browser, have


def test1_source_found():
    browser.open('https://www.google.com/')
    browser.element('[name="q"]').type('Selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


