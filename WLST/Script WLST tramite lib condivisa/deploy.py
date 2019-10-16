#!/usr/bin/python
import sys
sys.path.append("***PATH_COMPLETO/lib/")
from executor import *

class settings:

  #WL SETTINGS
  wl = None
  
  #L'ordine di definizione verrà utilizzato per il deploy sequenziale delle applicazioni.
  apps = [
      {
        "app_name": "***APP_NAME_1***",
        "path": "***PATH_COMPLETO/modulo.ear***",
        "cluster": "***CLUSTER_NAME_TARGET***"
      },
      {
        "app_name": "***APP_NAME_2***",
        "path": "***PATH_COMPLETO/modulo2.ear***",
        "cluster": "***CLUSTER_NAME_TARGET***"
      }
  ]

deploy_apps(settings())