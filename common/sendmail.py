import smtplib
from email.mime.text import MIMEText

class Mail():
    _send_host="smtp.163.com"
    _send_user="test"
    _send_address="test@163.com"
    _send_password="123456"

    def send_mail(self,user_list,subject,content):
        sender="test_name" + "<" + self._send_address + ">"
        message = MIMEText(content, _subtype="plain", _charset="utf-8")
        message["Subject"]=subject
        message["From"]=sender
        message["To"] = ";".join(user_list)
        self._server(sender,user_list,message)


    def _server(self, sender,user_list,message):
        server = smtplib.SMTP()
        server.connect(self._send_host)
        server.login(self._send_user, self._send_password)
        server.sendmail(sender, user_list,message.as_string())
        server.close()

if __name__ =="__main__":
    mail=Mail()
    mail.send_mail([""],"Subject:test","Content:success")



