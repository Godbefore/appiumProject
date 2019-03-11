from common.commonfunc import Common
import logging
from common import desired_cap

class HomePlay(Common):
    def play(self):
    #
        self.find_element("com.luojilab.player:id/homeLayout").click()
        
        list=self.find_elements("com.luojilab.player:id/play_state")
        print(list)
    
if __name__ == '__main__':
    driver=desired_cap.appium_desired()
    hp=HomePlay(driver)
    hp.play()