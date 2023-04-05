import time
from selenium.webdriver.common.action_chains import ActionChains

from pagesObj.HomePage import HomePage


class HomePageActions:
    def __init__(self, driver):
        self.driver = driver
        self.newsletterMailFailed = 'uczeSieSeleniumNaWaszejStronie@ops.pl'

    strToSearch = 'dzbanek'

    def searchTest(self):
        self.driver.find_element(*HomePage.searchIcon).click()
        self.driver.find_element(*HomePage.searchInput).send_keys(*HomePageActions.strToSearch)

        for element in self.driver.find_elements(*HomePage.searchLis):
            if element.text.lower() == (HomePageActions.strToSearch).lower():
                print('=======OK=======')
                break
            else:
                print("Brak takich produktów")

    def newsLetterTestCorrect(self):
        self.driver.find_element(*HomePage.newsletterMain)
        self.driver.find_element(*HomePage.newsletterInput).send_keys(self.newsletterMailFailed)
        self.driver.find_element(*HomePage.newsletterBtn).click()
        # asercja czy poprawnie email zapisany
        time.sleep(1)
        assert 'Dziękujemy za twoją subskrypcję' in self.driver.page_source
    def newsLetterTestNoCorrect(self):
        self.driver.find_element(*HomePage.newsletterMain)
        self.driver.find_element(*HomePage.newsletterInput).send_keys(self.newsletterMailFailed)
        self.driver.find_element(*HomePage.newsletterBtn).click()
        # asercja czy poprawnie email zapisany
        time.sleep(1)
        assert 'This email address is already subscribed.' in self.driver.page_source
    def menuTest(self):

        menu_collection = self.driver.find_element(*HomePage.menuCollection)
        menu_col_lubliana = self.driver.find_element(*HomePage.menuColLubliana)

        actions = ActionChains(self.driver)
        actions.move_to_element(menu_collection).perform()
        actions.move_to_element(menu_col_lubliana).click().perform()
