import smtplib

my_email = "nevidim_kr@abv.bg"
password = "x"
connection = smtplib.SMTP("smtp.abv.bg", port=465)
connection.starttls() #Transport layer security, securing the connection
connection.login(user=my_email, password=password) #Logging in
connection.sendmail(from_addrs=my_email, to_addrs="Receiving mail", msg="Hello") #From - To
connection.close() # with smtplib.SMTP() as connection:

# N.B. - Check mail security settings using python code to send email - Less secure apps allowing, app password
#msg="Subject:TEXT\n\nMAIL_TEXT" - Sending an e-mail with Subject
