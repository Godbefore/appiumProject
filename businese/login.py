from common.commonfunc import Common
import logging
from common import desired_cap


class Login(Common):

    def passwordlogin(self,username,password):
        self.find_element("com.luojilab.player:id/meLayout").click()
        nickname=self.find_element("com.luojilab.player:id/nicknameTextView")
        nicknametext=nickname.text
        nickname.click()
        logging.info("点击按钮：" + nicknametext+ "进入登录页面")
        self.find_element("com.luojilab.player:id/tv_login_by_pwd").click()
        logging.info("使用用户名密码登录")
        self.find_element("com.luojilab.player:id/et_pet_input").send_keys(username)
        logging.info("输入手机号码："+username)
        self.find_element("com.luojilab.player:id/et_pwd_input").send_keys(password)
        logging.info("输入密码")
        #点击确认按钮
        #self.find_element("com.luojilab.player:id/btn_login").click()

if __name__ == '__main__':
    driver=desired_cap.appium_desired()
    login=Login(driver)
    login.passwordlogin("13566668888","abc123")