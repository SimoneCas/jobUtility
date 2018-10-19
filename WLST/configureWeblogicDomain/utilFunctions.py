from wlstModule import *

def createJMSResource(name, type, path):
  cd('/')
  srvr = create(name, type)
  srvr.addTarget(getMBean(path))

def createSubDeployment(name, server, module):
  objModule = getMBean("/SystemResources/"+module)
  objModule.createSubDeployment(name)
  cd("/SystemResources/"+module+'/SubDeployments/'+name)
  serverList=[ObjectName(str('com.bea:Name='+server+',Type=JMSServer'))]
  set('Targets', jarray.array(serverList, ObjectName))

def createObject(name, module, subdeployment, type):
  cd('/JMSSystemResources/'+module+'/JMSResource/'+module)
  myob=create(name, type)
  myob.setJNDIName("jms/"+name)
  myob.setSubDeploymentName(subdeployment)

def notExistsCoherenceCluster(clusterName):
  myMBean = getMBean('/CoherenceClusterSystemResources/' + clusterName)
  if (myMBean is None):
    return true
  return false

def notExistsJMSServer(jmsServerName):
  myMBean = getMBean('/JMSServers/' + jmsServerName)
  if (myMBean is None):
    return true
  return false

def notExistsJMSModule(jmsModuleName):
  myMBean = getMBean('/JMSSystemResources/' + jmsModuleName)
  if (myMBean is None):
    return true
  return false

def notExistsJMSConnFactory(jmsModuleName, jmsResourceName):
  myMBean = getMBean('/JMSSystemResources/'+jmsModuleName+'/JMSResource/'+jmsModuleName+'/ConnectionFactories/'+jmsResourceName)
  if (myMBean is None):
    return true
  return false

def notExistsJMSUDQueue(jmsModuleName, jmsResourceName):
  myMBean = getMBean('/JMSSystemResources/'+jmsModuleName+'/JMSResource/'+jmsModuleName+'/UniformDistributedQueues/'+jmsResourceName)
  if (myMBean is None):
    return true
  return false

def notExistsJdbcDatasource(datasourceName):
  myMBean = getMBean('/JDBCSystemResources/'+datasourceName)
  if (myMBean is None):
    return true
  return false

def notExistsCoherenceConfig(clusterName, configName):
  myMBean = getMBean('/CoherenceClusterSystemResources/'+clusterName+'/CoherenceCacheConfigs/'+configName)
  if (myMBean is None):
    return true
  return false