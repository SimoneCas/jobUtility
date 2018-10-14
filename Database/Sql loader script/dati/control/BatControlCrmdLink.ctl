OPTIONS(skip=1)
load data
 into table CRMD_LINK
 fields terminated by ";"
 TRAILING NULLCOLS
 ( GUID_HI,
GUID_SET
   )