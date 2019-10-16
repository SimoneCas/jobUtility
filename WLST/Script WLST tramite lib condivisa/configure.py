#!/usr/bin/python
import sys
sys.path.append("*****PATH_COMPLETO_FINO_ALLA_LIB/lib/")
from executor import *

class settings:

  #WL SETTINGS
  wl = None
  
  # CLUSTERS
  clusters = [
    {
      "name": "***NOME_CLUSTER_1****",
      "messaging_mode": "unicast"
    },
    {
      "name": "***NOME_CLUSTER_2****",
      "messaging_mode": "unicast"
    }
  ]
  
  # MANAGED SERVERS
  managed_servers = [
    {
      "cluster": "***NOME_CLUSTER_1***",
      "server": "***NOME_SERVER_1***",
      "machine": "***NOME_MACHINE_1***",
      "port": 10001,
      "ssl_port": 10002
    }
  ]
  
  # JVM PARAMETER MANAGED SERVER
  server_jvm_parameters = [{
    "cluster_name": "***CLUSTER_NAME_1***",
    "arguments": " ***START_PARAMETERS*** "													   
  }]

  # migratable_clusters (4 SINGLETON/DS)
  migratable_clusters = [{
    "cluster_name": "***CLUSTER_NAME***",
    "data_source_name": "***DATA_SOURCE_NAME***" #can be null
  }]
  
  # COHERENCE CLUSTERS
  coherence_clusters = [{
    "coherence_cluster_name": "***COHERENCE_CLUSTER_NAME***",
    "coherence_cluster_port": 10008,
    "cluster_data_name": "***CLUSTER_WEBLOGIC_DATA_NAME***",
    "cluster_proxy_name": "***CLUSTER_WEBLOGIC_PROXY_NAME***",
    "wka": ["***IP1***","***IP2***"]
  }]
  
  # WORK MANAGERS
  work_managers = [
    {
      "domain_name": '***DOMAIN_NAME***',
      "name": '***WORK_MANAGER_NAME***',
      "cluster": '***CLUSTER_NAME***'
    }
  ]
  
  # MANAGED EXECUTOR SERVICE
  managed_executor_service_templates = [
    {
      "name": '***MEX_NAME***',
      "cluster": '***CLUSTER_NAME***',
      "dispatch_policy": '***WORK_MANAGER_NAME***'
    }
  ]
  
  # OVERRIDE COHERENCE CONFIG FILE
  coherence_config_files = [
    {
      "coherence_cluster_name": '***COHERENCE_CLUSTER_NAME***',
      "cluster_proxy_name": '***CLUSTER_WEBLOGIC_PROXY_NAME***',
      "bo_coh_config_name": '***CONFIG_NAME***',
      "bo_coh_config_jndi_name": '***CONFIG_JNDI_NAME***',
      "bo_coh_config_source_file": '***PATH_CONFIG_FILE_OVERRIDE***'
    }
  ]
  
  # DATA SOURCES JDBC
  data_sources = [
    {
      "data_source_target_cluster": '***CLUSTER_NAME_1_TARGET,CLUSTER_NAME_2_TARGET***',
      "data_source_name": '***DATA_SOURCE_NAME***,
      "data_source_jndi_name": '***JNDI_NAME***',
      "data_source_url": 'jdbc:oracle:thin:@HOST:PORT/SERVICE_NAME',
      "data_source_driver_name": 'oracle.jdbc.OracleDriver',
      "data_source_test_query": 'SQL SELECT 1 FROM DUAL',
      "data_source_usr": '***USER***',
      "data_source_pwd": '***PASSWORD***',
	  "global_transactions_protocol": 'none'
    }
  ]
  
  # JDBC PERSISTENT STORAGE
  jdbc_persistent_storages = [
  {
      "persistent_store_name": '***PERSISTENCE_STORAGE_NAME***',
      "data_source_name": '***DATA_SOURCE_NAME***',
      "target_cluster": '***CLUSTER_NAME_1_TARGET***'
    }
  ]

  # JMS RESOURCES
  jms_servers = [
    {
      "name" : "***JMS_SERVER_NAME***",
      "target_cluster" : "***CLUSTER_NAME_1_TARGET***"
	  #,"persistent_store_name": 'Betting-Offer-persistent-storage' #can be null
    }
  ]

  
  jms_modules = [
    {
      "name" : "***JMS_MODULE_NAME***",
      "target_cluster" : "***CLUSTER_NAME_1_TARGET***",
      "sub_deployments" : [
        {
          "name" : "***SUBDEPLOYMENT_NAME***",
          "target_jms_server" : "***CLUSTER_NAME_1_TARGET***"
        }
      ],
      "connection_factories" : [
        {
          "name" : "***CONNECTION_FACTORY_NAME***",
          "sub_deployment" : "***SUBDEPLOYMENT_NAME***",
          "XAConnectionFactoryEnabled" : True,
          "ServerAffinityEnabled" : False,
          "LoadBalancingEnabled" : True
        }
      ],
	  "foreign_servers" : [
        {
          "name" : "***FOREIGN_SERVER_NAME***",
          "initial_context_factory" : "oracle.jms.AQjmsInitialContextFactory",
          "data_source_jndi_name" : "***DATA_SOURCE_NAME***",
		  "connection_factories" : [
		    {
		      "name" : "***CONNECTION_FACTORY_NAME***",
			  "local_jndi_name" : "***LOCAL_JNDIN_NAME***",
              "remote_jndi_name" : "***REMOTE_JNDI_NAME***"
		    }
		  ],
		  "destinations" : [
		    {
		      "name" : "***DESTINATION_QUEUE***",
			  "local_jndi_name" : "***LOCAL_JNDIN_NAME***",
              "remote_jndi_name" : "***REMOTE_JNDI_NAME***"
		    }
		  ]
        }
      ],
    },
    {
      "name" : "***JMS_MODULE_NAME***",
      "target_cluster" : "***CLUSTER_NAME_1_TARGET***",
      "sub_deployments" : [
        {
          "name" : "***SUBDEPLOYMENT_NAME***",
          "target_jms_server" : "***TARGET_JMS_SERVER_NAME***"
        }
      ],
      "connection_factories" : [
        {
          "name" : "***CONNECTION_FACTORY_NAME***",
          "sub_deployment" : "***SUBDEPLOYMENT_NAME***",
          "XAConnectionFactoryEnabled" : True,
          "ServerAffinityEnabled" : False,
          "LoadBalancingEnabled" : True
        }
      ],
      "distributed_queues" : [
        {
          "name" : "***QUEUE_NAME***",
          "sub_deployment" : "***SUBDEPLOYMENT_NAME***",
          "redelivery_limit" : 1
        }
      ]
    }
  ]

execute_full_config(settings())
