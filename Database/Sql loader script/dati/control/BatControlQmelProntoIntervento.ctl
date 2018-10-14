OPTIONS(skip=1)
load data
 into table SAP_QMEL_PRONTO_INT_CARIC
 fields terminated by "|"
 TRAILING NULLCOLS
 ( AVVISO,
ORDINE,
ORDINE_ORIG
   )