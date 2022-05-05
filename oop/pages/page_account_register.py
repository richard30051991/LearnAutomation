from oop.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class PageRegisterLocator:
    CONTINUE = (By.CSS_SELECTOR, '[value = "Continue"]')


class PageRegister(BasePage):
    def fill_in_the_fields(self, firstname, lastname, email, telephone, password, confirm):
        self.find_element((By.CSS_SELECTOR, '[name="firstname"]')).send_keys(firstname)
        self.find_element((By.CSS_SELECTOR, '[name="lastname"]')).send_keys(lastname)
        self.find_element((By.CSS_SELECTOR, '[name="email"]')).send_keys(email)
        self.find_element((By.CSS_SELECTOR, '[name="telephone"]')).send_keys(telephone)
        self.find_element((By.CSS_SELECTOR, '[name="password"]')).send_keys(password)
        self.find_element((By.CSS_SELECTOR, '[name="confirm"]')).send_keys(confirm)

    def click_continue_button(self):
        self.find_element(PageRegisterLocator.CONTINUE).click()

    def click_checkbox_privacy_policy(self):
        self.find_element((By.CSS_SELECTOR, '[name="agree"]')).click()

    def get_text_alert_null__privacy_policy(self):
        return self.find_element((By.CSS_SELECTOR, '[class="alert alert-danger alert-dismissible"]')).text

    def get_text_error_null_name(self):
        return self.find_element((By.CSS_SELECTOR, '[class="text-danger"]'))[0].text

    def get_count_error_null_fields(self):
        return len(self.find_elements((By.CSS_SELECTOR, '[class="text-danger"]')))
