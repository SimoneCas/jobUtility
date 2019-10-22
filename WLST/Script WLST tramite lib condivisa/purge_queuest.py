#!/usr/bin/python
import sys
sys.path.append("lib/")
from executor import *

class settings:

  wl = None
  wl = {
    "host": "admin_host:admin_port",
    "user": "admin-user",
    "password": "admin-password"
  }
 
  #if the "queues" field is not specified, it will purge all the queues found in specified JMS-Module.
  jms_modules = [
	{
	  "name": "JMS-Module-Name"#,
	  # will purge all queues found
	  #"queues": [ 
	  #	"queue_name"
	  #]
	}
 ]
  
purge_queues(settings())