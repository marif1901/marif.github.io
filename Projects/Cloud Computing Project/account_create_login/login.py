#!/usr/bin/python
import time
import os
def log():
				os.system("dialog  --inputbox 'Enter username' 10 40  2> /tmp/user")
				os.system("dialog  --passwordbox 'Enter password(case-sensitive)' 10 40  2> /tmp/pass")
				fhuser=open("/tmp/user", "r")
				user=fhuser.read()
				fhuser.close()

				fhpass=open("/tmp/pass", "r")
				passwd=fhpass.read()
				fhpass.close()

				fhcheck=open("/etc/passwd","r")
				k=0
				for i in  fhcheck :
					if (user==i.split(":")[0]):
						os.system("dialog  --infobox 'Logged in successfully' 10 40")
						time.sleep(0.5)
						k+=1
						break
				fhcheck.close()
				#'''wanna check password?'''
			
				os.system("cut -d: -f1 /etc/passwd | wc -l  2> /tmp/num_users ")
				fhnum=open("/tmp/num_users","r")
				num=fhnum.read()
				fhnum.close()
				if k==int(num):
					os.system("dialog --infobox '.....entered username/password mismatch.....' 10 40")
					time.sleep(1)
					os.system("dialog  --yesno 'Want to try again' 10 40")

					os.system("echo $?  2> /tmp/yn ")
					fhyn=open("/tmp/yn","r")
					yn=fhyn.read()
					fhyn.close()

					if int(yn)==0 :
						log()
					else:
						os.system("exit")
log()

