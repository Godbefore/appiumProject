# Automated Testing Learning:appium

## A simple Framework of appium with python unittest

```c# 
1. base：
    > 存放基础模块类:BaseView,该类封装最基本的方法
    baseView.py
        BaseView类
        初始化driver
        基础方法封装
2. businese：
    > 存放业务逻辑模块
    login.py
        继承commonfunc模块中的Common类    
        定义Login类封装登录操作相关元素和方法
3. case：
    > 存放测试类的模块
    test_login.py
        继承myunit模块中StartEnd类
        登录测试类封装：Test_Login
        调用Login类中的方法来编写用例
4. common：
    > 封装公共方法类
    commonfunc.py 
        公共类Common封装
        继承baseView中的BaseView类
        给业务模块进行继承调用其中的方法    
    connect_mysql.py
        封装连接访问MySQL数据库方法
    desired_caps.py 
        driver驱动封装
        日志配置文件加载
        启动App配置参数
    operate_execel
        封装操作Excel_2007文件方法
    sendmail.py
        封装关于发送结果到邮件的方法
    startend.py
        StartEnd类
        测试用例执行前后操作配置，封装为StartEnd类        
        继承unittest中TestCase类
        setUp() ：用例执行前执行操作
        tearDown()：用例执行完成后的操作    
        (setUpClass(),tearDownClass()所有用例执行前，执行后操作)
5. config：
    > 用于存放配置文件
    app1.yaml
        capability数据配置
    log.conf
        日志配置文件
6. data：
    > 数据文件,用于数据驱动
    user.csv
        用户名，密码数据
7. logs：
    > 存放日志文件
8. report：
    > 存放Html图形测试报告
    > 存放Excel文件类型的测试结果报告
9. run：
    > 执行自动化测试用例的模块
    HTMLTestRunner_cn.py
        用于生产Html报告的模块
    run.py
        自动化用例执行的入口
10. screenshots：
    > 存放截图文件
