import sys
from time import sleep

from HomeWork_PageObject.page.main_page import MainPage




class TestRegister:
    def test_register(self):
        #实例化一个首页类
        main = MainPage()
        #使用 首页类MainPage 的goto_register()方法里返回的 注册页类RegisterPage 的register()方法
        main.goto_register().register()
        sleep(3)

    def test_login_register(self):
        main = MainPage()
        main.goto_login().goto_register().register()