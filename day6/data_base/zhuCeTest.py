import unittest

import time

from day5.myTestCase import MyTestCase
from day6.data_base.connectDB import connDb


class ZhuCeTest(MyTestCase):
    def test_zhu_ce(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.find_element_by_name("username").send_keys("xingxing1203")
        driver.find_element_by_name("password").send_keys("111111")
        driver.find_element_by_name("userpassword2").send_keys("111111")
        driver.find_element_by_name("mobile_phone").send_keys("15811327410")
        driver.find_element_by_name("email").send_keys("74855@163.com")
        driver.find_element_by_class_name("reg_btn") .click()
        expected ="xingxing1203"
        time.sleep(3)
        actul =connDb()[1]
        self.assertEquals(expected,actul)
        print(connDb()[1] )

