OPTIONS(skip=1)
load data
 into table OPERANDI
 fields terminated by ";"
 TRAILING NULLCOLS
 ( IMPIANTO,
   OPERANDO,
   INIZIO,
   FINE,
   VALORE)