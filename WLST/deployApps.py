#!/usr/bin/python
import sys

def deployApps(apps):

	print 'Deploy apps:'
	print apps
	for app in apps:
		appName = app['appName']
		path = app['path']
		cluster_target = app['cluster']
		#print 'Deploy ' + appName + ' - ' + path + ' - ' + cluster_target
		
		myMBean = getMBean('edit:/AppDeployments/'+ appName)
		if (myMBean is None):
			wslt_progress = deploy(appName, path, cluster_target)
		else:
			wslt_progress = redeploy(appName, appPath=path)
			
		wslt_progress.printStatus()
	print 'deployed all BODG modules'
	
if __name__=="main":

	if len(sys.argv) == 1:
		print "Missing configuration path. 'deployBodgApps.py settings_SYSINT'"
		sys.exit(0);		

	print sys.argv[0]
	settings = __import__(sys.argv[1])

	if settings.wl != None:
		WL_HOST_PORT = settings.wl['hostAndPort']
		WLUSER = settings.wl['user']
		WLPASSWORD = settings.wl['password']
	else:
		WL_HOST_PORT=raw_input('Insert Weblogic host and port: ')
		WLUSER=raw_input('Insert Weblogic user: ')
		WLPASSWORD=raw_input('Insert Weblogic Password: ')
   
	try:

		connect(WLUSER, WLPASSWORD, WL_HOST_PORT)
		edit()
		startEdit()

		deployApps(settings.apps)

		save()
		activate()
		disconnect()

	except Exception, e:
		print str(e)
		undo('true','y')

else:
    sys.exit(0)