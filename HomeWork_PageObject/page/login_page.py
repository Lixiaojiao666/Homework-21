from selenium import webdriver


from HomeWork_PageObject.page.register_page import RegisterPage


class LoginPage():
    def __init__(self,driver):
        self.driver = driver

    def scan_login(self):
        pass
    def goto_register(self):
        self.driver.find_element_by_xpath('//*[@id="wework_admin.loginpage_wx2_$"]/main/div[2]/a').click()
        # 将RegisterPage类初始化为对象,同时传递一个diver过去，这样注册页就不会重复初始化driver，直接使用首页的dirver即可
        # 初始化一个类为对象，就是为了要使用它，此时初始化，就是为了传递driver过去
        return RegisterPage(self.driver)



