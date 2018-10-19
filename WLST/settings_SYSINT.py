# SETTINGS
wl = {
    "hostAndPort": "sasrmmpi01.match-point.it:7001",
    "user": "weblogic",
    "password": "MpiWladm2017"
}

#L'ordine di definizione verrà utilizzato per lo start e stop sequenziale dei clusters.
clusters = [
       "Cluster_betting-offer-data",
       "Cluster_betting-offer-proxy",   
       "Cluster_betting-offer-providing",
       "Cluster_betting-offer-stream",
       "Cluster_betting-offer-adapter"
]

#L'ordine di definizione verrà utilizzato per il deploy sequenziale delle applicazioni.
apps = [
    {
		"appName": "betting-offer-data-grid-gar",
        "path": "/deployint/betting-offer/setup_APP/betting-offer-data-grid-gar/0.0.4-SNAPSHOT/betting-offer-data-grid-gar-0.0.4-SNAPSHOT.gar",
        "cluster": "Cluster_betting-offer-data,Cluster_betting-offer-proxy"
    },
    {
        "appName": "betting-offer-providing-ear",
        "path": "/deployint/betting-offer/setup_APP/betting-offer-providing/0.0.2-SNAPSHOT/betting-offer-providing-ear-0.0.2-SNAPSHOT.ear",
		"cluster": "Cluster_betting-offer-providing"
    },
    {
        "appName": "betting-offer-stream",
        "path": "/deployint/betting-offer/setup_APP/betting-offer-stream/0.0.4-SNAPSHOT/betting-offer-stream-0.0.4-SNAPSHOT.ear",
		"cluster": "Cluster_betting-offer-stream"
    },
    {
        "appName": "betting-offer-ivt-adapter",
        "path": "/deployint/betting-offer/setup_APP/betting-offer-ivt-adapter/0.0.3-SNAPSHOT/betting-offer-ivt-adapter-0.0.3-SNAPSHOT.ear",
		"cluster": "Cluster_betting-offer-adapter"
    }
]