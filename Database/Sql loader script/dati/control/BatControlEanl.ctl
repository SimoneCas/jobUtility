OPTIONS(skip=1)
load data
 into table SAP_EANL
 fields terminated by ";"
 TRAILING NULLCOLS
 ( IMPIANTO,
   EDIFICIO
   )