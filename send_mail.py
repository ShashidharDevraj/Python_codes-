# Script to send an email notification if the given IP is down. 
# This fails to work for Gmail due to security constraints. 
# Works for office Configured Gmail, Outlook.

import os 
import smtplib

def send(status):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)   # Connect to server using SSL. 
    server.login('<email_id>', "<Password>")
    server.sendmail(
      "<FROM Address>", 
      ["To Address", "To Address"], 
      "Alert Message!! Your Container %s is %s" % (i, status))
    server.quit()



ips = ["52.37.52.175", "10.95.11.227", "54.203.159.52", "54.214.224.142"]

for i in ips:
    status = os.system("ping -c 3 %s" % i)  # Ping for the IP for 3 times. 
    if status == 256:
        send("down")
