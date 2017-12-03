import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from day5.myTestCase import MyTestCase

class LoginTestCase(MyTestCase):
    def test_login(self):
        #self.driver.get("http://localhost/index.php?m=user&c=public&a=login")
        lp = LoginPage()
        lp.open()

        #self.driver.find_element(By.ID,"username").send_keys("xingxing1203")
        lp.input_username("xingxing1203")
        #self.driver.find_element(By.ID,"password" ) .send_keys("111111")
        lp.input_password("111111")

        #self.driver.find_element(By.CLASS_NAME,"login_btn ").click()
        lp.input_login_btn.click()

        time.sleep(5)
        expected ="我的会员中心 - 道e坊商城 - Powered by Haidao"
        self.assertIn("我的会员中心",self.driver.title)
        pcp = PersonalCenterPage(self.driver)
        time.sleep(5)
        self.assertIn(pcp.title,self.driver .title)


