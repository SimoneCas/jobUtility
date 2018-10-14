OPTIONS(skip=1)
load data
 into table CRMD_LINK_USR_COMMITT
 fields terminated by ";"
 TRAILING NULLCOLS
 ( GUID_HI,
GUID_SET,
OBJTYPE_HI,
OBJTYPE_SET
)