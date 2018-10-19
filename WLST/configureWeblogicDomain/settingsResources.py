#!/bin/sh

#JMS
JMS_SERVER_NAME="JMSServer-Bodg"


JMS_MODULE_NAME="JMSModule-Bodg"


SUB_DEPL_NAME="Bodg-SD"


CONN_FACTORY_NAME="connectionFactory-bodg"


#EVENTS
EVENTS_QUEUE="events_queue"

EVENTS_PAGES_QUEUE="events_pages_queue"

#MARKETS
MARKETS_QUEUE="markets_queue"

MARKETS_PAGES_QUEUE="markets_pages_queue"

EVENTS_MARKETS_PAGES_QUEUE="events_pages_for_markets_queue"

REDELIVERY_LIMIT="1"

#MARKET_ATTRIBUTE_QUEUE
MARKET_ATTRIBUTE_QUEUE="market_attribute_queue"

#PERSISTENT JDBC DATASOURCE
JDBC_STORAGE_DATA_SOURCE_NAME="Betting-Offer-DB"

JDBC_STORAGE_DATA_SOURCE_JNDI_NAME="jdbc/betting-offer-db"

JDBC_STORAGE_DATA_SOURCE_URL="jdbc:oracle:thin:@sdbexarmmptest-scan.sisal.it:1521/spint.mp.it"

JDBC_STORAGE_DATA_SOURCE_DRIVER_NAME="oracle.jdbc.OracleDriver"

JDBC_STORAGE_DATA_SOURCE_PWD="mpdba_test"

DATA_SOURCE_TEST_QUERY="SQL SELECT 1 FROM DUAL"

JDBC_STORAGE_DATA_SOURCE_USER="mp_dba"


