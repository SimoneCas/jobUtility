OPTIONS(skip=1)
load data
 into table TABLE_DATE_PASS_STATO
 fields terminated by ";"
 TRAILING NULLCOLS
 ( SR,
   DATA_PASS_STATO
   )