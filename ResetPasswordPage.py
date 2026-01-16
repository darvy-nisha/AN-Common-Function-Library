from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResetPasswordPage:
    """
    Page Object for the Reset Password page.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.forgot_password_button = (By.XPATH,"//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")
        self.username_input = (By.XPATH, "//input[@placeholder='Username']")
        self.reset_password_button = (By.XPATH, "//button[@type='submit']")

    def click_forget_password_button(self) -> bool:
        """
        Clicks the 'Forgot Password' button.
        """
        try:
            self.wait.until(EC.element_to_be_clickable(self.forgot_password_button)).click()
            return True
        except Exception:
            return False

    def enter_username(self, username: str) -> bool:
        """
        Enters the username in the username input field.
        """
        try:
            username_field = self.wait.until(EC.visibility_of_element_located(self.username_input))
            username_field.clear()
            username_field.send_keys(username)
            return True
        except Exception:
            return False

    def click_reset_password_button(self) -> bool:
        """
        Clicks the Reset Password button.
        """
        try:
            self.wait.until(EC.element_to_be_clickable(self.reset_password_button)).click()
            return True
        except Exception:
            return False
