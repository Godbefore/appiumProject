from appium import webdriver
from time import sleep
import logging
from selenium.common.exceptions import NoSuchElementException

class BaseView(object):

    def __init__(self,driver):
        self.driver=driver
        # 初始化后进入APP主页，关闭新手提示
        for i in range(12):
            try:
                self.driver.find_element_by_id("com.luojilab.player:id/iv_close").click()    
            except NoSuchElementException:
                sleep(1)
            else：
                logging.info("第%s秒点击关闭初始化消息框"%i)
                break
    # 获取窗口的实际大小
    def getsize(self):
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        return x,y
    # 向右滑动，默认在banner位置
    def rightswipe(self,y=0.1,var=1):
        size=self.driver.getsize()
        x1=int(size[0]*0.2) # 从左边20%
        x2=int(size[0]*0.8) # 到右边80%
        y1=int(size[1]*y)
        y2=int(size[1]*y)
        # var指定滑动次数
        for i in range(var):
            self.driver.swipe(x1,y1,x2,y2,500)
            logging.info("右滑%s次" % (i + 1))
            sleep(0.5)
    # 向左滑动，默认在banner位置        
    def leftswipe(self,y=0.1,var=1):
        size=self.driver.getsize()
        x1=int(size[0]*0.8)
        x2=int(size[0]*0.2)
        y1=int(size[1]*y)
        y2=int(size[1]*y)
        for i in range(var):
            self.driver.swipe(x1,y1,x2,y2,500)
            logging.info("左滑%s次"%(i+1))
            sleep(0.5)

if __name__=="__main__":
    driver = webdriver.Remote()

