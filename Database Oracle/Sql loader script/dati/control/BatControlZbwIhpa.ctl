OPTIONS(skip=1)
load data
 into table ZBW_IHPA
 fields terminated by ";"
 TRAILING NULLCOLS
 ( 
OBJNR,
PARNR
   )