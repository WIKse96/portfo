import time

from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.by import By

from pagesObj.SaleProductPage import OneProductSale

class SaleProductActions(OneProductSale):

    def __init__(self, driver):
        self.driver = driver

    def addToCartClick(self):
        self.addToCartBtn.click_button()
        self.driver.get('https://www.seart.pl/checkout/cart/')
        print(specialPriceSale)



