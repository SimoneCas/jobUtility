#!/usr/bin/python
import os,sys
from wlstModule import *
# VERSION: 0.0.1

def create_clusters(clusters):
  print "create_clusters " + str(clusters)

  for cluster in clusters:
    name = cluster['name']
    messaging_mode = cluster['messaging_mode']

    print 'init configuration cluster ' + name

    if (not_exists_cluster(name)):
      cd('/')
      create(name,'Cluster')
      cd('Clusters/'+name)
      set('ClusterMessagingMode', messaging_mode)
      if 'address' in cluster:
        set('ClusterAddress', cluster['address'])
      print 'created cluster ' + name
    else:
      print 'cluster '+ name +' already exists'

def create_managed_servers(managed_servers):
  print "create_managed_servers " + str(managed_servers)

  for managed in managed_servers:
    server = managed['server']
    machine = managed['machine']
    cluster = managed['cluster']
    port = managed['port']
    ssl_port = managed['ssl_port']
    muxer_class = managed.get('muxer_class','weblogic.socket.NIOSocketMuxer')
    unicast_listen_address = managed.get('unicast_listen_address')

    cd('/Machines/'+machine+'/NodeManager/'+machine)
    listen_address = get('ListenAddress')

    print 'init configuration managed server ' + server

    if (not_exists_managed(server)):
      cd('/')
      create(server,'Server')
      print 'created server '+ server
    else:
      print 'server '+ server +' already exists'
    cmo = cd('/Servers/'+ server)
    print 'set machine to server ' + server
    cmo.setMachine(getMBean('/Machines/' +  machine))
    print 'set cluster to server ' + server
    cmo.setCluster(getMBean('/Clusters/' + cluster))
    print 'set listen port to server ' + server
    cmo.setListenPort(port)
    cmo.setListenAddress(listen_address)
    cmo.setMuxerClass(muxer_class)
    cmo = cd('SSL/' + server)
    cmo.setListenPort(ssl_port)
    diagnosticContextEnabled = managed.get('diagnostic_context_enabled', True)
    cmo = cd('/Servers/'+ server + '/ServerDiagnosticConfig/' + server)
    cmo.setDiagnosticContextEnabled(diagnosticContextEnabled)
    if(unicast_listen_address is not None):
      cmo.setUnicastListenAddress(unicast_listen_address)


def create_coherence_clusters(coherence_clusters):
  print "create_coherence_clusters " + str(coherence_clusters)

  for current in coherence_clusters:
    coherence_cluster_name = current['coherence_cluster_name']
    coherence_cluster_port = current['coherence_cluster_port']
    cluster_data_name = current['cluster_data_name']
    cluster_proxy_name = current.get('cluster_proxy_name', None)
    cluster_app_name = current.get('cluster_app_name', None)
    wka = current.get('wka', None)

    print 'init configuration coherence cluster ' + coherence_cluster_name

    cd('/')
    if(not_exists_coherence_cluster(coherence_cluster_name)):
      # Create Coherence Cluster
      print 'creating coherence cluster '+coherence_cluster_name
      cohSR = create(coherence_cluster_name, 'CoherenceClusterSystemResource')
      print 'created coherence cluster '+coherence_cluster_name
    else:
      print 'Coherence cluster ' + coherence_cluster_name + ' already exists'
      cohSR = getMBean('/CoherenceClusterSystemResources/' + coherence_cluster_name)

    cohBean = cohSR.getCoherenceClusterResource()
    cohCluster = cohBean.getCoherenceClusterParams()
    cohCluster.setTransport('udp')
    cohCluster.setClusterListenPort(coherence_cluster_port)
    if (cluster_proxy_name is not None):
      cmo = cd('/Clusters/' + cluster_proxy_name)
      cmo.setCoherenceClusterSystemResource(cohSR)
      cohSR.addTarget(cmo)
      cd('CoherenceTier/'+cluster_proxy_name) 
      set('LocalStorageEnabled', 'false')
    if (cluster_app_name is not None):
      cmo = cd('/Clusters/' + cluster_app_name)
      cmo.setCoherenceClusterSystemResource(cohSR)
      cohSR.addTarget(cmo)
      cd('CoherenceTier/'+cluster_app_name) 
      set('LocalStorageEnabled', 'false')
    cmo = cd('/Clusters/' + cluster_data_name)
    cmo.setCoherenceClusterSystemResource(cohSR)
    cohSR.addTarget(cmo)
    print 'set local storage enabled to weblogic cluster '+ cluster_data_name
    cd('CoherenceTier/'+cluster_data_name)
    set('LocalStorageEnabled', 'true')
  
    if (wka is not None):
      print 'Add known Coherence Cluster addresses';
      cmo = cd('/CoherenceClusterSystemResources/' + coherence_cluster_name + '/CoherenceClusterResource/' + coherence_cluster_name + '/CoherenceClusterParams/' + coherence_cluster_name + '/CoherenceClusterWellKnownAddresses/' + coherence_cluster_name);
      for i in range(len(wka)):
        if(not_exists_coherence_wka(coherence_cluster_name,'WKA-' + str(i))):
          print 'create '+'WKA-' + str(i) + ' : ' + wka[i]
          cmo.createCoherenceClusterWellKnownAddress('WKA-' + str(i));
        address = cmo.lookupCoherenceClusterWellKnownAddress('WKA-' + str(i));
        address.setListenAddress(wka[i]);


