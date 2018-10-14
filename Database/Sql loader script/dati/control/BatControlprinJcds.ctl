OPTIONS(skip=1)
load data APPEND
 into table SAP_PRIN_UTI_PRIN
 fields terminated by ";"
 TRAILING NULLCOLS
 ( N_OGGETTO,
   STATO,
   UTENTE,
   DATA,
   ORA,
   I_U)