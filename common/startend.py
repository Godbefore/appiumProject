from unittest import TestCase
from common.desired_cap import appium_desired
import logging
import time

class StratEnd(TestCase):
    #@classmethod
    #def setUpclass(cls):
    #def tearDownclass(cls):
    
    
    
    # 执行case前
    def setUp(self):
        self.driver=appium_desired()
        logging.info("启动APP，开始测试")
    # 执行case后
    def tearDown(self):
        logging.info("关闭APP，完成测试用例")
        self.driver.close_app()
        time.sleep(3)
