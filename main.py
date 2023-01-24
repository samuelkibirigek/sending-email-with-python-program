import smtplib

my_email = "senderemail@gmail.com"
# this is an apps password gotten from gmail security settings
my_password = "zfzrwixtiznixlyo"
receiver_email = "receiveremail@gmail.com"
the_message = "This email has been sent by a python program."

# Google will not work without a port number.Take Note.
connection = smtplib.SMTP("smtp.gmail.com", 587)
# This starts the transport layer security, tls. Means if intercepted the messages will be encrypted.
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(
    from_addr=my_email,
    to_addrs=receiver_email,
    msg=f"Subject:Testing SMTP with Python\n\n{the_message}"
)
connection.close()


