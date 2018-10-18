
#
# Make sure you have set the domain environment settings:
#
# . $WLS_DOMAIN/bin/setDomainEnv.sh
# 
# Usage:
# 
# /opt/weblogic/Middleware/Oracle_OSB/common/bin/wlst.sh setproxystate.py -e -f listofproxies.txt t3://l2-mslfonapp02:7001 webl0gic
# 
import getopt 
import sys
import os

from com.bea.wli.sb.management.configuration import SessionManagementMBean
from com.bea.wli.sb.management.configuration import ALSBConfigurationMBean
from com.bea.wli.config import Ref
from com.bea.wli.monitoring import StatisticType
from com.bea.wli.sb.util import Refs
from com.bea.wli.sb.management.configuration import CommonServiceConfigurationMBean

wl_user="system"
verbose=False

#########################################################################################

def ConnectToWLS(u, p, h):
  msg("Connect to " + h + " as user " + u)
  connect(u,p, h)
  domainRuntime()

def DisconnectFromWLS():
  msg("Disconnect")
  disconnect()

def CreateOSBSession():
  sessionName  = "SetProxyStateSession_" + str(System.currentTimeMillis())
  sessionMBean = findService(SessionManagementMBean.NAME, SessionManagementMBean.TYPE)
  sessionMBean.createSession(sessionName)
  msg("OSB Session Created: " + sessionName)
  return sessionMBean, sessionName

def ActivateSession(b, n, s, a):
  msg("Activate OSB Session: " + n)
  b.activateSession(n, a + " " + s)

def FindService(f, s, session, n):
  msg("Find proxy service: " + f + "/" + s)
  pxyConf = "ProxyServiceConfiguration." + n
  mbean = findService(pxyConf, 'com.bea.wli.sb.management.configuration.ProxyServiceConfigurationMBean')
  folderRef = Refs.makeParentRef(f + '/')
  serviceRef = Refs.makeProxyRef(folderRef, s)
  return serviceRef, mbean

def setStateService(b, s, a):
  if a == 'disable':
    msg("Disable Service")
    b.disableService(s)
  else:
    msg("Enable Service")
    b.enableService(s)

#########################################################################################

def usage():
  print "Usage: Enable/Disable Proxy services"
  print "setProxyState [-d|-e] [-v] [-f list-of-proxy-services] admin-url wls-password [proxy-service]"
  print "-v verbose output"
  print "-d disable the proxy state"
  print "-e enable the proxy state"
  print "-f file with a list of proxy services"

def main():

############################################################
## Parse Arguments
##
  proxy_file=""
  noofargs = 3
  try:
    opts, args = getopt.getopt(sys.argv[1:], "vdehf:", ["help"])

    for o, a in opts:
      if o == '-h':
        usage()
        exit()
      elif o == '-v':
        global verbose
        verbose = True
      elif o == '-d':
        state = "disable"
      elif o == '-e':
        state = "enable"
      elif o == '-f':
        proxy_file = a
        noofargs = noofargs - 1 
      else:
        print "Unknown argument."
        print ""
        usage()
        exit()

    if len(args) != noofargs:
      print "Invalid number of arguments."
      print ""
      usage()
      exit()

    admin_server = args[0]       
    wl_password = args[1]       

    if len(proxy_file) > 0:
      setStateListOfProxyService(proxy_file, state, wl_password, admin_server)
    else:
      proxy_service = args[2]
      setStateOfProxyService(proxy_service, state, wl_password, admin_server)

  except getopt.GetoptError, err:
    # print help information and exit: 
    print str(err)
    print ""
    usage()

############################################################

def msg(m):
  if verbose:
    print m

def setStateListOfProxyService(pfile, stateOnOff, wl_password, admin_server):
  try:
    ConnectToWLS(wl_user, wl_password, admin_server)

    file = open(pfile, "r")
    osbSession, sessionName = CreateOSBSession()

    appliedServices = ""
    for line in file.readlines():
      line = line.lstrip().rstrip()
      msg("Read line: " + line)
      if line.find("#") < 0 and len(line) > 0:
        relativePath = os.path.dirname(line)
        pServiceName = os.path.basename(line)
        appliedServices = appliedServices + " " + pServiceName
        service, sessionBean = FindService(relativePath, pServiceName, osbSession, sessionName)
        setStateService(sessionBean, service, stateOnOff)
  
    file.close()
    ActivateSession(osbSession, sessionName, appliedServices, stateOnOff)

    DisconnectFromWLS()

  except:
    print "Unexpected error: ", sys.exc_info()[0]
    dumpStack()
    raise

def setStateOfProxyService(pservice, stateOnOff, wl_password, admin_server):
  try:
    ConnectToWLS(wl_user, wl_password, admin_server)

    osbSession, sessionName = CreateOSBSession()

    relativePath = os.path.dirname(pservice)
    pServiceName = os.path.basename(pservice)

    service, sessionBean = FindService(relativePath, pServiceName, osbSession, sessionName)
    setStateService(sessionBean, service, stateOnOff)
    ActivateSession(osbSession, sessionName, pServiceName, stateOnOff)

    DisconnectFromWLS()

  except:
    print "Unexpected error: ", sys.exc_info()[0]
    dumpStack()
    raise

############################################################

main()
exit()