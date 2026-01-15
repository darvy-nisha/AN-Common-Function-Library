from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    textbox_username_xpath = (By.XPATH, "//input[@placeholder='Username']")
    textbox_password_xpath = (By.XPATH, "//input[@placeholder='Password']")
    button_login_xpath = (By.XPATH, "//button[@type='submit']")
    invalid_msg_xpath = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")

    def input_username(self, username):
        username_field = self.wait.until(EC.visibility_of_element_located(self.textbox_username_xpath))
        username_field.clear()
        username_field.send_keys(username)

    def input_password(self, password):
        password_field = self.wait.until(EC.visibility_of_element_located(self.textbox_password_xpath))
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.button_login_xpath)).click()

    def invalid_mssg(self):
        return self.wait.until(EC.visibility_of_element_located(self.invalid_msg_xpath)).text
