import smtplib

my_email = "yasnaabdi2024@gmail.com"
password = "jyxwweympqkcqxcz"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
         from_addr=my_email,
         to_addrs="yasnaabdi2024@gmail.com",
         msg="Hi"
     )

#import smtplib

#before @ is the identity of my email account and after is email provider identity
#my_email = "yasnaabdi2024@gmail.com"
#password = "jyxwweympqkcqxcz"


#with smtplib.SMTP("smtp.gmail.com") as connection:
#    #SECURITY
#    connection.starttls()
#    connection.login(user=my_email, password=password)
#    connection.sendmail(from_addr=my_email, to_addrs="yasnaabdi2003@gmail.com",
#                        msg="Subject:Hi!\n\nThis is the body")



## Sending Email with Python
# import smtplib
#
# my_email = "appbreweryinfo@gmail.com"
# password = "abcd1234()"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="appbrewerytesting@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )


## Working with date and time in Python
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)