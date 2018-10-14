OPTIONS(skip=1)
load data
 into table SAP_EANL_REGISTR_CARIC
 fields terminated by "|"
 TRAILING NULLCOLS
 (IMPIANTO,
TIPO_IMPIANTO
   )