from wlstModule import *
# VERSION: 0.0.1

def create_jms_servers(jms_servers):
  for jms_server in jms_servers:
    create_jms_server(jms_server)


def create_jms_server(jms_server):
  jms_server_name = jms_server['name']
  cluster_name = jms_server['target_cluster']
  persistent_store_name = jms_server.get('persistent_store_name', None)
  
  if(not_exists_jms_server(jms_server_name)):
    create_jms_resource(jms_server_name, 'JMSServer', '/Clusters/'+cluster_name)
    print 'Created jms server ' + jms_server_name
  else:
    print 'Jms server ' + jms_server_name + ' already exists'

  cmo=cd('/JMSServers/'+jms_server_name)

  if (persistent_store_name is not None):
    cmo.setPersistentStore(getMBean('/JDBCStores/'+persistent_store_name))
  else:
    cmo.setPersistentStore(persistent_store_name)

  
def not_exists_jms_server(jmsServerName):
  myMBean = getMBean('/JMSServers/' + jmsServerName)
  if (myMBean is None):
    return true
  return false
  

def create_jms_modules(jms_modules):
  for jms_module in jms_modules:
    create_jms_module(jms_module)


def create_jms_module(jms_module):
  jms_module_name = jms_module['name']
  cluster_name = jms_module['target_cluster']
  if(not_exists_jms_module(jms_module_name)):
    create_jms_resource(jms_module_name, 'JMSSystemResource', '/Clusters/'+cluster_name)
    print 'Created jms module ' + jms_module_name
  else:
    print 'Jms module ' + jms_module_name + ' already exists'
  create_sub_deployments(jms_module_name, jms_module.get('sub_deployments', []))
  create_connection_factories(jms_module_name, jms_module.get('connection_factories', []))
  create_distributed_queues(jms_module_name, jms_module.get('distributed_queues', []))
  create_foreign_servers(jms_module_name, jms_module.get('foreign_servers', []))

  
def create_sub_deployments(jms_module_name, sub_deployments):
  for sub_deployment in sub_deployments:
    create_sub_deployment(jms_module_name, sub_deployment)


def create_sub_deployment(jms_module_name, sub_deployment):
  name = sub_deployment['name']
  server = sub_deployment['target_jms_server']
  if not_exists_sub_deployment(jms_module_name, name):
    objModule = getMBean('/SystemResources/'+jms_module_name)
    objModule.createSubDeployment(name)
    print 'Created sub-deployment ' + name
  else:
    print 'Jms sub-deployment ' + name + ' already exists'
  cd('/SystemResources/'+jms_module_name+'/SubDeployments/'+name)
  serverList = [ObjectName(str('com.bea:Name='+server+',Type=JMSServer'))]
  set('Targets', jarray.array(serverList, ObjectName))


def not_exists_sub_deployment(jms_module_name, sub_deployment_name):
  myMBean = getMBean('/SystemResources/'+jms_module_name+'/SubDeployments/'+sub_deployment_name)
  if (myMBean is None):
    return true
  return false


def create_jms_resource(name, type, target_path):
  cd('/')
  res = create(name, type)
  res.addTarget(getMBean(target_path))


def create_connection_factories(jms_module_name, connection_factories):
  for connection_factory in connection_factories:
    create_connection_factory(jms_module_name, connection_factory)


def create_connection_factory(jms_module_name, connection_factory):
  conn_factory_name = connection_factory['name']
  sub_depl_name = connection_factory['sub_deployment']
  if(not_exists_jms_conn_factory(jms_module_name, conn_factory_name)):
    create_jms_object(conn_factory_name, jms_module_name, sub_depl_name, 'ConnectionFactory')
    print 'Created connection factory ' + conn_factory_name
  else:
    print 'Connection factory ' + conn_factory_name + ' already exists'
  cd('/JMSSystemResources/'+jms_module_name+'/JMSResource/'+jms_module_name+'/ConnectionFactories/'+conn_factory_name+'/TransactionParams/'+conn_factory_name)
  set('XAConnectionFactoryEnabled', connection_factory['XAConnectionFactoryEnabled'])
  cmo=cd('/JMSSystemResources/'+jms_module_name+'/JMSResource/'+jms_module_name+'/ConnectionFactories/'+conn_factory_name+'/LoadBalancingParams/'+conn_factory_name)
  cmo.setServerAffinityEnabled(connection_factory['ServerAffinityEnabled'])
  cmo.setLoadBalancingEnabled(connection_factory['LoadBalancingEnabled'])

  
