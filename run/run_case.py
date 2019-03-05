import unittest
from run import HTMLTestRunner_cn

#要扫描的测试文件目录
test_dir = '../case'
discover = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern="test*.py",top_level_dir=None)
# 保存报告目录
filename = '../report/result.html'
# 打开文件
fp = open(filename, 'wb')
# 用HTMLTestRunner_cn生成报告
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：')
runner.run(discover)
fp.close()