# PGEWCRZXYPHQSDNE
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def send_e_mail():
    # 邮件内容配置
    # 邮箱文本
    mse = MIMEText('hello', 'html', 'utf-8')
    # 发件人
    mse['From'] = formataddr((['liuri', 'liu18941113060@163.com']))
    # 主题
    mse['Subject']='test'


    # send e-mail
    sever=smtplib.SMTP_SSL('smtp.163.com')
    sever.login('liu18941113060@163.com','PGEWCRZXYPHQSDNE')
    sever.sendmail('liu18941113060@163.com','liu18941113060@163.com',mse.as_string())
    sever.quit()
send_e_mail()


# 发送多个邮件
# send_email("424662508@qq.com")
# send_email("424662509@qq.com")
# send_email("wupeiqi@live.com")
email_list=["424662508@qq.com","424662509@qq.com","wupeiqi@live.com"]