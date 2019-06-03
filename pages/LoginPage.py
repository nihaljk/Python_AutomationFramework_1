class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.username = "txtUsername"
        self.password = "txtPassword"
        self.login_id = "btnLogin"

    def enter_username(self,username):
        self.driver.find_element_by_id(self.username).clear()
        self.driver.find_element_by_id(self.username).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_id(self.password).clear()
        self.driver.find_element_by_id(self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_id).click()