def config_jvm_start_parameters(server_jvm_parameters):
  print "config_start_parameters " + str(server_jvm_parameters)
  for current in server_jvm_parameters:
    cluster_name = current['cluster_name']
    arguments = current['arguments']
    managed_servers = current.get('servers', None)

    print 'init configuration start parameters ' + cluster_name

    cluster_bean_path = getPath('com.bea:Name=' + cluster_name + ',Type=Cluster');
    cluster = getMBean('/'+cluster_bean_path); 
    servers = cluster.getServers();  
    for server in servers:
      server_name = server.getName()  
      cmo=cd('/Servers/'+server_name+'/ServerStart/'+server_name)
      argsSetted = False
      
      if (managed_servers is not None):
        for managed_server in managed_servers:
          managed_server_name = managed_server['managed_name']
          managed_server_arg = managed_server['arguments']
          if (managed_server_name == server_name):
            argsSetted = True
            cmo.setArguments(arguments +  ' ' + managed_server_arg)

      if (not argsSetted):
        cmo.setArguments(arguments)


def configure_migratable_clusters(migratable_clusters):
  print "configure_migratable_clusters " + str(migratable_clusters)
  for current in migratable_clusters:
    cluster_name = current['cluster_name']
    data_source_name = current.get('data_source_name', None)
    if (data_source_name is None):
        migration_basis = 'consensus'
        table_name = None
    else:
        migration_basis = 'database'
        table_name = current.get('table_name', 'ACTIVE')
    
    print 'init configure migratable cluster '+ cluster_name

    cluster_bean_path = getPath('com.bea:Name=' + cluster_name + ',Type=Cluster');
    cluster = getMBean('/'+cluster_bean_path);   
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
    cd('/Clusters/' + cluster_name);
    cluster.setMigrationBasis(migration_basis);
    set('CandidateMachinesForMigratableServers',jarray.array(candidate_machines, ObjectName));
    if (data_source_name is not None):
      set('DataSourceForAutomaticMigration', getMBean('/JDBCSystemResources/'+data_source_name))
      cluster.setAutoMigrationTableName(table_name);

