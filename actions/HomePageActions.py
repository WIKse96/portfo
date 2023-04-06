import time
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.by import By

from pagesObj.HomePage import HomePage

class HomePageActions(HomePage):

    def __init__(self, driver):
        self.searchIcon = None
        self.driver = driver

    # button click

    def loginBtnClick(self):
        self.loginBtn.click_button()
        assert "możliwość przechowywania wielu adresów dostawy" in self.driver.page_source


    def searchTest(self):
        pass

    def menu_homepge(self):
        action = AC(self.driver)
        action.move_to_element(self.menu_meble)
        action.perform()
        action.click(self.toaletki_menu)
        action.perform()

        pass