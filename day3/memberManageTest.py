import unittest

import time
from selenium import webdriver


class MemberManageTest(unittest.TestCase):
    # 变量前面加上self.表示这个变量是类的属性, 可以被所有的方法访问
    def setUp(self):
        # 打开浏览器
        # driver声明在setUp方法之内, 不能被其他方法访问
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # driver.maximize_window()

    def tearDown(self):
        # quit() 退出整个浏览器
        # close()关闭一个浏览器标签
        # 代码编写和调试的时候, 需要在quit()方法前假一个时间等待,方便看清楚执行过程
        # 正式运行的时候去掉时间等待, 为了提高程序执行速度
        time.sleep(20)
        self.driver.quit()

    def test_add_member(self):
        # self.driver.get("")
        driver = self.driver
        driver.get("")