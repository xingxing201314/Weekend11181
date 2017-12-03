from selenium import webdriver
import unittest
import ddt

from day4.readCsv2 import read


@ddt.ddt
class UnittestDemo(unittest.TestCase):

    member_info = read("member_info.csv")

    @classmethod
    def setUpClass(cls):
        print("set up class")

    @classmethod
    def tearDownClass(cls):
        print("tear Down")

    def test_log_in(self):
        print("log in")

    @ddt.data(*member_info)
    def test_add_member(self, data):
        print("add member")
        print(data[0])

