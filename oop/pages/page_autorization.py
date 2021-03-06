import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from oop.pages.base_page import BasePage


@pytest.fixture(scope="function")
def authorization_admin(browser, url):
    browser.get(url + "admin/")
    BasePage(browser).find_element((By.CSS_SELECTOR, '[id="input-username"]')).send_keys("user")
    BasePage(browser).find_element((By.CSS_SELECTOR, '[id="input-password"]')).send_keys("bitnami")
    BasePage(browser).find_element((By.CSS_SELECTOR, '[type="submit"]')).click()


class PageAuthorizationAdminLocator:
    SUBMIT = (By.CSS_SELECTOR, "[type='submit']")


class PageAuthorizationAdmin(BasePage):
    def get_text_title(self):
        return self.find_element((By.CSS_SELECTOR, '[class="panel-title"]')).text

    def get_text_by_button_submit(self):
        return self.find_element(PageAuthorizationAdminLocator.SUBMIT).text

    def get_text_by_error_authorization(self):
        self.find_element(PageAuthorizationAdminLocator.SUBMIT).click()
        return self.find_element((By.CSS_SELECTOR, '[class="alert alert-danger alert-dismissible"]')).text

    def get_text_placeholder(self, element):
        return self.find_element((By.CSS_SELECTOR, f'[name="{element}"]')).get_attribute('placeholder')

