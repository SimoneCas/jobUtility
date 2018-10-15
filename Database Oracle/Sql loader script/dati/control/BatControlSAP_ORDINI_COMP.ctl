OPTIONS(skip=1)
load data APPEND
 into table SAP_ORDINI_COMP
 fields terminated by ";"
 TRAILING NULLCOLS
 ( ORDINE,
OPERAZIONE,
DT_COMP,
ORA_COMP
   )