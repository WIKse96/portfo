from selenium.webdriver.common.by import By

class CollectionPage():
    def __init__(self, driver):
        self.driver = driver

    productList = (By.XPATH, "//div[@class='product details product-item-details']")
    collection_filter = (By.XPATH, "//div[normalize-space()='Kolekcja']")
    addToCartBtn_collection = (By.XPATH, "//button[@type='submit'][@title='Dodaj do koszyka']")


    def assertions(self):
        assert self.driver.find_elements(*CollectionPage.productList)
        print('Ilość produktów na karcie:',len(self.driver.find_elements(*CollectionPage.productList)))
        assert self.driver.find_element(*CollectionPage.collection_filter)
