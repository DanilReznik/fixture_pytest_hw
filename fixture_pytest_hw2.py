from selene import browser, be, have


def test_search(browser_set):

    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search2(browser_set):

    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('asd12312312dsag').press_enter()
    browser.element('[id="search"]').should(have.text('По запросу asd12312312dsag ничего не найдено'))


