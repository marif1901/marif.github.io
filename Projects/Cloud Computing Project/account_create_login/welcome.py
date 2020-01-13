#!/usr/bin/python
import os
import time
import thread
def install():
	os.system("yum install dialog -y &> /dev/null")
def welcome():
	os.system("dialog --pause 'waiting for the basic installation......' 30 40 10")
	os.system("dialog --infobox '.....set up is complete.....' 20 40")
	time.sleep(1)
	os.system("dialog --infobox '.....welcome to the worlds biggest cloud hub.....' 20 40")
	time.sleep(3)

	os.system("dialog --menu 'select ur choice' 20 50 2  1 'Login' 2 'Signup'   2> /tmp/log ")
	fhlog=open("/tmp/log","r")
	log=fhlog.read()
	fhlog.close()

	if int(log) == 1:
		import login
	elif int(log) == 2:
		import signup

thread.start_new_thread(install,())

thread.start_new_thread(welcome,())
while 1:
	pass



	

