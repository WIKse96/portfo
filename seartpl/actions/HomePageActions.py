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
    def searchDesktop(self):
        self.search_bar.set_text(self.texts_to_search['search_Home_Page'])
        self.search_btn.click_button()
        highlighted_links = self.driver.find_elements(By.XPATH, "//span[@class='searchindex-highlight']")
        for idx, highlighted_link in enumerate(highlighted_links):
            print(idx, highlighted_link.text)
            assert 'Komoda' == highlighted_link.text
            break
        print('============================ OK - searcjDesktop ============================')