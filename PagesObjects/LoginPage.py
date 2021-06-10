class LoginPage():
    # locator of all the  elements
    textbox_username_name="txtUsername"
    textbox_password="txtPassword"
    button_click="Submit"
    text_welcome="welcome"

    def __init__(self,driver):
        self.driver=driver
    def setUserName(self,username):
        self.driver.find_element_by_name(self.textbox_username_name).send_keys(username)
    def setPassword(self,password):
        self.driver.find_element_by_name(self.textbox_password).send_keys(password)
    def ClickLogin(self):
        self.driver.find_element_by_name(self.button_click).click()
    def ClickButton(self):
        self.driver.find_element_by_id(self.text_welcome).click()
