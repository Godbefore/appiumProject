from common.startend import StratEnd
from businese.login import Login
import unittest

class Test_Login(StratEnd):
    # 登录成功后会显示"登录成功"元素，用来判断是否登录成功
    successinfo=""
    def test_1(self):
        driver=Login(self.driver)
        usermessage=driver.getuserby_csv(0)
        driver.passwordlogin(*usermessage)
        self.assertTrue(driver.isexist(self.successinfo))
        driver.getScreenShot("login_t1")

    def test_2(self):
        driver=Login(self.driver)
        usermessage=driver.getuserby_csv(1)
        driver.passwordlogin(*usermessage)
        self.assertTrue(driver.isexist(self.successinfo))
        driver.getScreenShot("login_t2")

    def test_3(self):
        driver = Login(self.driver)
        usermessage = driver.getuserby_csv(2)
        driver.passwordlogin(*usermessage)
        self.assertTrue(driver.isexist(self.successinfo))
        driver.getScreenShot("login_t3")

if __name__=="__main__":
    unittest.main()