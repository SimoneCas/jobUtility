OPTIONS(skip=1)
load data
 into table CRMD_PARTNER_USR_COMMITT
 fields terminated by ";"
 TRAILING NULLCOLS
 ( GUID,
PARTNER_NO
)