import time

from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory


class HomePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.seart.pl/"

        #wyszukiwany tekst w funcji searchDeskopt()
        self.texts_to_search = {'search_Home_Page':'Komoda'}

    # Locators
    locators = {
        'loginBtn': ('xpath', "//a[@title='Zaloguj']"),
        'registerBtn': ('xpath', "//a[@title='Załóż konto']"),
        'logo': ('xpath', "//div[@class='logo active']"),
        'linkMoreBlogPosts':('xpath', "//a[@class='show-more-link'][contains(text(),'Zobacz więcej postów')]"),
        'mainBaner':('xpath', "//img[@id='baner4_slider']"),
        'categoryIcon':('xpath', "//div[@class='categoryicon']"),
        'colecctionMenuBtn': ('xpath',"//div[@id='megamenuwraper']//a[@class='Level0 '][normalize-space()='Kolekcje']"),
        'b2bLink':('xpath', "//a[@title='Współpraca b2b']"),
        'fbLink':('xpath', "//em[@class='fa fa-facebook']"),
        'gridRustyk':('xpath', "// div[@class ='banner a-center banner-font-light hover-fade'] / div[@ class ='banner-content'] / div[@ class ='banner-inner'] / div[@ class ='whiteback'] / div[@ class ='white'] / h3/a[normalize-space()='Rustyk']"),
        'spanShopTheLook':('xpath', "//span[normalize-space()='Shop the look']"),
        'tel':('xpath', "//div[@class='infolinia visible-sm visible-md visible-lg a-right']/a[contains(text(),'601 316 615')]"),
        'currency':('xpath', "//div[@id='currency-select']//a[@class='kody-waluty'][normalize-space()='GBP']"),
        'freeDeliveryBaner':('xpath', "//div[@class='banner a-center banner-font-light hover-fade']/a[@href='https://www.seart.pl/koszt-dostawy.html']"),
        'featuredHome':('xpath', "//div[@class='slider-featured-container']"),
        'opinions':('xpath', "//div[@class='row opinie-klientow']"),
        'whyisitworth':('xpath', "//center[normalize-space()='Dlaczego warto?']"),
        'orderdeliveryFooter':('xpath', "//div[@class='content-element']/div/h3[contains(text(),'Dostawy zamówień')]"),
        'ourOferFooter':('xpath', "//div/div[@class='content-element']/h3[normalize-space()='Nasza Oferta']"),
        'informationFooter':('xpath', "//div/div[@class='content-element']/h3[normalize-space()='Informacje']"),
        'inputSearch':('xpath', "//input[@id='search'][@name='q'][@xpath=2]"),
        'menu_meble':('xpath', "//div[@id='megamenuwraper']//a[contains(@class,'Level0')][normalize-space()='Meble']"),
        'toaletki_menu':('xpath', "//div[@id='megamenuwraper']//a[contains(@class,'Level2')][normalize-space()='Toaletki i konsole']"),
        'search_bar':('xpath', "//div[@class='quick-access search-center hidden-xs hidden-sm']//input[@id='search']"),
        'search_btn':('xpath', "//body/div[contains(@class,'wrapper active')]/div[contains(@class,'page active')]/div[contains(@class,'active')]/div[contains(@class,'header active')]/div[contains(@class,'container active')]/div[contains(@class,'table-row active')]/div[contains(@class,'quick-access search-center hidden-xs hidden-sm')]/form[@id='search_mini_form']/div[contains(@class,'form-search')]/button[contains(@title,'Szukaj')]/span[1]")
    }


# assertios
    def homePage_assertions(self):
        assert self.loginBtn.element_to_be_clickable()
        assert self.registerBtn.element_to_be_clickable()
        assert self.b2bLink.visibility_of_element_located()
        assert self.colecctionMenuBtn.element_to_be_clickable()
        assert self.currency.element_to_be_clickable()
        assert self.tel.element_to_be_clickable()
        # assert self.mainBaner.element_to_be_clickable()
        assert 'https://www.seart.pl/media/wysiwyg/banery-rozne/banner-lewy-sredni-2023_kopia.jpg' in self.driver.page_source
        assert self.opinions.visibility_of_element_located()
        assert self.orderdeliveryFooter.visibility_of_element_located()
        assert self.ourOferFooter.visibility_of_element_located()

        assert 'src="https://www.seart.pl/skin/frontend/pixel/seart/images/logo_seart.png"' in self.driver.page_source
        assert self.gridRustyk.visibility_of_element_located()
        assert self.categoryIcon.visibility_of_element_located()
        assert self.fbLink.visibility_of_element_located()
        assert self.spanShopTheLook.visibility_of_element_located()
        assert "Meble z drewna" in self.driver.page_source
        assert "Meble drewniane z kolekcji Sara pozwolą w piękny, ponadczasowy i funkcjonalny sposób urządzić mieszkanie. Kolekcja Sara to eleganckie, zachwycające w swej prostocie meble z drewna świerkowego." in self.driver.page_source
        assert "Spraw, aby twoje wnętrze stało się przytulne i stylowe. Postaw na dywany retro, dywany nowoczesne lub modne dywany sznurkowe. Dywany z naszej ofert świetnie sprawdzają się w aranżacjach scandi-boho, rustykalnych i nowoczesnych." in self.driver.page_source
        assert "To dzięki naszym Klientom mamy co i dla kogo tworzyć" in self.driver.page_source
        assert "Copyright (C) 2018 Seart. All rights reserved." in self.driver.page_source
        assert self.driver.title == "Meble drewniane od producenta - Seart.pl - Sklep meblowy online"
        assert self.search_bar.visibility_of_element_located()

        print("========================OK - homePage_assertions ========================")
