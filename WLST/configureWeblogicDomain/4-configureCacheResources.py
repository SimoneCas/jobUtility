#!/usr/bin/python

# Import di tutte le funzioni del file envConfig.py
from includeCacheResources import *
from settingsEnvironment import *


print 'Start interaction mode'

WLUSER=raw_input('Insert Weblogic user: ')
WLPASSWORD=raw_input('Insert Weblogic Password: ')

# ENV CONFIGURATION
connect(WLUSER,WLPASSWORD, 't3://' + HOST_NAME + ':' + WLS_PORT)

try:
	edit()
	startEdit()
	createCoherenceCluster()
	configStartParameters()
	envJMSConfiguration()
	envJDBCPersistentConfiguration()
	overrideCoherenceConfigFile()
	save()
	activate()


	disconnect()
	
except Exception,e:
	print str(e)
	undo('true','y')
