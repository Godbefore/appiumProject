from appium import webdriver
import yaml
import logging
import logging.config

_CON_LOG = '../config/log.conf'
logging.config.fileConfig(_CON_LOG)
logging = logging.getLogger()


def appium_desired(name="app1.yaml",port=4723):
    with open("../config/%s"%name, 'r') as file:
        data = yaml.load(file)

    desired_caps = {}
    desired_caps["platformName"] = data["platformName"]
    desired_caps["platformVersion"] = data["platformVersion"]
    desired_caps["deviceName"] = data["deviceName"]
    desired_caps["appPackage"] = data["appPackage"]
    desired_caps["appActivity"] = data["appActivity"]
    desired_caps["noReset"] = False

    driver = webdriver.Remote('http://localhost:%s/wd/hub'%port, desired_caps)


    return driver