# Script to check the status of the rest api.
# Status : 200, 400, 500, 404. etc...


import requests
import smtplib
import os 


def send(status):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('<email_id>', "Password")
    server.sendmail(
      "FROM Address", 
      ["TO Address", "TO Address"], 
      "Alert Message!! Your Container is %s" % (status))
    server.quit()


url = 'http://<ip_address>/api/v1/data/'  


status = requests.head(url)   # This will do GET operation to the URL and holds the status of it. 

if status.status_code == 404:
  send("down")
elif status.status_code == 200:
	send("up")
else:
	print(status)