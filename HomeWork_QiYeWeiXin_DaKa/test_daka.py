from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
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
        #self.driver.quit()
        pass

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
        #定位并点击 工作台，组合查询：resource id 和 text
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.wework:id/f3a").text("工作台")').click()
        #定位并点击 打卡
        self.driver.find_element(MobileBy.XPATH,'//*[@text="打卡"]').click()
        #定位并点击 外出打卡
        self.driver.find_element(MobileBy.XPATH, '//*[@text="外出打卡"]').click()
        #定位并点击 包含“次打卡”的元素
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("次外出")').click()

        #验证打卡成功：定位“外出打卡成功”，并打印
        print(self.driver.find_element(MobileBy.XPATH, '//*[@text="外出打卡成功"]').text)