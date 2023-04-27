import time

from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory



class CategoryPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    # Locators
    locators = {
        'loginBtn': ('xpath', "//a[@title='Zaloguj']")
    }
    products = (By.XPATH, '//div[@class="item-area"]')



# assertios
    def catPage_assertions(self):
        time.sleep(3)
        print(len(self.driver.find_elements(*CategoryPage.products)))
        # assert self.driver.opinionsBannerSqr.visibility_of_element_located()
        print("========================OK - catPage_assertions ========================")
