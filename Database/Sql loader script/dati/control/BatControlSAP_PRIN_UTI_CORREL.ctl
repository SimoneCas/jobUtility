OPTIONS(skip=1)
load data APPEND
 into table SAP_PRIN_UTI_CORREL
 fields terminated by ";"
 TRAILING NULLCOLS
 ( AVVISO,
N_OGGETTO
   )