from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.extensions import android
from selenium.webdriver.common.by import By

class TestAddMembers:
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

    def test_add_members(self):
        '''
        打开【企业微信】应用
        进入【通讯录】页面
        点击【添加成员】
        点击【手动输入添加】
        输入【姓名】【手机号】并点击【保存】
        验证点：添加成功提示信息
        '''
        #定位并点击 通讯录，组合查询：resource id 和 text
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.wework:id/f3a").text("通讯录")').click()
        #定位并点击 添加成员
        self.driver.find_element(MobileBy.XPATH,'//*[@text="添加成员"]').click()
        # 定位并点击 手动输入添加
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        # 输入姓名，手机号
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/bf7"]').send_keys("李酸")
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/gge"]').send_keys("18866668889")
        #定位并点击 保存 按钮
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/am4"]').click()

        #验证添加成功：获取提示添加成功的toast
        #print(self.driver.find_element(MobileBy.XPATH,
        #                               '//*[@class="android.widget.Toast"]//*[contains(@text,"添加成功")]').text)
