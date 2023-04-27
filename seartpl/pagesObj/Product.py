from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory
class Products(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.seart.pl/witryna-sosnowa-vintage.html'

    locators = {
        'addToCartBtn': ('xpath', "//span[contains(text(),'Do koszyka')]"),
        'prodDetails': ('xpath', "//div[@class='specyfikacja']//div"),
        'description': ('xpath', "//div[@class='main_opis']"),
        'faq': ('xpath', "//a[@id='tab_product_faq_tabbed']"),
        'askAboutProduct':('xpath', "//a[@id='tab_productquestions_tabbed']"),
        'addToCartMessage':('xpath', "//div[@id='messages_product_view']/div[2]/div/div/text()"),
        'productsInCart':('xpath', "//div[@class='wrapper']/div/div//div/div/div/div/div/a/span[@class='items']"),
        'goToCheckoutBtn':('xpath', "//div[@class='totals']//button[@title='Przejdź do kasy']"),
        'name':('xpath', "//input[@id='billing:firstname']"),
        'lastName':('xpath', "//input[@id='billing:lastname']"),
        'email':('xpath', "//input[@placeholder='nazwa@domena.pl']"),
        'tel':('xpath', "//input[@id='billing:telephone']"),
        'street':('xpath', "//input[@id='billing:street1']"),
        'address':('xpath', "//input[@id='billing:street2']"),
        'floor':('xpath', "//input[@id='billing:floor']"),
        'postCode':('xpath', "//input[@id='billing:postcode']"),
        'city':('xpath', "//input[@id='billing:city']"),
        'delivery':('xpath', "//label[@for='s_method_flatrate_flatrate']"),
        'payment':('xpath', "//label[@for='p_method_banktransfer']"),
        'comment':('xpath', "//textarea[@id='order-comment']"),
        'accept1':('xpath', "//label[@for='agreement-1']"),
        'accept2':('xpath', "//input[@id='agreement-3']"),
        'confirm':('xpath', "//button[@title='Potwierdzam zamówienie']")
    }

    def SimpleProduct_assertions(self):
        assert self.addToCartBtn.element_to_be_clickable()
        assert self.faq.element_to_be_clickable()
        assert self.askAboutProduct.element_to_be_clickable()
        assert self.prodDetails.visibility_of_element_located()
        assert self.description.visibility_of_element_located()


    def goSimpleProduct(self):
        self.driver.get(self.url)
