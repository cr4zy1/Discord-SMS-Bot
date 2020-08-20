import smtplib
import config


def send_email(subj, msg, reciever):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subj,msg)
        server.sendmail(config.EMAIL_ADDRESS,reciever, message)
        server.quit()
        return 1
    except:
       return 0


