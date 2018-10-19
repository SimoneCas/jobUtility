# WLST
Insieme di tutti gli script WLST sviluppati. 

Indice:
*  [Stop e start Clusters weblogic](#start-e-stop-clusters)
*  [Configurazione dominio Weblogic](#configurazione-dominio-weblogic)
*  [Abilitazione/Disabilitazione dei Proxy Service di OSB](#abilita-disabilita-proxy-service)



### Start e stop Clusters
Script che stoppa e ristarta tutti i server dei cluster configurati.

Variabili interne allo script:
```
1. wls_user = utente weblogic
2. wls_pwd = password weblogic
3. host_name = url admin server
4. wls_port = porta admin server
5. clusters = array ordinato con i cluster da gestire
```

L'ordine di stop dei cluster è dall'ultimo elemento dell'array al primo
L'ordine di start dei cluster è dal primo elemento dell'array all'ultimo

Run: 
```
MIDDLEWARE_HOME/oracle_common/common/bin/wlst Stop&StartClusters.py
```
### Configurazione domino Weblogic
Script idempotente e parametrico che configura le seguenti risorse Weblogic:
* Managed Servers
* Cluster Weblogic
* Work Manager
* Singleton Cluster
* Cluster Coherence
* Parametri di avvio di managed servers
* Server JMS, Moduli JMS, Code JMS
* Datasource JDBC
* Override file di configurazione di Coherence

Tutte le parametrizzazioni sono configurate nei file settings_application_SYSINT.py, settingsEnvironment.py e settingsResources.py

Run: 
```
MIDDLEWARE_HOME/oracle_common/common/bin/wlst 4-configureCacheResources.py
```

### Abilita-Disabilita Proxy Service
Script che abilita/disabilità i proxy service di OSB indicati in input.

Variabili di input:
```
setProxyState [-d|-e] [-v] [-f list-of-proxy-services] admin-url wls-password [proxy-service]

-v verbose output
-d disable the proxy state
-e enable the proxy state
-f file with a list of proxy services
```
Esempio Run:
```
MIDDLEWARE_HOME/oracle_common/common/bin/wlst Stop&StartClusters.py setproxystate.py -e -f /scriptAbilitazioneProxy/listProxyDrop1.txt t3://wide-soa-a-01.wind.root.it:7001 weblogic1
```

Formato file con la lista di proxy services:
```
# RECEIVER REMEDY
Contact/receiver/remedy/nttm/wideesbContactNTTM_RTTRemedyTxManagerPrx
Contact/receiver/remedy/ottm/wideesbContactOTTM_RTTRemedyTxManagerPrx
```	
