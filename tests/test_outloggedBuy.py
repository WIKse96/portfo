from seleniumpagefactory.Pagefactory import PageFactory

from actions.Category_actions import CategoryActions
from pagesObj.CategoryPage import CategoryPage
from utilities.BaseClass import BaseClass
from pagesObj.HomePage import HomePage
from actions.HomePageActions import HomePageActions


# @pytest.mark.usefixtures("setup") - dziedziczone z BaseClass
class TestOne(BaseClass):

    def goHome(self):
        self.driver.get("https://www.seart.pl/")

    def test_OutloggedBuy(self, setup):
        homePage = HomePage(self.driver)
        home_page_actions = HomePageActions(self.driver)
        homePage.homePage_assertions()

        home_page_actions.loginBtnClick()
        home_page_actions.searchTest()
        home_page_actions.menu_homepge()
    def test_Collection(self):
        category_page = CategoryPage(self.driver)
        # category_page_actions = CategoryActions(self.driver)

        category_page.catPage_assertions()

