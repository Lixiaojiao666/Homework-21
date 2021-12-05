from appium import webdriver
from selenium.webdriver.common.by import By


class TestDaKa:
    def setup(self):
        desired_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": "com.tencent.wework.launch.WwMainActivity",
            "noReset": True,
            "unicodeKeyBoard":True,
            "resetKeyBoard":True,

        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
        self.driver.implicitly_wait(15)
    def teardown(self):
        self.driver.quit()

    def test_daka(self):
        '''
        打开【企业微信】应用
        进入【工作台】页面
        点击【打卡】
        选择【外出打卡】tab
        点击【第 N 次打卡】
        验证点：提示【外出打卡成功】
        :return:
        '''
        self.driver.find_element(By.XPATH)
