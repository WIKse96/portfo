import time

from selenium.webdriver.common.by import By

from pagesObj.CollectionPage import CollectionPage

class CollectionPageActions:
    def __init__(self, driver):
        self.driver = driver
        self.addedToCart_info = None
        self.showCartBtn = None

    def addToCart_collection(self):
        btns = self.driver.find_elements(*CollectionPage.addToCartBtn_collection)
        btns[2].click()
        time.sleep(3)
        self.addedToCart_info = (By.XPATH, "//div[@class='pupup-suc-added-to-your-bag']")

    def showCart_frompopup(self):
        self.showCartBtn = (By.XPATH, "//button[text()='Zobacz Koszyk']")
        self.driver.find_element(self.showCartBtn).click()
        time.sleep(3)
