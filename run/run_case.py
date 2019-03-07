import unittest
from run import HTMLTestRunner_cn
import sys
import logging
import time

# 项目目录
path='C:/appiumProject/'
sys.path.append(path)
# 要扫描的测试文件目录
test_dir = '../case'
discover = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern="test*.py",top_level_dir=None)
# 保存报告目录
now=time.strftime('%Y-%m-%d %H_%M_%S')
filename = '../report/'+ now +' result.html'
# 打开文件
fp = open(filename, 'wb')
# 用HTMLTestRunner_cn生成报告
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'case执行情况：')
logging.info("===========测试开始===========")
runner.run(discover)
fp.close()
logging.info("===========测试结束===========")