def create_work_managers(work_managers):
  print "create_work_managers " + str(work_managers)
  cmo = cd('/')
  domain_name = cmo.getName()

  for current in work_managers:
    #domain_name = current['domain_name']
    name = current['name']
    cluster = current['cluster']
    min_thread_constraint = current.get('min_thread_constraint', None)
    max_thread_constraint = current.get('max_thread_constraint', None)
    ignore_stuck_threads = current.get('ignore_stuck_threads', false)

    print '======= Creating a WorkManager ======='

    if (not_exists_work_manager(domain_name, name)):
      cd('edit:/SelfTuning/' + domain_name + '/WorkManagers/')
      create(name,'WorkManagers')
      cmo = cd('edit:/SelfTuning/' + domain_name + '/WorkManagers/' + name)
      cmo.addTarget(getMBean("/Clusters/"+ cluster))
      print ' WorkManager Created...'
    else:
      print 'workManager '+ name +' already exists'
    cmo = cd('/SelfTuning/'+domain_name+'/WorkManagers/' + name)
    cmo.setIgnoreStuckThreads(ignore_stuck_threads)
    print ' Ignore Stuck Threads set...'

    cmo=cd('edit:/SelfTuning/' + domain_name + '/WorkManagers/' + name)
    if (min_thread_constraint is not None):
      create_min_thread_constraint(cluster, domain_name, name + 'MinTC', min_thread_constraint)
      cmo.setMinThreadsConstraint(getMBean('/SelfTuning/' + domain_name + '/MinThreadsConstraints/' + name + 'MinTC'))
      print ' min thread constraint setted...'
    else:
      cmo.setMinThreadsConstraint(None)
      print ' min thread constraint setted to None'
    if (max_thread_constraint is not None):
      create_max_thread_constraint(cluster, domain_name, name + 'MaxTC', max_thread_constraint)
      cmo.setMaxThreadsConstraint(getMBean('/SelfTuning/' + domain_name + '/MaxThreadsConstraints/' + name + 'MaxTC'))
      print ' max thread constraint setted...'
    else:
      cmo.setMaxThreadsConstraint(None)
      print ' max thread constraint setted to None'

def create_min_thread_constraint(cluster, domain_name, name, min_thread_constraint):
    print "create_min_thread_constraint " + name

    print '======= Creating a MinThreadConstraint ======='

    if (not_exists_min_thread_contraint(domain_name, name)):
      wmMBean=getMBean("/SelfTuning/"+domain_name)
      minThreadConstInstance=wmMBean.createMinThreadsConstraint(name)
      minThreadConstInstance.addTarget(getMBean("/Clusters/"+ cluster))
      minThreadConstInstance.setCount(min_thread_constraint)
      print ' MinThreadsConstraint Created...'
    else:
      print ' MinThreadConstraint '+ name +' already exists'
      my_mbean=getMBean('/SelfTuning/' + domain_name + '/MinThreadsConstraints/' + name)
      if (my_mbean.getCount() != min_thread_constraint):
        my_mbean.setCount(min_thread_constraint)
        print ' MinThreadConstraint '+ name +' - count modified'

def create_max_thread_constraint(cluster, domain_name, name, max_thread_constraint):
    print "create_max_thread_constraint " + name

    print '======= Creating a MaxThreadConstraint ======='

    if (not_exists_max_thread_contraint(domain_name, name)):
      wmMBean=getMBean("/SelfTuning/"+domain_name)
      maxThreadConstInstance=wmMBean.createMaxThreadsConstraint(name)
      maxThreadConstInstance.addTarget(getMBean("/Clusters/"+ cluster))
      maxThreadConstInstance.setCount(max_thread_constraint)
      print ' MaxThreadsConstraint Created...'
    else:
      print ' MaxThreadConstraint '+ name +' already exists'
      my_mbean=getMBean('/SelfTuning/' + domain_name + '/MaxThreadsConstraints/' + name)
      if (my_mbean.getCount() != max_thread_constraint):
        my_mbean.setCount(max_thread_constraint)
        print ' MaxThreadConstraint '+ name +' - count modified'

def create_managed_executor_service_template(managed_executor_service_templates):
  print "create_managed_executor_service_template " + str(managed_executor_service_templates)

  for current in managed_executor_service_templates:

    name = current['name']
    cluster = current['cluster']
    dispatch_policy = current['dispatch_policy']

    print '======= Creating a Managed Executor ======='

    if (not_exists_managed_executor_service_template(name)):
      cmo = cd('/')
      cmo.createManagedExecutorServiceTemplate(name)
      cmo = cd('/ManagedExecutorServiceTemplates/'+name)
      cmo.setLongRunningPriority(5)
      cmo.setMaxConcurrentLongRunningRequests(10)
      cmo.setDispatchPolicy(dispatch_policy)
      set('Targets',jarray.array([ObjectName('com.bea:Name='+cluster+',Type=Cluster')], ObjectName))
      print ' ManagedExecutor Created...'
    else:
      print 'ManagedExecutor '+ name +' already exists'

