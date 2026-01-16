from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # Example locators (replace with your actual locators)
        self.textbox_username_xpath = (By.XPATH, "//input[@placeholder='Username']")
        self.textbox_password_xpath = (By.XPATH, "//input[@placeholder='Password']")
        self.button_login_xpath = (By.XPATH, "//button[@type='submit']")
        self.invalid_msg_xpath = (By.XPATH, "//div[@class='error-message']")

    # ------------------------------
    # Actions returning True/False
    # ------------------------------

    def input_username(self, username: str) -> bool:
        """
        Enter username and return True if successful
        """
        try:
            username_field = self.wait.until(EC.visibility_of_element_located(self.textbox_username_xpath))
            username_field.clear()
            username_field.send_keys(username)
            return True
        except Exception as e:
            return False

    def input_password(self, password: str) -> bool:
        """Enter password and return True if successful"""
        try:
            password_field = self.wait.until(EC.visibility_of_element_located(self.textbox_password_xpath))
            password_field.clear()
            password_field.send_keys(password)
            return True
        except Exception as e:
            return False

    def click_login(self) -> bool:
        """Click login button and return True if successful"""
        try:
            self.wait.until(EC.element_to_be_clickable(self.button_login_xpath)).click()
            return True
        except Exception as e:
            return False

    # ------------------------------
    # Validation / getter methods
    # ------------------------------

    def invalid_mssg(self) -> str:
        """Return the text of invalid credentials message"""
        try:
            return self.wait.until(EC.visibility_of_element_located(self.invalid_msg_xpath)).text
        except:
            return ""
