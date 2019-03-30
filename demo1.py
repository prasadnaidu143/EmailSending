# import math
# import random
# import smtplib
# import ssl
# email=input("enter ayour mail :")
#
# digits = "0123456789"
# OTP = ""
# for x in range(4):
#     OTP += digits[math.floor(random.random() * 10)]
# smtp_server = "smtp.gmail.com"
# port = 465
# From_mail = "prasadnaidu766@gmail.com"
# To_email = email
# e_password = "njzgvtdzgjruayoa"
# message = " Hello This Is Your OTP  For Registration: " + OTP + "Username :"
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#     server.login(From_mail, e_password)
#     server.sendmail(From_mail, To_email, message)
#
# print("message sent")
import smtplib
email_from="prasadnaidu766@gmail.com"
email_to="prasadchaitu766@gmail.com"
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_from,"cnjvwtoprlhfaqzj")
message="hi this is prasad sending from python"
server.sendmail(email_from,email_to,message)
server.quit()