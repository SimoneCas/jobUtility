OPTIONS(skip=1)
load data
 into table CRMD_SRV_SUBJECT
 fields terminated by ";"
 TRAILING NULLCOLS
 ( GUID_REF,
KATALOGART,
CODE,
CODEGRUPPE
)