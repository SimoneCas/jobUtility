-----CONFIGURAZIONE------------
DEFINE PATH_SCRIPT_SQL='D:\Acea-Monitoraggio-L655\ACEA_DB_L655\SVIL\SCRIPT_DB\indicatori655\SCRIPT_DB';

-------------------------------
--INSTALLAZIONE TABELLE--------
-------------------------------

prompt '2';
@ '&PATH_SCRIPT_SQL\1_INSTALLAZIONE\1_CFG_INDICATORI_DLG.sql';
prompt '2';
@ '&PATH_SCRIPT_SQL\1_INSTALLAZIONE\2_CFG_RANGE_CALCOLO.sql';
prompt '24_GET_SOGLIA_DL.sql';
@ '&PATH_SCRIPT_SQL\1_INSTALLAZIONE\24_GET_SOGLIA_DL.sql';

------------------
--INSERT DATI--------
-------------------------------
prompt 'FG_INDICATORI_DLG.sql';
@ '&PATH_SCRIPT_SQL\2_INSERT\1_INS_CFG_INDICATORI_DLG.sql';