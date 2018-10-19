#!/usr/bin/python

import os,sys

def createWorkManager(workManagers):

	for workManager in workManagers:
		domainName = workManager['domainName']
		name = workManager['name']
		cluster = workManager['cluster']

		print '======= Creating a WorkManager Kafka ======='
		cd('edit:/SelfTuning/' + domainName + '/WorkManagers/')
		myMBean = getMBean('edit:/SelfTuning/' + domainName + '/WorkManagers/' + name)
		if (myMBean is None):
			create(name,'WorkManagers')
			cd('edit:/SelfTuning/' + domainName + '/WorkManagers/' + name)
			#cmo.addTarget(getMBean("/Servers/"+ targetServerName))
			cmo.addTarget(getMBean("/Clusters/"+ cluster))
			print ' WorkManager Created...'
			cd('/SelfTuning/'+domainName+'/WorkManagers/' + name)
			cmo.setIgnoreStuckThreads(true)
			print ' Ignore Stuck Threads setted...'
		else:
			print 'workManager '+ name +' already exists'
	

def createManagedExecutorServiceTemplate(managedExecutorServiceTemplates):

	for mest in managedExecutorServiceTemplates:
		
		domainName = mest['domainName']
		name = mest['name']
		cluster = mest['cluster']
		dispatchPolicy = mest['dispatchPolicy']

		print '======= Creating a Managed Executor Kafka ======='
		cd('/')
		myMBean = getMBean('/ManagedExecutorServiceTemplates/'+name)
		if (myMBean is None):
			cmo.createManagedExecutorServiceTemplate(name)
			cd('/ManagedExecutorServiceTemplates/'+name)
			cmo.setLongRunningPriority(5)
			cmo.setMaxConcurrentLongRunningRequests(10)
			cmo.setDispatchPolicy(dispatchPolicy)
			set('Targets',jarray.array([ObjectName('com.bea:Name='+cluster+',Type=Cluster')], ObjectName))
			print ' ManagedExecutor Kafka Created...'
		else:
			print 'ManagedExecutor '+ name +' already exists'

if __name__=="main":

	if len(sys.argv) == 1:
		print "Missing configuration path. 'configureSingletonService.py settings_SYSINT (senza estensione)'"
		sys.exit(0);		

	print "Loading settings <" + str(sys.argv[1]) + ">"
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

		createWorkManager(settings.workManagers)
		createManagedExecutorServiceTemplate(settings.managedExecutorServiceTemplates)

		save()
		activate()
		disconnect()

	except Exception, e:
		print str(e)
		undo('true','y')

else:
    sys.exit(0)


#	print '======= Creating MaxThreadsConstraint ======='
#	cd('edit:/SelfTuning/' + domainName + '/MaxThreadsConstraints/')
#	create(maxThreadConstraintName,'MaxThreadsConstraints')
#	cd('edit:/SelfTuning/' + domainName + '/MaxThreadsConstraints/' + maxThreadConstraintName)
#	#cmo.addTarget(getMBean("/Servers/"+ targetServerName))
#	cmo.addTarget(getMBean("/Clusters/"+ clusterName))
#	set('Count',maxThread)
#	print ' MaxThreadsConstraint Created...'
	
#	print '======= Assigning the MaxThreadConstraint to the WorkManager ======='
#	cd('edit:/SelfTuning/' + domainName + '/WorkManagers/' + workManagerName)
#	bean=getMBean('/SelfTuning/' + domainName + '/MaxThreadsConstraints/' + maxThreadConstraintName)
#	cmo.setMaxThreadsConstraint(bean)
#	print ' Assigned MaxThreadsConstraint...'
	
#	print '======= Creating MinThreadsConstraint ======='
#	cd('edit:/SelfTuning/' + domainName + '/MinThreadsConstraints/')
#	create(minThreadConstraintName,'MinThreadsConstraints')
#	cd('edit:/SelfTuning/' + domainName + '/MinThreadsConstraints/' + minThreadConstraintName)
#	cmo.addTarget(getMBean("/Servers/"+ ServerName))
#	set('Count',minThread)
#	print ' MinThreadsConstraint Created...'
	
#	print '======= Assigning the MinThreadConstraint to the WorkManager ======='
#	cd('edit:/SelfTuning/' + domainName + '/WorkManagers/' + workManagerName)
#	bean=getMBean('/SelfTuning/' + domainName + '/MinThreadsConstraints/' + minThreadConstraintName)
#	cmo.setMinThreadsConstraint(bean)
#	print ' Assigned MinThreadsConstraint...'