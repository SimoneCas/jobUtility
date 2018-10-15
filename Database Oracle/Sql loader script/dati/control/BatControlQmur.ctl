OPTIONS(skip=1)
load data
 into table SAP_QMUR_CARIC
 fields terminated by "|"
 TRAILING NULLCOLS
 ( 
QMNUM,
URCOD,
URGRP,
URTXT
   )