def override_coherence_config_files(coherence_config_files):
  print "override_coherence_config_file " + str(coherence_config_files)

  for current in coherence_config_files:

    coherence_cluster_name = current['coherence_cluster_name']
    cluster_proxy_name = current['cluster_proxy_name']
    bo_coh_config_name = current['bo_coh_config_name']
    bo_coh_config_jndi_name = current['bo_coh_config_jndi_name']
    bo_coh_config_source_file = current['bo_coh_config_source_file']

    cd('/CoherenceClusterSystemResources/'+coherence_cluster_name+'/CoherenceCacheConfigs')
    
    if(not_exists_coherence_config(coherence_cluster_name, bo_coh_config_name)):
      print 'Create coherence config files'  
      create(bo_coh_config_name, 'CoherenceCacheConfig')
    else:
      print 'Coherence config ' + bo_coh_config_name + ' already exists'
    
    cmo = cd(bo_coh_config_name)
    set('JNDIName',bo_coh_config_jndi_name)
    print(bo_coh_config_source_file);
    cmo.setCacheConfigurationFile(bo_coh_config_source_file)
    cmo.importCacheConfigurationFile()
    cmo.addTarget(getMBean('/Clusters/'+cluster_proxy_name))

def create_data_sources(data_sources):
  print "create_data_source " + str(data_sources)

  for current in data_sources:

    data_source_name = current['data_source_name']
    data_source_jndi_name = current['data_source_jndi_name']
    data_source_url = current['data_source_url']
    data_source_driver_name = current['data_source_driver_name']
    data_source_test_query = current['data_source_test_query']
    data_source_usr = current['data_source_usr']
    data_source_pwd = current['data_source_pwd']
    data_source_target_cluster = current['data_source_target_cluster']
    global_transactions_protocol = current.get('global_transactions_protocol', 'none')
    #GRIDLINK
    data_source_type = current.get('data_source_type', 'GENERIC')
    grid_link_node_list = current.get('grid_link_node_list', None)
    
    if(not_exists_data_source(data_source_name)):
      print 'Creating datasource JDBC STORAGE ' + data_source_name
      cmo=cd('/')
      cmo.createJDBCSystemResource(data_source_name)
      print 'Created ' + data_source_name + ' Jdbc datasource'
    else:
      print 'Jdbc datasource ' + data_source_name + ' already exists'
     
    cmo=cd('/JDBCSystemResources/'+data_source_name+'/JDBCResource/'+data_source_name)
    cmo.setName(data_source_name)
    set('DatasourceType', data_source_type)
      
    if (grid_link_node_list is not None):
      cmo=cd('/JDBCSystemResources/'+data_source_name+'/JDBCResource/'+data_source_name+'/JDBCOracleParams/'+data_source_name)
      cmo.setActiveGridlink(true)
      cmo.setOnsNodeList(grid_link_node_list)
      cmo.setFanEnabled(true)
      
    cd('/JDBCSystemResources/'+data_source_name+'/JDBCResource/'+data_source_name+'/JDBCDataSourceParams/'+data_source_name)
    set('JNDINames',jarray.array([String(data_source_jndi_name)], String))
    cmo=cd('/JDBCSystemResources/'+data_source_name+'/JDBCResource/'+data_source_name+'/JDBCDriverParams/'+data_source_name)
    cmo.setUrl(data_source_url)
    cmo.setDriverName( data_source_driver_name )
    cmo.setPassword(data_source_pwd)
    cmo=cd('/JDBCSystemResources/'+data_source_name+'/JDBCResource/'+data_source_name+'/JDBCConnectionPoolParams/'+data_source_name)
    cmo.setTestTableName(data_source_test_query)
    cmo=cd('/JDBCSystemResources/'+data_source_name+'/JDBCResource/'+data_source_name+'/JDBCDriverParams/'+data_source_name+'/Properties/'+data_source_name )
    if(not_exists_data_source_user(data_source_name)):
      cmo.createProperty('user')
    cmo=cd('/JDBCSystemResources/'+data_source_name+'/JDBCResource/'+data_source_name+'/JDBCDriverParams/'+data_source_name+'/Properties/'+data_source_name+'/Properties/user')
    cmo.setValue(data_source_usr)
    cmo=cd('/JDBCSystemResources/'+data_source_name+'/JDBCResource/'+data_source_name+'/JDBCDataSourceParams/'+data_source_name)
    cmo.setGlobalTransactionsProtocol(global_transactions_protocol)
    cd('/SystemResources/'+data_source_name)

    targetList = array = []
    targetSplitted = data_source_target_cluster.split(",")
    for target in targetSplitted:
      targetList.append(ObjectName('com.bea:Name='+target+',Type=Cluster'))

    set('Targets',jarray.array(targetList, ObjectName))

