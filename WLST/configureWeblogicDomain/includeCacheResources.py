#!/usr/bin/python

from wlstModule import *
# Import di tutte le funzioni del file envConfig.py
from utilFunctions import *
from settingsResources import *
from settingsEnvironment import *

def createCoherenceCluster():
  if(notExistsCoherenceCluster(COHERENCE_CLUSTER_NAME)):
    # Create Coherence Cluster
    print 'INIT CONFIGURATION COHERENCE CLUSTER'
    cd('/')
    cohSR = create(COHERENCE_CLUSTER_NAME, 'CoherenceClusterSystemResource')
    print 'created coherence cluster '+COHERENCE_CLUSTER_NAME
    cohBean = cohSR.getCoherenceClusterResource()
    cohCluster = cohBean.getCoherenceClusterParams()
    cohCluster.setTransport('udp')
    cohCluster.setClusterListenPort(COHERENCE_CLUSTER_PORT)
    cmo = cd('/Clusters/' + CLUSTER_PROXY_NAME)
    cmo.setCoherenceClusterSystemResource(cohSR)
    cohSR.addTarget(cmo)
    cd('CoherenceTier/'+CLUSTER_PROXY_NAME)
    set('LocalStorageEnabled', 'false')
    cmo = cd('/Clusters/' + CLUSTER_DATA_NAME)
    cmo.setCoherenceClusterSystemResource(cohSR)
    cohSR.addTarget(cmo)
    print 'set local storage enabled to weblogic cluster '+ CLUSTER_DATA_NAME
    cd('CoherenceTier/'+CLUSTER_DATA_NAME)
    set('LocalStorageEnabled', 'true')
  else:
    print 'Coherence cluster ' + COHERENCE_CLUSTER_NAME + ' already exists'
  
def configStartParameters():
  
  print 'Configure start parameters on cluster '+ CLUSTER_APP_NAME
  cluster_bean_path = getPath('com.bea:Name=' + CLUSTER_APP_NAME + ',Type=Cluster');
  cluster = getMBean('/'+cluster_bean_path); 
  servers = cluster.getServers();  
  for server in servers:  
    ServerName = server.getName()  
    cmo=cd('/Servers/'+ServerName+'/ServerStart/'+ServerName)
    cmo.setArguments(ARGUMENTS_APP_SERVERS)

