import smtplib

email = smtplib.SMTP('smtp.gmail.com', 587)
email.ehlo()
email.starttls()

sender = 'vitalnicholas@gmail.com'
password = '25/06/1993'
recipient = 'odaircibasc@hotmail.com'

message = 'this is a test email'.encode('utf-8')

email.login(sender, password)
email.sendmail(sender, recipient, message)
email.quit()