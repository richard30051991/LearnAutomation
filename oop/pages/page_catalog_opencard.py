from oop.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class PageCatalogShopLocator:
    INPUT_LIMIT = (By.CSS_SELECTOR, '[id="input-limit"] option[selected="selected"]')
    INPUT_SORT = (By.CSS_SELECTOR, '[id="input-sort"] option[selected="selected"]')
    NEW_PRICE_APPLE_CINEMA = (By.XPATH, "//*[@alt='Apple Cinema 30\"']/../../..//span[@class='price-new']")
    OLD_PRICE_APPLE_CINEMA = (By.XPATH, "//*[@alt='Apple Cinema 30\"']/../../..//span[@class='price-old']")


class PageCatalogShop(BasePage):
    def check_input_limit(self):
        return self.find_element(PageCatalogShopLocator.INPUT_LIMIT).text

    def get_input_sort(self):
        return self.find_element(PageCatalogShopLocator.INPUT_SORT).text

    def get_new_price_apple_cinema(self):
        return self.find_element(PageCatalogShopLocator.NEW_PRICE_APPLE_CINEMA).text

    def get_old_price_apple_cinema(self):
        return self.find_element(PageCatalogShopLocator.OLD_PRICE_APPLE_CINEMA).text
