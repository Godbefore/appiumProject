from common.commonfunc import Common
import logging
from common import desired_cap
# 登录功能封装为Login类
class Login(Common):

    def passwordlogin(self,username,password):
        #点击 "我" 
        self.find_element("com.luojilab.player:id/meLayout").click()
        # 进入登录页面
        logging.info("点击按钮：" + nicknametext+ "进入登录页面")
        self.find_element("com.luojilab.player:id/nicknameTextView").click()
        logging.info("不使用短信登录,选择用户名和密码登录")
        self.find_element("com.luojilab.player:id/tv_login_by_pwd").click()
        logging.info("输入用户名(手机号码)：" + username)
        self.find_element("com.luojilab.player:id/et_pet_input").send_keys(username)
        logging.info("输入密码："+"*"*len(password))
        self.find_element("com.luojilab.player:id/et_pwd_input").send_keys(password)
        #点击确认按钮
        #logging.info("点击确认按钮登录")
        #self.find_element("com.luojilab.player:id/btn_login").click()

if __name__ == '__main__':
    driver=desired_cap.appium_desired()
    login=Login(driver)
    login.passwordlogin("13512348888","abc123")