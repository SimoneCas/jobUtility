OPTIONS(skip=1)
load data
 into table CRMD_ORDERADM_H
 fields terminated by ";"
 TRAILING NULLCOLS
 ( GUID,
CREATED_AT
   )