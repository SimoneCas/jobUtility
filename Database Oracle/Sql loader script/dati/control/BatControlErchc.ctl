OPTIONS(skip=1)
load data
 into table crm_erchc
 fields terminated by ";"
 TRAILING NULLCOLS
 ( BELNR,LFDNR,OPBEL,CPUDT,BUDAT,INTOPBEL,INTCPUDT,INTBUDAT,TOBRELEASD,SIMULATED,INVOICED,SPCANC )