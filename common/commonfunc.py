from base.baseview import BaseView
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import csv
import time
import logging
import os

class Common(BaseView):

    def find_element(self,value,id=By.ID):
        return WebDriverWait(self.driver, 20).until(lambda x: x.find_element(id,value))

    def find_elements(self,value,id=By.ID):
        return WebDriverWait(self.driver, 20).until(lambda x: x.find_elements(id,value))

    def isexist(self,value,id=By.ID):
        try:
            WebDriverWait(self.driver, 20).until(lambda x: x.find_elements(id,value))
            return True
        except NoSuchElementException:
            return False

    def getuser(self,l=0):
        with open("../data/user.csv", "r", encoding='utf-8-sig') as file:
            user = csv.reader(file)
            for line, row in enumerate(user):
                if l==line:
                    return row[0],row[1]

    def getTime(self):
        self.now=time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self,module):
        time=self.getTime()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module,time)

        logging.info('get %s screenshot' %module)
        self.driver.get_screenshot_as_file(image_file)
