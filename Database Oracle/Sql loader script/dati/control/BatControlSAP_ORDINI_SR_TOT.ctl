OPTIONS(skip=1)
load data APPEND
 into table SAP_ORDINI_SR_TOT
 fields terminated by ";"
 TRAILING NULLCOLS
 ( ORDINE,
TIPO_ODL,
DIV,
SR,
ZZ_DISCNO
   )