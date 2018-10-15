OPTIONS(skip=1)
load data
 into table CRMD_SRV_OSSET_CARIC
 fields terminated by "|"
 TRAILING NULLCOLS
 ( GUID_SET,
GUID,
PROFILE_TYPE
)