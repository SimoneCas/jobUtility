OPTIONS(skip=1)
load data
 into table SAP_EVBS
 fields terminated by ";"
 TRAILING NULLCOLS
 ( EDIFICIO,
   AVVISO
   )