def create_jms_object(name, module, subdeployment, type):
  cd('/JMSSystemResources/'+module+'/JMSResource/'+module)
  myob=create(name, type)
  myob.setJNDIName("jms/"+name)
  myob.setSubDeploymentName(subdeployment)

  
def not_exists_jms_module(jmsModuleName):
  myMBean = getMBean('/JMSSystemResources/' + jmsModuleName)
  if (myMBean is None):
    return true
  return false

  
def not_exists_jms_conn_factory(jmsModuleName, jmsResourceName):
  myMBean = getMBean('/JMSSystemResources/'+jmsModuleName+'/JMSResource/'+jmsModuleName+'/ConnectionFactories/'+jmsResourceName)
  if (myMBean is None):
    return true
  return false


def create_distributed_queues(jms_module_name, queues):
  for queue in queues:
    create_distributed_queue(jms_module_name, queue)


def create_distributed_queue(jms_module_name, queue):
  queue_name = queue['name']
  sub_depl_name = queue['sub_deployment']
  if(not_exists_jms_ud_qeue(jms_module_name, queue_name)):
    print 'Creating queue '+queue_name
    create_jms_object(queue_name, jms_module_name, sub_depl_name, 'UniformDistributedQueue')
    print 'Created queue '+queue_name
  else:
    print 'UniformDistributedQueue ' + queue_name + ' already exists'
  cmo = cd('/JMSSystemResources/'+jms_module_name+'/JMSResource/'+jms_module_name+'/UniformDistributedQueues/'+queue_name+'/DeliveryFailureParams/'+queue_name)
  redelivery_limit = queue.get('redelivery_limit',-1)
  set('RedeliveryLimit', redelivery_limit)
  errorDestinationName = queue.get('error_destination', None)
  if (errorDestinationName is not None):
    errorDestination = getMBean('/JMSSystemResources/'+jms_module_name+'/JMSResource/'+jms_module_name+'/UniformDistributedQueues/'+errorDestinationName)
    set('ErrorDestination', errorDestination)
    print 'Dead letter queue set to: '+errorDestinationName
  else:
    cmo.unSet('ErrorDestination')
    print 'Dead letter queue unset'
  cd('/JMSSystemResources/'+jms_module_name+'/JMSResource/'+jms_module_name+'/UniformDistributedQueues/'+queue_name+'/DeliveryParamsOverrides/'+queue_name)
  redelivery_delay = queue.get('redelivery_delay',-1)
  set('RedeliveryDelay', redelivery_delay)
  time_to_deliver = queue.get('time_to_deliver',-1)
  set('TimeToDeliver', time_to_deliver)

def create_foreign_servers(jms_module_name, foreign_servers):
  for current in foreign_servers:
    create_foreign_server(jms_module_name, current)

def create_foreign_connection_factories(jms_module_name, foreign_server_name, connection_factories):
  for current in connection_factories:
    create_foreign_connection_factory(jms_module_name, foreign_server_name, current)

def create_foreign_destinations(jms_module_name, foreign_server_name, foreign_destinations):
  for current in foreign_destinations:
    create_foreign_destination(jms_module_name, foreign_server_name, current)

