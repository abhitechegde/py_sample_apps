# Smtplib can be used in Python to send an e-mail
# no need to install anything SMTP will be pre installed
import smtplib

### variables 
# variable server is for smtp server address and a port number
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

# from and to email id
user_id = "example@gmail.com"
to = "example@gmail.com"  
message=" Hello, This is a test email from python SMTP server" # message to pass in teh body
password="password"
# Note: add user your email id, password and message here

server.login(user_id, password)
# login is for authenticate the user to log into gmail 

server.sendmail(user_id, to, message) 
print("Email Sent")

server.quit()

# smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials v2sm7195926pje.15 - gsmtp') 

# if you get the above error , go to your google account settings to allow less secure apps to access your account.  
# (It's not recommended because it might make it easier for someone to break into your account). if you want to allow access anyway, follow these steps:

# 1. Go to "Less Secure apps" section
# 2. next to "access for less secure apps," select Turn on.
# https://myaccount.google.com/lesssecureapps ---> Google Less Secure apps</a>