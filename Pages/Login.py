import time

from selenium.webdriver.common.by import By
from Pages.Base import BasePage
from Config.CustomLogger import LogGen


class LoginPage(BasePage):
    #   ********By Locators************
    element = (By.XPATH, "//h5[text()='Elements']")
    Header = (By.XPATH, "//div[@class='main-header']")
    # signin = (By.ID, 'SignIn')
    # username = (By.XPATH, '//*[@type="text"]')
    # password = (By.XPATH, "//*[@type='password']")
    # next =(By.ID, "idp-discovery-submit")
    # Login_button = (By.XPATH, "//*[@type='submit']")
    # forgotPassword = (By.XPATH, "*//a[@class='link help js-help'][text()='Forgot Password?']")
    # resetPassword = (By.CSS_SELECTOR, "#help-links-container > li:nth-child(1) > a")
    # resetUserName = (By.ID, 'account-recovery-username')
    # resetViaEmail = (By.XPATH, "*//a[@class='button button-primary button-wide email-button link-button'][text("
    #                            ")='Reset via Email']")
    # profil = (By.XPATH, "//a[@role='button'][']")
    # log_out = (By.XPATH, "//a[text()=' Logout ']")
    # subscribe = (By.ID, "Subscribe")
    # register_link = (By.XPATH, '//*[@id="wrapper"]/header/nav/h1[2]/a[3]')
    logger = LogGen.loggen()

    # **********Constructor of BasePage Class********
    def __init__(self, driver):
        super().__init__(driver)

    # **********   Page Actions  ***************

    def launch_demo_qa(self):
        time.sleep(3)
        elementdisplayed = self.element_present(self.element)
        self.do_click(self.element)
        return elementdisplayed

    def assertheader(self):
        time.sleep(3)
        header = self.get_text(self.Header)
        print(header)
        return header







    # This function called to validate login credentials
    # def validCredentials(self, username, password):
    #     time.sleep(3)
    #     #self.do_click(self.signin)
    #     self.logger.info("***********  Entering Username **********************")
    #     self.clear(self.username)
    #     self.do_send_keys(self.username, username)
    #     #self.do_click(self.next)
    #     self.do_send_keys(self.password, password)
    #     self.do_click(self.Login_button)
    #     return
    #
    # # This function called when perform ResetPassword
    # def ResetPassword(self, uname):
    #     time.sleep(6)
    #     self.do_click(self.log_out)
    #     time.sleep(6)
    #     self.do_click(self.signin)
    #     time.sleep(6)
    #     self.do_click(self.forgotPassword)
    #     time.sleep(4)
    #     self.do_click(self.resetPassword)
    #     time.sleep(5)
    #     self.do_send_keys(self.resetUserName, uname)
    #     time.sleep(2)
    #     self.do_click(self.resetViaEmail)
    #
    # time.sleep(2)
    #
    # # This function called when perform Subscribe
    # def Subscribe(self):
    #     time.sleep(6)
    #     self.do_click(self.log_out)
    #     time.sleep(7)
    #     self.do_click(self.subscribe)
    #
    # # This function called when perform Register (Create Lite User)
    # def Register(self):
    #     time.sleep(6)
    #     self.do_click(self.log_out)
    #     time.sleep(7)
    #     self.do_click(self.register_link)
    #
    # def Logout(self):
    #     self.do_click(self.profil), time.sleep(2)
    #     self.do_click(self.log_out)
    #     time.sleep(7)
