#!/usr/bin/python

import os,sys
 
#----------SINGLETON CLUSTER CONFIGURATION----------

def configureSingleton(clusters):
	for clusterName in clusters:
		print 'Configure singleton cluster configuration'
		cluster_bean_path = getPath('com.bea:Name=' + clusterName + ',Type=Cluster');
		cluster = getMBean('/'+cluster_bean_path); 
		cluster.setMigrationBasis('consensus');  
		servers = cluster.getServers();  
		candidate_servers = [];  
		candidate_machines = [];  
		for server in servers:  
			server_object_name = ObjectName(repr(server.getObjectName()));  
			candidate_servers.append(server_object_name);  
			machine = server.getMachine();  
			machine_object_name = ObjectName(repr(machine.getObjectName()));  
			if machine_object_name not in candidate_machines:  
				candidate_machines.append(machine_object_name);
		cd('/Clusters/' + clusterName);
		set('CandidateMachinesForMigratableServers',jarray.array(candidate_machines, ObjectName));


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

		configureSingleton(settings.singletonServiceClusters)

		save()
		activate()
		disconnect()

	except Exception, e:
		print str(e)
		undo('true','y')

else:
    sys.exit(0)
