# WLST
Insieme di tutti gli script WLST sviluppati. 

Indice:
Libreria unificata che permette sia operazioni di configurazione che di operatività. Customizzabile andando a modificare semplici file di configurazione:
*  [Script WLST tramite lib condivisa](#Script-WLST-tramite-lib-condivisa)

Il resto degli script invece fornisce singole funzionalità:
*  [Stop e start Clusters weblogic](#start-e-stop-clusters)
*  [Configurazione dominio Weblogic](#configurazione-dominio-weblogic)
*  [Deploy applicazioni](#deploy-applicazioni)
*  [Abilitazione/Disabilitazione dei Proxy Service di OSB](#abilita-disabilita-proxy-service)


### Script WLST tramite lib condivisa
Libreria unificata che permette sia operazioni di configurazione che di operatività. Customizzabile andando a modificare semplici file di configurazione.
Posizionare su filesystemm nella stessa directory sia i file di configurazione .py che la cartella lib che contiene le tre liberrie:
```
main_dir
    |
    |__ configure.py
    |__ deploy.py
    |__ reboot.py
    |__ startup.py
    |__ shutdown.py
    |______ lib
             |
             |__ domain_lib.py
             |__ executor.py
             |__ jms_lib.py
```

Esempio lancio dello script:

```
MIDDLEWARE_HOME/oracle_common/common/bin/wlst configure.py
```

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

### Deploy applicazioni
Script idempotente che installa gli eseguibili passati in input.

Variabili da configurare nel file setting_SYSINT:
* appName: nome applicazione
* path: percorso fisico di dove risiede il file da installare
* cluster: cluster sul quale installare il pacchetto

Run: 
```
MIDDLEWARE_HOME/oracle_common/common/bin/wlst deployApps.py settings_SYSINT
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
