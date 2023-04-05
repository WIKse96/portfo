import time

from PageActions.HomePage_actions import HomePageActions
from PageActions.Collection_actions import CollectionPageActions
from pagesObj.CollectionPage import CollectionPage
from utilities.BaseClass import BaseClass
from pagesObj.HomePage import HomePage


# @pytest.mark.usefixtures("setup") - dziedziczone z BaseClass
class TestOne(BaseClass):

    def test_OutloggedBuy(self):
        # tworzenie obiektów
        self.driver.get("https://porcelana.pl/")
        homePageObj = HomePage(self.driver)
        homePageObj.goHome()

        homePageObj.assertions()

    def test_homePage(self):
        homePageActions = HomePageActions(self.driver)

        homePageActions.searchTest()
        homePageActions.newsLetterTestCorrect()
        homePageActions.newsLetterTestNoCorrect()
        homePageActions.menuTest()
    def test_collectionPage(self):
        colectionPage = CollectionPage(self.driver)
        collectionPageActions = CollectionPageActions(self.driver)

        colectionPage.assertions()
        collectionPageActions.addToCart_collection()
        collectionPageActions.showCart_frompopup()

