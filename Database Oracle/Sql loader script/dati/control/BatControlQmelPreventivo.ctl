OPTIONS(skip=1)
load data
 into table SAP_QMEL_PREVENTIVO
 fields terminated by ";"
 TRAILING NULLCOLS
 ( AVVISO,
   NUM_OGGETTO,
   ZTIPPREV
   )