def create_foreign_server(jms_module_name, foreign_server):
  foreign_server_name = foreign_server['name']
  initial_context_factory = foreign_server['initial_context_factory']
  data_source_jndi_name = foreign_server['data_source_jndi_name']
  connection_factories = foreign_server.get('connection_factories', [])
  foreign_destinations = foreign_server.get('destinations', [])
  
  cmo=cd('/JMSSystemResources/'+jms_module_name+'/JMSResource/'+jms_module_name)
  if(not_exists_foreign_server(jms_module_name, foreign_server_name)):
    print 'Creating Foreign Server '+foreign_server_name
    cmo.createForeignServer(foreign_server_name)
    print 'Created Foreign Server '+foreign_server_name
  else:
    print 'Foreign Server ' + foreign_server_name + ' already exists'
  cmo=cd('/JMSSystemResources/'+jms_module_name+'/JMSResource/'+jms_module_name+'/ForeignServers/'+foreign_server_name)
  cmo.setDefaultTargetingEnabled(true)
  cmo.setInitialContextFactory(initial_context_factory)
  if(not_exists_foreign_server_datasource_jndi(jms_module_name, foreign_server_name)):
    cmo.createJNDIProperty('datasource')
  cmo=cd('/JMSSystemResources/'+jms_module_name+'/JMSResource/'+jms_module_name+'/ForeignServers/'+foreign_server_name+'/JNDIProperties/datasource')
  cmo.setValue(data_source_jndi_name)
  
  create_foreign_connection_factories(jms_module_name, foreign_server_name, connection_factories)
  create_foreign_destinations(jms_module_name, foreign_server_name, foreign_destinations)
 

def create_foreign_connection_factory(jms_module_name, foreign_server_name, connection_factory):
  connection_factory_name = connection_factory['name']
  remote_jndi_name = connection_factory['remote_jndi_name']
  local_jndi_name = connection_factory['local_jndi_name']
  
  cmo=cd('/JMSSystemResources/'+jms_module_name+'/JMSResource/'+jms_module_name+'/ForeignServers/'+foreign_server_name)
  
  if(not_exists_foreign_server_connection_factory(jms_module_name, foreign_server_name, connection_factory_name)):
     print 'Creating Foreign Connection Factory '+connection_factory_name
     cmo.createForeignConnectionFactory(connection_factory_name)
     print 'Created Foreign Connection Factory '+connection_factory_name
  else:
    print 'Foreign Connection Factory ' + foreign_server_name + ' already exists'
  
  cmo=cd('/JMSSystemResources/'+jms_module_name+'/JMSResource/'+jms_module_name+'/ForeignServers/'+foreign_server_name+'/ForeignConnectionFactories/'+connection_factory_name)
  cmo.setLocalJNDIName(local_jndi_name)
  cmo.setRemoteJNDIName(remote_jndi_name)
  
def create_foreign_destination(jms_module_name, foreign_server_name, foreign_destinations):
  destination_name = foreign_destinations['name']
  remote_jndi_name = foreign_destinations['remote_jndi_name']
  local_jndi_name = foreign_destinations['local_jndi_name']

  cmo=cd('/JMSSystemResources/'+jms_module_name+'/JMSResource/'+jms_module_name+'/ForeignServers/'+foreign_server_name)
  
  if(not_exists_foreign_server_destination(jms_module_name, foreign_server_name, destination_name)):
    print 'Creating Foreign Destination '+destination_name
    cmo.createForeignDestination(destination_name)
    print 'Created Foreign Destination '+destination_name
  else:
    print 'Foreign Destination' + foreign_server_name + ' already exists'
  
  cmo=cd('/JMSSystemResources/'+jms_module_name+'/JMSResource/'+jms_module_name+'/ForeignServers/'+foreign_server_name+'/ForeignDestinations/'+destination_name)
  cmo.setLocalJNDIName(local_jndi_name)
  cmo.setRemoteJNDIName(remote_jndi_name)
  