def envJMSConfiguration():
  # Create JMS Server
  if(notExistsJMSServer(JMS_SERVER_NAME)):
    createJMSResource(JMS_SERVER_NAME, 'JMSServer', '/Clusters/'+CLUSTER_APP_NAME)
  
    cmo=cd('/JMSServers/'+JMS_SERVER_NAME)
    print 'Created jms server bodg'
  else:
    print 'Jms server ' + JMS_SERVER_NAME + ' already exists'
  
  # Create JMS Module
  if(notExistsJMSModule(JMS_MODULE_NAME)):
    createJMSResource(JMS_MODULE_NAME, 'JMSSystemResource', '/Clusters/'+CLUSTER_APP_NAME)
    print 'Created bodg jms module'
    # Create sub-deployment in module Bodg
    createSubDeployment(SUB_DEPL_NAME, JMS_SERVER_NAME, JMS_MODULE_NAME)
    print 'Created bodg jms subdeployment'
  else:
    print 'Jms module ' + JMS_MODULE_NAME + ' already exists'
  
  # Create connection factory
  if(notExistsJMSConnFactory(JMS_MODULE_NAME, CONN_FACTORY_NAME)):
    createObject(CONN_FACTORY_NAME, JMS_MODULE_NAME, SUB_DEPL_NAME, 'ConnectionFactory')
    cd('/JMSSystemResources/'+JMS_MODULE_NAME+'/JMSResource/'+JMS_MODULE_NAME+'/ConnectionFactories/'+CONN_FACTORY_NAME+'/TransactionParams/'+CONN_FACTORY_NAME)
    set('XAConnectionFactoryEnabled', true)
    cmo=cd('/JMSSystemResources/'+JMS_MODULE_NAME+'/JMSResource/'+JMS_MODULE_NAME+'/ConnectionFactories/'+CONN_FACTORY_NAME+'/LoadBalancingParams/'+CONN_FACTORY_NAME)
    cmo.setServerAffinityEnabled(false)
    cmo.setLoadBalancingEnabled(true)
    print 'Created bodg connection factory'
  else:
    print 'Connection factory ' + CONN_FACTORY_NAME + ' already exists'
  
  # Create queues EVENTS
  if(notExistsJMSUDQueue(JMS_MODULE_NAME, EVENTS_QUEUE)):
    print 'Creating queue '+EVENTS_QUEUE
    createObject(EVENTS_QUEUE, JMS_MODULE_NAME, SUB_DEPL_NAME, 'UniformDistributedQueue')
    print 'Created queue '+EVENTS_QUEUE
    cd('/JMSSystemResources/'+JMS_MODULE_NAME+'/JMSResource/'+JMS_MODULE_NAME+'/UniformDistributedQueues/'+EVENTS_QUEUE+'/DeliveryFailureParams/'+EVENTS_QUEUE)
    set('RedeliveryLimit', REDELIVERY_LIMIT)
  else:
    print 'UniformDistributedQueue ' + EVENTS_QUEUE + ' already exists'
  
  if(notExistsJMSUDQueue(JMS_MODULE_NAME, EVENTS_PAGES_QUEUE)):
    print 'Creating queue '+EVENTS_PAGES_QUEUE
    createObject(EVENTS_PAGES_QUEUE, JMS_MODULE_NAME, SUB_DEPL_NAME, 'UniformDistributedQueue')
    print 'Created queue '+EVENTS_PAGES_QUEUE
  else:
    print 'UniformDistributedQueue ' + EVENTS_PAGES_QUEUE + ' already exists'

  
  # Create queues MARKETS
  if(notExistsJMSUDQueue(JMS_MODULE_NAME, MARKETS_QUEUE)):
    print 'Creating queue '+MARKETS_QUEUE
    createObject(MARKETS_QUEUE, JMS_MODULE_NAME, SUB_DEPL_NAME, 'UniformDistributedQueue')
    print 'Created queue '+MARKETS_QUEUE
    cd('/JMSSystemResources/'+JMS_MODULE_NAME+'/JMSResource/'+JMS_MODULE_NAME+'/UniformDistributedQueues/'+MARKETS_QUEUE+'/DeliveryFailureParams/'+MARKETS_QUEUE)
    set('RedeliveryLimit', REDELIVERY_LIMIT)
  else:
    print 'UniformDistributedQueue ' + MARKETS_QUEUE + ' already exists'
  
  if(notExistsJMSUDQueue(JMS_MODULE_NAME, MARKETS_PAGES_QUEUE)):
    print 'Creating queue '+MARKETS_PAGES_QUEUE
    createObject(MARKETS_PAGES_QUEUE, JMS_MODULE_NAME, SUB_DEPL_NAME, 'UniformDistributedQueue')
    print 'Created queue '+MARKETS_PAGES_QUEUE
  else:
    print 'UniformDistributedQueue ' + MARKETS_PAGES_QUEUE + ' already exists'

  if(notExistsJMSUDQueue(JMS_MODULE_NAME, EVENTS_MARKETS_PAGES_QUEUE)):
    print 'Creating queue '+EVENTS_MARKETS_PAGES_QUEUE
    createObject(EVENTS_MARKETS_PAGES_QUEUE, JMS_MODULE_NAME, SUB_DEPL_NAME, 'UniformDistributedQueue')
    print 'Created queue '+EVENTS_MARKETS_PAGES_QUEUE
  else:
    print 'UniformDistributedQueue ' + EVENTS_MARKETS_PAGES_QUEUE + ' already exists'
  
  # Create queues MARKET_ATTRIBUTE_QUEUE
  if(notExistsJMSUDQueue(JMS_MODULE_NAME, MARKET_ATTRIBUTE_QUEUE)):
    print 'Creating queue '+MARKET_ATTRIBUTE_QUEUE
    createObject(MARKET_ATTRIBUTE_QUEUE, JMS_MODULE_NAME, SUB_DEPL_NAME, 'UniformDistributedQueue')
    print 'Created queue '+MARKET_ATTRIBUTE_QUEUE
    cd('/JMSSystemResources/'+JMS_MODULE_NAME+'/JMSResource/'+JMS_MODULE_NAME+'/UniformDistributedQueues/'+MARKET_ATTRIBUTE_QUEUE+'/DeliveryFailureParams/'+MARKET_ATTRIBUTE_QUEUE)
    set('RedeliveryLimit', REDELIVERY_LIMIT)
  else:
    print 'UniformDistributedQueue ' + MARKET_ATTRIBUTE_QUEUE + ' already exists'

  
