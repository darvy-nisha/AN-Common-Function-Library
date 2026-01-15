from selenium.webdriver.common.by import By


class Login:
    def __init__(self,driver):
        self.text_invalidmsg_xpath
        self.driver = driver

    textbox_username_xpath = (By.XPATH, "//input[@placeholder='Username']")
    textbox_password_xpath = (By.XPATH, "//input[@placeholder='Password']")
    button_login_xpath = (By.XPATH, "//button[@type='submit']")
    invalid_msg_xpath = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")

    def input_username(self,username):
        self.driver.find_element(*self.textbox_username_xpath).send_keys(username)

    def input_password(self,password):
        self.driver.find_element(*self.textbox_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.button_login_xpath).click()

    def invalid_mssg(self):
        return self.driver.find_element(*self.invalid_msg).text


