import os
import time

source = ["/Users/jack/projects/py_learn"]

target_dir = "/Users/jack/projects/"

target_name = target_dir  + time.strftime("%Y%m%d%H%M%S") + '01.zip'

zip_command = "zip -qr '%s' %s" %(target_name,' '.join(source))

if os.system(zip_command) == 0:
	print ("Successful backup to: ",target_name)
else:
	print ("Backup FAILED")


