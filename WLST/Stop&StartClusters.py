#!/usr/bin/python

# weblogic variable
wls_user = 'weblogic'
wls_pwd = 'Welcome1'
host_name = 't3://127.0.0.1'
wls_port = '7001'
clusters = [
    {
        "name": "Cluster_1"
    },
    {
        "name": "Cluster_2"
    },
    {
        "name": "Cluster_3"
    },
    {
        "name": "Cluster_4"
    },
    {
        "name": "Cluster_5"
    }
]
connect(wls_user,wls_pwd,host_name+':'+wls_port)
nClusters = len(clusters)
for x in range(nClusters-1, -1, -1):
	cluster = clusters[x]
	clusterName = cluster['name']
	print 'stopping cluster ' + clusterName
	shutdown(name=clusterName, entityType='Cluster', block='true')
	print 'stopped cluster ' + clusterName

print 'stopped all BODG clusters'

for cluster in clusters:
	clusterName = cluster['name']
	print 'starting cluster ' + clusterName
	start(name=clusterName, type='Cluster', block='true')
	print 'started cluster ' + clusterName

print 'started all BODG clusters'
disconnect()
 


