OPTIONS(skip=1)
load data 
 into table	 CRMD_SCAPPTSEG_IND_27
 fields terminated by ";"
 TRAILING NULLCOLS
 ( APPL_GUID,
TST_FROM,
TST_TO
   )