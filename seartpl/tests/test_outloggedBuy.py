from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory

from actions.Category_actions import CategoryActions
from pagesObj.CategoryPage import CategoryPage
from utilities.BaseClass import BaseClass
from pagesObj.HomePage import HomePage
from actions.HomePageActions import HomePageActions
from pagesObj.Product import Products
from actions.ProductActions import ProductActions


# @pytest.mark.usefixtures("setup") - dziedziczone z BaseClass
class TestOne(BaseClass):

    def goHome(self):
        self.driver.get("https://www.seart.pl/")

    def test_OutloggedBuy(self, setup):
        #ODKOMENTOWAĆ DO TESTÓW
        
        
        # homePage = HomePage(self.driver)
        # home_page_actions = HomePageActions(self.driver)
        # homePage.homePage_assertions()

        # home_page_actions.loginBtnClick()
        # home_page_actions.searchTest()
        # home_page_actions.menu_homepge()
        pass
    def test_Collection(self):
        #ODKOMENTOWAĆ DO TESTÓW
        # category_page = CategoryPage(self.driver)
        # category_page_actions = CategoryActions(self.driver)

        # category_page.catPage_assertions()
        pass
    def test_search(self):
        #ODKOMENTOWAĆ DO TESTÓW
        # self.goHome()
        # homePage = HomePageActions(self.driver)
        # homePage.searchDesktop()
        pass

    def test_groupedBuy(self):
        # self.goHome()
        pass

    def test_simpleBuy(self):
        #ODKOMENTOWAĆ DO TESTÓW
        self.goHome()
        product = Products(self.driver)
        productActions = ProductActions(self.driver)


        product.goSimpleProduct()

        product.SimpleProduct_assertions()
        productActions.addToCartClick()
        productActions.goToCart()
        productActions.goToCheckout()
        productActions.fillOutForm()

    def test_simpleWithCustomOptionsBuy(self):
        #ODKOMENTOWAĆ DO TESTÓW
        # self.goHome()
        pass
