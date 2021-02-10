import allure
import configparser
import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


@allure.feature('Test Baidu WebUI')
class ISelenium(unittest.TestCase):

    def test1(self):
        # print(os.environ.keys())
        # print(os.environ.values())
        # print(os.environ['HOMEPATH'])

        # 从环境变量中获取数据库配置
        user = os.environ.get('USERNAME')
        print(user)
        pwd = os.environ.get('PWD')
        print(pwd)
        host = os.environ.get('HOST')
        print(host)
        port = os.environ.get('PORT')
        print(port)
        dbName = os.environ.get('DBNAME')
        print(dbName)

        # 获取环境变量的所有key
        keys = os.environ.keys()  #
        values = os.environ.values()
        print(type(keys))  # <class 'collections.abc.KeysView'>
        print(list(keys))
        print(list(values))