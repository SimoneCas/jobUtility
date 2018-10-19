#!/bin/sh

CLUSTER_APP_NAME="Cluster_betting-offer-providing"

CLUSTER_DATA_NAME="Cluster_betting-offer-data"

CLUSTER_PROXY_NAME='Cluster_betting-offer-proxy'

COHERENCE_CLUSTER_NAME='Coherence_Betting-offer'

COHERENCE_CLUSTER_PORT=7575

BO_COH_CONFIG_JNDI_NAME='bodg'

BO_COH_CONFIG_NAME='Bodg_proxy_config'

BO_COH_CONFIG_SOURCE_FILE='/u01/app/data/config/bettingOffer/coherence-cache-config-proxy-nodb.xml'

ARGUMENTS_APP_SERVERS='-Dtangosol.coherence.cacheconfig=/u01/app/data/config/bettingOffer/coherence-cache-config-client.xml -Dtangosol.pof.config=/u01/app/data/config/bettingOffer/pof-config.xml -Dcoherence.tcmp.enabled=false'

HOST_NAME='sasrmmpi01.match-point.it'

WLS_PORT='7001'