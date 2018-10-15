OPTIONS(skip=1)
load data
 into table CRMD_SCAPPTSEG
 fields terminated by ";"
 TRAILING NULLCOLS
 ( APPL_GUID,
TST_FROM
   )