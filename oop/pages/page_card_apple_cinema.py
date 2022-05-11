from oop.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class PageCardShopLocator:
    NAME_PRODUCT = (By.CSS_SELECTOR, '[id="product-product"] [class="col-sm-4"] h1')


class PageCardShop(BasePage):
    def get_count_image_product(self):
        return len(self.find_elements((By.CSS_SELECTOR, '[class="image-additional"]')))

    def get_styles_price(self):
        return self.find_element((By.XPATH, "//*[(text() = '$122.00')]")).get_attribute("style")

    def get_name_product(self):
        return self.find_element(PageCardShopLocator.NAME_PRODUCT).text
