OPTIONS(skip=1)
load data
 into table SAP_EVER
 fields terminated by ";"
 TRAILING NULLCOLS
 ( IMPIANTO,
DATA_CONTRATTO
)