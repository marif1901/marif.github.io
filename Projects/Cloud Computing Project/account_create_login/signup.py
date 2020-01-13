#!/usr/bin/python
import time
import os
def signup():
				os.system("dialog  --inputbox 'Enter username' 10 40  2> /tmp/user")
				fhuser=open("/tmp/user", "r")
				user=fhuser.read()
				fhuser.close()
			
				fhcheck=open("/etc/passwd","r")
				for i in  fhcheck :
					if (user==i.split(":")[0]):
						os.system("dialog  --msgbox 'username already exists' 10 40")
						time.sleep(1)
						signup()
				fhcheck.close()

				os.system("dialog  --passwordbox 'Enter password(case-sensitive)' 10 40  2> /tmp/pass")
				fhpass=open("/tmp/pass", "r")
				passwd=fhpass.read()
				fhpass.close()
				#'''wanna update user?'''
signup()
