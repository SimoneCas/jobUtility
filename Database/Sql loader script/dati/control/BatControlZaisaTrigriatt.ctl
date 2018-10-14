OPTIONS(skip=1)
load data
 into table ZAISA_TRIGRIATT
 fields terminated by ";"
 TRAILING NULLCOLS
 ( DISCNO,
ZORIGINE,
MESSAGE,
DATA_RIC,
ORA_RIC
)