def create_jdbc_persistent_storages(jdbc_persistent_storages):
  print "create_jdbc_persistent_storages " + str(jdbc_persistent_storages)

  for current in jdbc_persistent_storages:

    persistent_store_name = current['persistent_store_name']
    data_source_name = current['data_source_name']
    target_cluster = current['target_cluster']
    prefix_name = current.get('prefix_name', None)

    if(not_exists_jdbc_persistent_storage(persistent_store_name)):
      print 'Creating Jdbc persistent storage' + persistent_store_name
      cmo=cd('/')
      cmo.createJDBCStore(persistent_store_name)
    else:
      print 'Jdbc persistent storage ' + persistent_store_name + ' already exists'

    cmo=cd('/JDBCStores/'+persistent_store_name)
    cmo.setDataSource(getMBean('/JDBCSystemResources/'+data_source_name))
    cmo.setMigrationPolicy('On-Failure')
    if (prefix_name is not None):
      cmo.setPrefixName(prefix_name)
    set('Targets',jarray.array([ObjectName('com.bea:Name='+target_cluster+',Type=Cluster')], ObjectName))

#EXIST FUNCTIONS
def not_exists_cluster(name):
  my_mbean = getMBean('/Clusters/'+name)
  if (my_mbean is None):
    return true
  return false

def not_exists_managed(server):
  my_mbean = getMBean('/Servers/'+server)
  if (my_mbean is None):
    return true
  return false

def not_exists_coherence_cluster(cluster_name):
  my_mbean = getMBean('/CoherenceClusterSystemResources/' + cluster_name)
  if (my_mbean is None):
    return true
  return false

def not_exists_work_manager(domain_name, name):
  my_mbean = getMBean('/SelfTuning/' + domain_name + '/WorkManagers/' + name)
  if (my_mbean is None):
    return true
  return false

def not_exists_max_thread_contraint(domain_name, name):
  my_mbean = getMBean('/SelfTuning/' + domain_name + '/MaxThreadsConstraints/' + name)
  if (my_mbean is None):
    return true
  return false

def not_exists_min_thread_contraint(domain_name, name):
  my_mbean = getMBean('/SelfTuning/' + domain_name + '/MinThreadsConstraints/' + name)
  if (my_mbean is None):
    return true
  return false

def not_exists_managed_executor_service_template(name):
  my_mbean = getMBean('/ManagedExecutorServiceTemplates/'+name)
  if (my_mbean is None):
    return true
  return false

def not_exists_coherence_config(clusterName, configName):
  my_mbean = getMBean('/CoherenceClusterSystemResources/'+clusterName+'/CoherenceCacheConfigs/'+configName)
  if (my_mbean is None):
    return true
  return false

def not_exists_data_source(data_source_name):
  my_mbean = getMBean('/JDBCSystemResources/'+data_source_name)
  if (my_mbean is None):
    return true
  return false

def not_exists_data_source_user(data_source_name):
  my_mbean = getMBean('/JDBCSystemResources/'+data_source_name+'/JDBCResource/'+data_source_name+'/JDBCDriverParams/'+data_source_name+'/Properties/'+data_source_name+'/Properties/user')
  if (my_mbean is None):
    return true
  return false

def not_exists_jdbc_persistent_storage(persistent_store_name):
  my_mbean = getMBean('/JDBCStores/'+persistent_store_name)
  if (my_mbean is None):
    return true
  return false

def not_exists_coherence_wka(coherence_cluster_name, wka):
  my_mbean = getMBean('/CoherenceClusterSystemResources/' + coherence_cluster_name + '/CoherenceClusterResource/' + coherence_cluster_name + '/CoherenceClusterParams/' + coherence_cluster_name + '/CoherenceClusterWellKnownAddresses/' + coherence_cluster_name + '/CoherenceClusterWellKnownAddresses/' + wka);

  if (my_mbean is None):
    return true
  return false 
