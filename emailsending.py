import smtplib
content="hiiiiii how r u"
send_mail=['vamsikrishna8015@gmail.com','vamshikrishna6668@gmail.com']
server=smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login('vamsi9477@gmail.com','vamsi66@V')
for i in send_mail:
    server.sendmail('vamsi9477@gmail.com',i,content)
server.quit()