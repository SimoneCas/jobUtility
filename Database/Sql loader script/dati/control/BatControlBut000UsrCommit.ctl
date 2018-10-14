OPTIONS(skip=1)
load data
 into table BUT000_USR_COMMITT
 fields terminated by ";"
 TRAILING NULLCOLS
 ( PARTNER,
PARTNER_GUID,
BPKIND
)