from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
class ProductsSale(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        'h1Sales': ('xpath', "//h1[contains(text(),'Wyprzedaż mebli drewnianych')]"),
        'productNameh2':('xpath', "//h2[@class='product-name']"),
        'promoLabel':('xpath', "//div[@class='etykieta_promocja']"),
        'szafka':('xpath', "//a[@title='Drewniana Szafka RTV Country Limited 17 - WYPRZEDAŻ']"),
        'newPrice':('xpath', "//span[@id='product-price-18571']"),
        'oldPrice':('xpath', "//span[@id='old-price-18571']"),
        'descWrapper':('xpath', "//div[@class='description-wrapper']"),
        'prodToOpen': ('xpath', "//img[@alt='Drewniana Szafka RTV ']")

    }

    def Sale_assertions(self):
        assert self.h1Sales.visibility_of_element_located()
        assert self.productNameh2.element_to_be_clickable()
        ProductNameh2 = self.get_elements(By.XPATH, self.locators['productNameh2'][1])
        PromoLabel = self.get_elements(By.XPATH, self.locators['promoLabel'][1])

        #czy ilosc produktow z etykieta == ilości produktów w kategorii
        assert len(ProductNameh2) == len(PromoLabel)
        newPrice_str = self.newPrice.text[:-6].replace(" ", "")
        oldPrice_str = self.oldPrice.text[:-6].replace(" ", "")
        newPrice_int = int(newPrice_str)
        oldPrice_int = int(oldPrice_str)
        assert oldPrice_int > newPrice_int

        self.create_dictionary()





    def get_elements(self, by, locator):
        return self.driver.find_elements(by, locator)

    def create_dictionary(self):
        #boxy z ceną, które zawierają obecną cenę i przeceniona
        dictionary = {}
        descWrappers = self.get_elements(By.XPATH, self.locators['descWrapper'][1])

        for i in descWrappers:
            key = i.find_element(By.XPATH, ".//h2").text
            v0 = i.find_element(By.XPATH, ".//div[@class='price-box']/p[@class='old-price']").text
            v1 = i.find_element(By.XPATH, ".//div[@class='price-box']/p[@class='special-price']").text
            dictionary[key] = [int(v0[:-6].replace(" ", "")), int(v1[:-6].replace(" ", ""))]

        # print(dictionary)
        #sprawdzam czy wszystkie wartości przekreślone są większe od tych nieprzekreślonych
        for value in dictionary.values():
            assert value[0] > value[1]

