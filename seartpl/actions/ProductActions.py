import time

from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.by import By

from pagesObj.Product import Products

class ProductActions(Products):

    def __init__(self, driver):
        self.driver = driver
        self.datas = {
            'name': 'Witkor',
            'lastName': 'Testowy',
            'email': 'test@seart.pl',
            'tel': '555666888',
            'street': 'Marii Testowej-Curie',
            'address': '22A',
            'floor': 'Pierwsze 1',
            'postCode': '55-888',
            'city': 'Testawa',
            'comment':'TEsT@#!112./'
        }

    # button click

    def addToCartClick(self):
        self.addToCartBtn.click_button()
        time.sleep(2)
        assert self.productsInCart.text == "1 produktów(y)"

    def goToCart(self):
        self.productsInCart.click_button()

    def goToCheckout(self):
        self.goToCheckoutBtn.click_button()

    def fillOutForm(self):
        self.name.set_text(self.datas['name'])
        self.lastName.set_text(self.datas['lastName'])
        self.email.set_text(self.datas['email'])
        self.tel.set_text(self.datas['tel'])
        self.street.set_text(self.datas['street'])
        self.address.set_text(self.datas['address'])
        self.floor.set_text(self.datas['floor'])
        self.postCode.set_text(self.datas['postCode'])
        self.city.set_text(self.datas['city'])
        self.comment.set_text(self.datas['comment'])
        self.delivery.click_button()
        self.payment.click_button()
        time.sleep(2)
        self.accept1.click_button()
        self.accept2.click_button()
        time.sleep(10)

        #do złożenia zamówienia odkomentuj
        # self.confirm.click_button()


