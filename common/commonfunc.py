from base.baseview import BaseView
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import csv
import time
import logging
import os

class Common(BaseView):
    #使用显示等待重写find_element和find_elements方法,默认使用ID查找
    def find_element(self,value,id=By.ID):
        return WebDriverWait(self.driver, 20).until(lambda x: x.find_element(id,value))
    def find_elements(self,value,id=By.ID):
        return WebDriverWait(self.driver, 20).until(lambda x: x.find_elements(id,value))
      
    #判断元素是否存在
    def isexist(self,value,id=By.ID):
        try:
            WebDriverWait(self.driver, 20).until(lambda x: x.find_elements(id,value))
        except NoSuchElementException:
            return False
        else:
            return True
            
    # 从csv文件中获取用户名密码信息
    def getuserby_csv(self,line=0):
        with open("../data/user.csv", "r", encoding='utf-8-sig') as file:
            user = csv.reader(file)
            for l, row in enumerate(user):
                if l==line:
                    return row[0],row[1]
                    
    # 导入connect_mysql后从数据库中获取用户名密码信息                
    def getuserby_mysql(self,line=0)
        pass
    
    # 格式化时间输出
    def getTime(self):
        self.now=time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now
    
    # 截图方法,在screenshots文件中生成 module+时间.png
    def getScreenShot(self,module):
        time=self.getTime()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module,time)

        logging.info('get %s screenshot' %module)
        self.driver.get_screenshot_as_file(image_file)
