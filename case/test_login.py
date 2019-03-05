from common.startend import StratEnd
from businese.login import Login
import unittest


class Test_Login(StratEnd):
    def test_1(self):
        driver=Login(self.driver)
        usermessage=driver.getuser(0)
        driver.passwordlogin(*usermessage)
        self.assertTrue(driver.isexist('com.luojilab.player:id/btn_login'))
        driver.getScreenShot("login")

    def test_2(self):
        driver=Login(self.driver)
        usermessage=driver.getuser(1)
        driver.passwordlogin(*usermessage)
        self.assertTrue(driver.isexist('com.luojilab.player:id/btn_login'))
        driver.getScreenShot("login")


    def test_3(self):
        driver = Login(self.driver)
        usermessage = driver.getuser(2)
        driver.passwordlogin(*usermessage)
        self.assertTrue(driver.isexist('com.luojilab.player:id/btn_login'))
        driver.getScreenShot("login")

if __name__=="__main__":
    unittest.main()