import smtplib

#enter the host and the port number
a=smtplib.SMTP('smtp.gmail.com',587)
#establish the connection
a.ehlo()
#start the connection
a.starttls()
a.login()