OPTIONS(skip=1)
load data APPEND
 into table SAP_IW49N
 fields terminated by ";"
 TRAILING NULLCOLS
 ( DIVPIANIFMANUT,
TIPO_DI_ORDINE,
ORDINE,
TIPO_DI_ATTIVITA_PM,
CENTRO_LAV_RESPONS,
OPERAZIONE,
STATO_UTENTE_OPERAZIONE,
CHIAVE_DI_CONTROLLO,
CH_TESTO_STANDARD,
OPERAZIONE_TESTO_BREVE,
UNITA_LAVORO,
LAVORO,
DATA_FINE_CARDINE,
DATA_INIZIO_CARDINE,
CID,
CONFERMA,
DATA_FINE_EFF,
IMPIANTO,
DATA_INI_PRESTO,
DATA_INI_TARDI,
DATA_INI_EFF,
ORA_INIZIO_CARDINE,
STATO_UTENTE,
ORA_FINE_EFF,
AVVISO,
IDONEITA
   )