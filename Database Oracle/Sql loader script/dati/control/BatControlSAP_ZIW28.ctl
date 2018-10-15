OPTIONS(skip=1)
load data 
 into table SAP_ZIW28
 fields terminated by ";"
 TRAILING NULLCOLS
 ( AVVISO,
ID_CHIAMATA
   )