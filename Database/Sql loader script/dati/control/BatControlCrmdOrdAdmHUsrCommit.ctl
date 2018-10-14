OPTIONS(skip=1)
load data
 into table CRMD_ORDERADM_H_USR_COMMITT
 fields terminated by ";"
 TRAILING NULLCOLS
 ( GUID,
OBJECT_ID,
PROCESS_TYPE
)