def envJDBCPersistentConfiguration():
  #----------DATASOURCE JDBC STORAGE----------
  if(notExistsJdbcDatasource(JDBC_STORAGE_DATA_SOURCE_NAME)):
    print 'Creating datasource JDBC STORAGE'
    cmo=cd('/')
    cmo.createJDBCSystemResource(JDBC_STORAGE_DATA_SOURCE_NAME)
    cmo=cd('/JDBCSystemResources/'+JDBC_STORAGE_DATA_SOURCE_NAME+'/JDBCResource/'+JDBC_STORAGE_DATA_SOURCE_NAME)
    cmo.setName(JDBC_STORAGE_DATA_SOURCE_NAME)
    cd('/JDBCSystemResources/'+JDBC_STORAGE_DATA_SOURCE_NAME+'/JDBCResource/'+JDBC_STORAGE_DATA_SOURCE_NAME+'/JDBCDataSourceParams/'+JDBC_STORAGE_DATA_SOURCE_NAME)
    set('JNDINames',jarray.array([String(JDBC_STORAGE_DATA_SOURCE_JNDI_NAME)], String))   
    cmo=cd('/JDBCSystemResources/'+JDBC_STORAGE_DATA_SOURCE_NAME+'/JDBCResource/'+JDBC_STORAGE_DATA_SOURCE_NAME+'/JDBCDriverParams/'+JDBC_STORAGE_DATA_SOURCE_NAME)
    cmo.setUrl(JDBC_STORAGE_DATA_SOURCE_URL)
    cmo.setDriverName( JDBC_STORAGE_DATA_SOURCE_DRIVER_NAME )
    cmo.setPassword(JDBC_STORAGE_DATA_SOURCE_PWD)
    cmo=cd('/JDBCSystemResources/'+JDBC_STORAGE_DATA_SOURCE_NAME+'/JDBCResource/'+JDBC_STORAGE_DATA_SOURCE_NAME+'/JDBCConnectionPoolParams/'+JDBC_STORAGE_DATA_SOURCE_NAME)
    cmo.setTestTableName(DATA_SOURCE_TEST_QUERY)
    cmo=cd('/JDBCSystemResources/'+JDBC_STORAGE_DATA_SOURCE_NAME+'/JDBCResource/'+JDBC_STORAGE_DATA_SOURCE_NAME+'/JDBCDriverParams/'+JDBC_STORAGE_DATA_SOURCE_NAME+'/Properties/'+JDBC_STORAGE_DATA_SOURCE_NAME )
    cmo.createProperty('user')
    cmo=cd('/JDBCSystemResources/'+JDBC_STORAGE_DATA_SOURCE_NAME+'/JDBCResource/'+JDBC_STORAGE_DATA_SOURCE_NAME+'/JDBCDriverParams/'+JDBC_STORAGE_DATA_SOURCE_NAME+'/Properties/'+JDBC_STORAGE_DATA_SOURCE_NAME+'/Properties/user')
    cmo.setValue(JDBC_STORAGE_DATA_SOURCE_USER)
    cmo=cd('/JDBCSystemResources/'+JDBC_STORAGE_DATA_SOURCE_NAME+'/JDBCResource/'+JDBC_STORAGE_DATA_SOURCE_NAME+'/JDBCDataSourceParams/'+JDBC_STORAGE_DATA_SOURCE_NAME)
    cmo.setGlobalTransactionsProtocol('none')
    cd('/SystemResources/'+JDBC_STORAGE_DATA_SOURCE_NAME)
    set('Targets',jarray.array([ObjectName('com.bea:Name='+CLUSTER_APP_NAME+',Type=Cluster') ], ObjectName))
  else:
    print 'Jdbc datasource ' + JDBC_STORAGE_DATA_SOURCE_NAME + ' already exists'

def overrideCoherenceConfigFile():
  if(notExistsCoherenceConfig(COHERENCE_CLUSTER_NAME, BO_COH_CONFIG_NAME)):
    print 'Override coherence config files'
    cd('/CoherenceClusterSystemResources/'+COHERENCE_CLUSTER_NAME+'/CoherenceCacheConfigs')
    create(BO_COH_CONFIG_NAME, 'CoherenceCacheConfig')
    cmo = cd(BO_COH_CONFIG_NAME)
    set('JNDIName',BO_COH_CONFIG_JNDI_NAME)
    print(BO_COH_CONFIG_SOURCE_FILE);
    cmo.importCacheConfigurationFile(BO_COH_CONFIG_SOURCE_FILE)
    cmo.addTarget(getMBean('/Clusters/'+CLUSTER_PROXY_NAME))
  else:
    print 'Coherence config ' + BO_COH_CONFIG_NAME + ' already exists'
  
  
  
 
 
