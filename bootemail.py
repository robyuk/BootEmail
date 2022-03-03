#! /usr/bin/env /usr/bin/python3

import yagmail
import os
from datetime import datetime
import socket

sender='automailry@gmail.com'
receiver='youngr2000-001@yahoo.com'
lastlog='/var/log/syslog.1'
curlog='/var/log/syslog'

def subject():
  nwinfo=socket.gethostbyname_ex(socket.gethostname())
  return 'Rebooted: '+nwinfo[0]+': '+str(nwinfo[2])


now=datetime.now()
#print(subject())

content=[str(now),lastlog,curlog]

yag=yagmail.SMTP(user=sender, password=os.getenv('automailrypw'))
yag.send(to=receiver, subject=subject(), contents=content)
print("Email sent.")
