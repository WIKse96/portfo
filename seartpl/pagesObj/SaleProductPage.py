from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By


class OneProductSale(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        'omnimbusInfo': ('xpath', "//div[@class='product-shop col-sm-7']/div[@class='price-box']/div[@class='tooltip pricetooltipomnibus']"),
        'specialPrice': ('xpath', "//div[@class='product-shop col-sm-7']/div[@class='price-box']/p[@class='special-price']/span[@class='price']"),
        'oldPrice': ('xpath', "//div[@class='product-shop col-sm-7']/div[@class='price-box']/p[@class='old-price']/span[@class='price']"),
        'addToCartBtn':('xpath', "//span[contains(text(),'Do koszyka')]")

    }

    def one_product_assertions(self):
        assert self.omnimbusInfo.visibility_of_element_located()
        assert self.specialPrice.visibility_of_element_located()
        assert self.oldPrice.visibility_of_element_located()
        assert self.addToCartBtn.visibility_of_element_located()

        global specialPriceSale
        specialPriceSale = self.specialPrice


