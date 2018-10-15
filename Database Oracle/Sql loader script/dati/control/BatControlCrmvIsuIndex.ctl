OPTIONS(skip=1)
load data
 into table CRMV_ISU_INDEX_H_CARIC
 fields terminated by "|"
 TRAILING NULLCOLS
 ( 
OBJECT_ID,
CREATED_AT
   )