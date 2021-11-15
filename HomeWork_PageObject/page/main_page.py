

#po封装首页类
from selenium import webdriver
from selenium.webdriver.common.by import By

from HomeWork_PageObject.page.login_page import LoginPage
from HomeWork_PageObject.page.register_page import RegisterPage


class MainPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/')
        self.driver.implicitly_wait(5)
    #封装 企业登录 功能
    def goto_login(self):
        self.driver.find_element(By.XPATH,'//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        # 将LoginPage类初始化为对象,同时传递一个diver过去，这样登录页就不会重复初始化driver，直接使用首页的driver即可
        # 初始化一个类为对象，就是为了要使用它，此时初始化，就是为了传递driver过去
        return LoginPage(self.driver)

    #封装 点击注册 功能
    def goto_register(self):
        self.driver.find_element(By.XPATH,'//*[@id="tmp"]/div[1]/a').click()
        #将RegisterPage类初始化为对象,同时传递一个diver过去，这样注册页就不会重复初始化driver，直接使用首页的dirver即可
        #初始化一个类为对象，就是为了要使用它，此时初始化，就是为了传递driver过去
        return RegisterPage(self.driver)


