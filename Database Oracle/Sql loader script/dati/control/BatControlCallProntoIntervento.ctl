OPTIONS(skip=1)
load data APPEND
 into table CALL_PRONTO_INTERVENTO
 fields terminated by ";"
 TRAILING NULLCOLS
 ( 
ID_CHIAMATA,
NUMERO_CHIAMANTE,
DATA_CHIAMATA,
DATA_CHIUS_CHIAMATA,
DATA_RISPOSTA,
ESITO_CHIAMATA,
ORA_CHIAMATA,
ORA_CHIUS_CHIAMATA,
ORA_RISP_CHIAMATA,
CHIAMATA,
CHIAMATA_ABBANDONATA,
CHIAMATA_RISPOSTA
   )