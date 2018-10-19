#!/usr/bin/python
import sys
#import settings as settings

def createCluster(clusters):

	print clusters
	for cluster in clusters:
		name = cluster['name']
		messagingMode = cluster['messagingMode']

		print 'INIT CONFIGURATION CLUSTER ' + name
		cd('/')
		myMBean = getMBean('/Clusters/'+name)
		if (myMBean is None):
			create(name,'Cluster')
			cd('Clusters/'+name)
			set('ClusterMessagingMode', messagingMode)
			if 'address' in cluster:
				set('ClusterAddress', cluster['address'])
			print 'created cluster ' + name
		else:
			print 'cluster '+ name +' already exists'

def createManaged(managedServers):

	print managedServers
	for managed in managedServers:
		server = managed['server']
		machine = managed['machine']
		cluster = managed['cluster']
		port = managed['port']
		sslPort = managed['sslPort']

		print 'INIT CONFIGURATION MANAGED ' + server
		cd('/')
		myMBean = getMBean('/Servers/'+server)
		if (myMBean is None):
			create(server,'Server')
			cd('/Servers/'+ server)
			print 'set machine to server ' + server
			cmo.setMachine(getMBean('/Machines/' +  machine))
			print 'set cluster to server ' + server
			cmo.setCluster(getMBean('/Clusters/' + cluster))
			print 'set listen port to server ' + server
			cmo.setListenPort(port)
			cd('SSL/' + server)
			cmo.setListenPort(sslPort)
			print 'created server '+ server
		else:
			print 'server '+ server +' already exists'
		
if __name__=="main":

	if len(sys.argv) == 1:
		print "Missing configuration path. 'configureDomain.py settings_SYSINT'"
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

		createCluster(settings.clusters)
		createManaged(settings.managedServers)

		save()
		activate()
		disconnect()

	except Exception, e:
		print str(e)
		undo('true','y')

else:
    sys.exit(0)

