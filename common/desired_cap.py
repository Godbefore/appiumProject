from appium import webdriver
import yaml
import logging
import logging.config
# 配置日志信息
_CON_LOG = '../config/log.conf'
logging.config.fileConfig(_CON_LOG)
logging = logging.getLogger()

# 设置初始化desird,返回一个driver
def appium_desired(name="app1.yaml",port=4723,noReset=False):
    # 从yaml文件中读取配置
    with open("../config/%s"%name, 'r') as file:
        data = yaml.load(file)

    desired_caps = {}
    desired_caps["platformName"] = data["platformName"]
    desired_caps["platformVersion"] = data["platformVersion"]
    desired_caps["deviceName"] = data["deviceName"]
    desired_caps["appPackage"] = data["appPackage"]
    desired_caps["appActivity"] = data["appActivity"]
    #是否重置APP 采用参数化
    desired_caps["noReset"] = noReset

    driver = webdriver.Remote('http://localhost:%s/wd/hub'%port, desired_caps)
    return driver