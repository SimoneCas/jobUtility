# CLUSTER VARIABLES
wl = {
    "hostAndPort": "sasrmmpi01.match-point.it:7001",
    "user": "weblogic",
    "password": "MpiWladm2017"
}

clusters = [
    {
        "name": "Cluster_betting-offer-adapter",
        "messagingMode": "unicast"
    },
    {
        "name": "Cluster_betting-offer-stream",
        "messagingMode": "unicast"
    },
    {
        "name": "Cluster_betting-offer-providing",
        "messagingMode": "unicast"
    }
]

# SINGLETON SERVICES
singletonServiceClusters = ["Cluster_betting-offer-providing"]

# MANAGED VARIABLES
managedServers = [
    {
        "cluster": "Cluster_betting-offer-adapter",
        "server": "MS_BO-ADAPTER_1",
        "machine": "Machine_1",
        "port": 20001,
        "sslPort": 30001
    },
    {
        "cluster": "Cluster_betting-offer-adapter",
        "server": "MS_BO-ADAPTER_2",
        "machine": "Machine_2",
        "port": 20002,
        "sslPort": 30002
    },
    {
        "cluster": "Cluster_betting-offer-stream",
        "server": "MS_BO-STREAM_1",
        "machine": "Machine_1",
        "port": 20003,
        "sslPort": 30003
    },
    {
        "cluster": "Cluster_betting-offer-stream",
        "server": "MS_BO-STREAM_2",
        "machine": "Machine_2",
        "port": 20004,
        "sslPort": 30004
    },
    {
        "cluster": "Cluster_betting-offer-providing",
        "server": "MS_BO-PROV_1",
        "machine": "Machine_1",
        "port": 20005,
        "sslPort": 30005
    },
    {
        "cluster": "Cluster_betting-offer-providing",
        "server": "MS_BO-PROV_2",
        "machine": "Machine_2",
        "port": 20006,
        "sslPort": 30006
    }
]

workManagers = [
    {
        "domainName": 'int_mp_domain',
        "name": 'bettingOfferEventWorkManager',
        "cluster": 'Cluster_betting-offer-providing'
    },
    {
        "domainName": 'int_mp_domain',
        "name": 'bettingOfferMarketWorkManager',
        "cluster": 'Cluster_betting-offer-providing'
    }
]

managedExecutorServiceTemplates = [
    {
        "domainName": 'int_mp_domain',
        "name": 'bettingOfferMarketConsumerKafkaMes',
        "cluster": 'Cluster_betting-offer-providing',
        "dispatchPolicy": 'bettingOfferMarketWorkManager'
    },
    {
        "domainName": 'int_mp_domain',
        "name": 'bettingOfferEventConsumerKafkaMes',
        "cluster": 'Cluster_betting-offer-providing',
        "dispatchPolicy": 'bettingOfferEventWorkManager'
    }
]