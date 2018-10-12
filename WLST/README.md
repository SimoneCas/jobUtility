# WLST
Insieme di tutti gli script WLST sviluppati. 

Indice:
*  [Stop e start Clusters weblogic](#start-e-stop-clusters)





### Start e stop Clusters
Script che stoppa e ristarta tutti i server dei cluster configurati.

Variabili interne allo script:
1 wls_user = utente weblogic
2 wls_pwd = password weblogic
3 host_name = url admin server
4 wls_port = porta admin server
5 clusters = array ordinato con i cluster da gestire

L'ordine di stop dei cluster è dall'ultimo elemento dell'array al primo
L'ordine di start dei cluster è dal primo elemento dell'array all'ultimo

Run: MIDDLEWARE_HOME/oracle_common/common/bin/wlst Stop&StartClusters.py

