OPTIONS(skip=1)
load data
 into table CRMD_CUSTOMER_H
 fields terminated by ";"
 TRAILING NULLCOLS
 ( GUID,
ZZAUFNR_RIM,
ZZAUFNR
   )