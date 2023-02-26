from selene import browser, have


def test1_source_found(browser_configs):

    browser.element('[name="q"]').type('Selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test2_source_not_found(browser_configs):
    browser.open('https://www.google.com/')
    browser.element('[name="q"]').type('оврыаорыаол').press_enter()
    browser.element('.card-section').should(have.text('ничего не найдено.'))
