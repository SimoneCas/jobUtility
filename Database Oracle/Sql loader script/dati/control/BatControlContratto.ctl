OPTIONS(skip=1)
load data
 into table CONTRATTI
 fields terminated by ";"
 TRAILING NULLCOLS
 ( CONTRATTO,
  SOCIETA,
  INIZIO,
  FINE,
  CID,
  CONTR_SIST_PREC,
  IMPIANTO,
  CONTO_CONTR,
  DATA_ATTIVAZIONE,
  DATA_CESSAZIONE,
  TIPO_CONTRATTO)