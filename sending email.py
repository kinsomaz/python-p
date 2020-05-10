#sending email
import smtplib
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('kinsomaz88@gmail.com', 'pwufkqwikektsgvm')
smtpObj.sendmail('kinsomaz88@gmail.com', 'maryamakinlade0@gmail.com', 'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
smtpObj.quit()
