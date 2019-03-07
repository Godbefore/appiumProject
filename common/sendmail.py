import smtplib
from email.mime.text import MIMEText

# 发送测试结果到邮件
class Mail():
    _send_host="smtp.163.com" # 邮箱host
    _send_user="test" # 用户名
    _send_address="test@163.com" # 邮箱名
    _send_password="123456" # 密码

    def send_mail(self,user_list,subject,content):
        # 发送者<邮箱地址>
        sender="test_name" + "<" + self._send_address + ">"
        # 用MIME得到邮件格式文本message
        message = MIMEText(content, _subtype="plain", _charset="utf-8")
        message["Subject"]=subject # 邮件主题
        message["From"]=sender     # 邮件发送者
        message["To"] = ";".join(user_list) # 收件人列表
        self._server(sender,user_list,message) # 调用发送方法

    # 连接邮箱服务器并发送邮件
    def _server(self, sender,user_list,message):
        server = smtplib.SMTP()
        server.connect(self._send_host)
        server.login(self._send_user, self._send_password)
        server.sendmail(sender, user_list,message.as_string())
        server.close()

if __name__ =="__main__":
    mail=Mail()
    mail.send_mail([""],"Subject:test","Content:success")



