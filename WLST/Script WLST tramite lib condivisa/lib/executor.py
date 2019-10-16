#!/usr/bin/python
from domain_lib import *
from jms_lib import *
# VERSION: 0.0.1

def execute_full_config(settings):
 
  try:
    init_connection(settings)
    begin_edit()

    #the order is important
    create_clusters(getattr(settings,"clusters",[]))
    create_managed_servers(getattr(settings,"managed_servers",[]))
    create_coherence_clusters(getattr(settings,"coherence_clusters",[]))
    config_jvm_start_parameters(getattr(settings,"server_jvm_parameters",[]))
    create_work_managers(getattr(settings,"work_managers",[]))
    create_managed_executor_service_template(getattr(settings,"managed_executor_service_templates",[]))
    override_coherence_config_files(getattr(settings,"coherence_config_files",[]))
    create_data_sources(getattr(settings,"data_sources",[]))
    create_jdbc_persistent_storages(getattr(settings,"jdbc_persistent_storages",[]))
    configure_migratable_clusters(getattr(settings,"migratable_clusters",[]))
    create_jms_servers(getattr(settings,"jms_servers",[]))
    create_jms_modules(getattr(settings,"jms_modules",[]))
  
    end_edit()
    disconnect()

  except Exception, e:
    dumpStack()
    undo('true','y')
  
def deploy_apps(settings):
 
  try:
    init_connection(settings)
    begin_edit()

    for app in settings.apps:
      app_name = app['app_name']
      path = app['path']
      cluster_target = app['cluster']
      deployment_plan = None
      if (hasattr(app, 'deployment_plan')):
         deployment_plan = app['deployment_plan']
      
      myMBean = getMBean('edit:/AppDeployments/'+ app_name)
      if (myMBean is not None):
        if (deployment_plan is not None):
           wslt_progress = redeploy(app_name, appPath=path, planPath = deployment_plan)
        wslt_progress = redeploy(app_name, appPath=path)
      else:
        if (deployment_plan is not None):
           wslt_progress = deploy(app_name, path, cluster_target, planPath = deployment_plan)
        wslt_progress = deploy(app_name, path, cluster_target)
      
      print '### DEPLOY STATUS ### '+app_name+ '###'
      wslt_progress.printStatus()
    
    end_edit()
    disconnect()
    
  except Exception, e:
    dumpStack()
    undo('true','y')

def shutdown_clusters(settings):
  try:
    init_connection(settings)

    stop_clusters(settings.clusters)

    disconnect()

  except Exception, e:
    dumpStack()

def startup_clusters(settings):
  try:
    init_connection(settings)

    start_clusters(settings.clusters)

    disconnect()

  except Exception, e:
    dumpStack()

def reboot_clusters(settings):

  try:
    init_connection(settings)

    stop_clusters(settings.clusters)
    start_clusters(settings.clusters)

    disconnect()

  except Exception, e:
    dumpStack()

def purge_queues(settings):

  try:
    init_connection(settings)

    perform_purge_queues(settings.jms_modules, settings.wl)

    disconnect()

  except Exception, e:
    dumpStack()
  
def init_connection(settings):

  if settings.wl is None:
    host=raw_input('Insert Weblogic host and port: ')
    user=raw_input('Insert Weblogic user: ')
    password=raw_input('Insert Weblogic Password: ')
    settings.wl={
      "host": host,
      "user": user,
      "password": password
    }
  
  connect(settings.wl['user'], settings.wl['password'], settings.wl['host'])

def begin_edit():
  edit()
  startEdit()
  
def end_edit():
  save()
  activate()
  
def stop_clusters(clusters):

  nClusters = len(clusters)
  for x in range(nClusters-1, -1, -1):
    cluster = clusters[x]
    shutdown(name=cluster, entityType='Cluster', block='true')
    state(cluster,'Cluster')
  
def start_clusters(clusters):

  for cluster in clusters:
    start(name=cluster, type='Cluster', block='true')
    state(cluster,'Cluster')
  

  
