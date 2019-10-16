#!/usr/bin/python
import sys
sys.path.append("***PATH_COMPLETO/lib/")
from executor import *

class settings:

  #WL SETTINGS
  wl = None
  
  #L'ordine di definizione verrà utilizzato per lo start e stop sequenziale dei clusters.
  clusters = [
         "CLUSTER_NAME_1",
         "CLUSTER_NAME_2",   
         "CLUSTER_NAME_3"
  ]
  
reboot_clusters(settings())
