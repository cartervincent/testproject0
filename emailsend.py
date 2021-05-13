import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '***'
receiver = '***'
subject = 'python email test'
smtpserver = 'smtp.163.com'
username = '***'
password = '***'

msg = MIMEText(u'你好', 'plain', 'utf-8')  # 中文需参数‘utf-8'，单字节字符不需要
msg['Subject'] = Header(subject, 'utf-8')

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
