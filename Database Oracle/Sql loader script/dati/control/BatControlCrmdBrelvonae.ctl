OPTIONS(skip=1)
load data
 into table CRMD_BRELVONAE
 fields terminated by ";"
 TRAILING NULLCOLS
 ( OBJGUID_A_SEL,
OBJGUID_B_SEL
   )