def perform_purge_queues(jms_modules, wl):
  
  for jms_module in jms_modules:
    
    print 'Purge queues starts, '+str(jms_module)
    
    jms_module_name = jms_module['name']
    queue_names = jms_module.get('queues', None)
    
    if (queue_names is None):#if None, search queues in jms module.
      queue_names = []
      jms_module_MBean = getMBean('/JMSSystemResources/'+jms_module_name+'/JMSResource/'+jms_module_name+'/');
      queues = jms_module_MBean.getUniformDistributedQueues()
      for queue in queues:
        #print 'queue: '+str(queue) 
        queue_names.append(queue.getName()) 

    queues_to_purge = []
    for queue_name in queue_names:
      cd('/JMSSystemResources/'+jms_module_name+'/JMSResource/'+jms_module_name+'/UniformDistributedQueues/'+queue_name)
      sub_deployment_name = get('SubDeploymentName')
      sub_deployment = getMBean('/SystemResources/'+jms_module_name+'/SubDeployments/'+sub_deployment_name)
      jms_servers = sub_deployment.getTargets() 
      for jms_server in jms_servers:
        jms_server_name = jms_server.getName()
        jms_server = getMBean('/SystemResources/'+jms_module_name+'/SubDeployments/'+sub_deployment_name+'/Targets/'+jms_server_name)
        clusters = jms_server.getTargets()
        for cluster in clusters:
          cluster_name = cluster.getName()
          cluster = getMBean('/SystemResources/'+jms_module_name+'/SubDeployments/'+sub_deployment_name+'/Targets/'+jms_server_name+'/Targets/'+cluster_name)
          managed_servers = cluster.getServers()
          for managed_server in managed_servers:
            managed_server_name = managed_server.getName()
            managed_server = getMBean('/SystemResources/'+jms_module_name+'/SubDeployments/'+sub_deployment_name+'/Targets/'+jms_server_name+'/Targets/'+cluster_name+'/Servers/'+managed_server_name)
            listen_port = managed_server.getListenPort()
            machine = managed_server.getMachine()
            host = machine.getName()
            queues_to_purge.append({'queue_name':queue_name,
                      'managed_server_name':managed_server_name,
                      'jms_server_name':jms_server_name,
            'jms_module_name':jms_module_name,
                      'host':host+':'+str(listen_port)})

    for queue_to_purge in queues_to_purge:
      #CONNECT TO MANAGED#
      connect(wl['user'], wl['password'], queue_to_purge['host'])
      cd('/')
      serverRuntime()
      queue = getMBean('/JMSRuntime/'+queue_to_purge['managed_server_name']+'.jms/JMSServers/'+queue_to_purge['jms_server_name']+'@'+queue_to_purge['managed_server_name']+'/Destinations/'+queue_to_purge['jms_module_name']+'!'+queue_to_purge['jms_server_name']+'@'+queue_to_purge['managed_server_name']+'@'+queue_to_purge['queue_name'])
      print '$$$ Performing purge: '+str(queue_to_purge)  
      print '$$$ MessagesCurrentCount: '+str(queue.getMessagesCurrentCount())
      print '$$$ MessagesPendingCount: '+str(queue.getMessagesPendingCount())
      print '$$$ Deleted message: '+str(queue.deleteMessages(''))
      disconnect()

def not_exists_foreign_server_destination(jms_module_name, foreign_server_name, destination_name):
  try:
    myMBean = getMBean('/JMSSystemResources/'+jms_module_name+'/JMSResource/'+jms_module_name+'/ForeignServers/'+foreign_server_name+'/ForeignDestinations/'+destination_name)
    if (myMBean is None):
      return true
    return false
  except:
    return true
  
  
def not_exists_foreign_server_connection_factory(jms_module_name, foreign_server_name, connection_factory_name):
  try:
    myMBean = getMBean('/JMSSystemResources/'+jms_module_name+'/JMSResource/'+jms_module_name+'/ForeignServers/'+foreign_server_name+'/ForeignConnectionFactories/'+connection_factory_name)
    if (myMBean is None):
      return true
    return false
  except:
    return true
  

def not_exists_foreign_server(jms_module_name, foreign_server_name):
  try:
    myMBean = getMBean('/JMSSystemResources/'+jms_module_name+'/JMSResource/'+jms_module_name+'/ForeignServers/'+foreign_server_name)
    if (myMBean is None):
      return true
    return false
  except:
    return true
 
 
def not_exists_foreign_server_datasource_jndi(jms_module_name, foreign_server_name):
  try:
    myMBean = getMBean('/JMSSystemResources/'+jms_module_name+'/JMSResource/'+jms_module_name+'/ForeignServers/'+foreign_server_name+'/JNDIProperties/datasource')
    if (myMBean is None):
      return true
    return false
  except:
    return true
 
  
def not_exists_jms_ud_qeue(jmsModuleName, jmsResourceName):
  try:
    myMBean = getMBean('/JMSSystemResources/'+jmsModuleName+'/JMSResource/'+jmsModuleName+'/UniformDistributedQueues/'+jmsResourceName)
    if (myMBean is None):
      return true
    return false
  except:
    return true