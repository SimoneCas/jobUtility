--liquibase formatted sql

--changeset simone:1
CREATE TABLE "MARKETS" (
	"EXTERNAL_SYSTEM_STATUS" VARCHAR2(255 BYTE), 
	"INSERT_DATE" TIMESTAMP, 
	"NAME" VARCHAR2(255 BYTE), 
	"MATCH_ID" VARCHAR2(255 BYTE), 
	"MARKET_ID" VARCHAR2(255 BYTE), 
	"TIMESTAMP" NUMBER(20,0), 
	"TRANSACTION_ID" VARCHAR2(255 BYTE), 
	"STATUS" VARCHAR2(255 BYTE), 
	"STATUS_OLD" VARCHAR2(255 BYTE), 
	"PROVIDER_ID" VARCHAR2(255 BYTE),
	CONSTRAINT "MARKETS_PK" PRIMARY KEY ("MATCH_ID","MARKET_ID")
);

--rollback DROP TABLE "MARKETS";

--changeset simone:2
CREATE TABLE "MARKETS_WAYS" (
	"INSERT_DATE" TIMESTAMP, 
	"ODDS" NUMBER(10,4), 
	"WAY_ID" VARCHAR2(255 BYTE), 
	"WIN" VARCHAR2(255 BYTE), 
	"MATCH_ID" VARCHAR2(255 BYTE), 
	"MARKET_ID" VARCHAR2(255 BYTE), 
	"TIMESTAMP" NUMBER(20,0), 
	"STATUS" VARCHAR2(255 BYTE), 
	"STATUS_OLD" VARCHAR2(255 BYTE)
);

--rollback DROP TABLE "MARKETS_WAYS";

-- changeset simone:3
ALTER TABLE "MARKETS"
ADD ("BRAND_ID" VARCHAR(20) NOT NULL);

-- rollback ALTER TABLE "MARKETS" DROP COLUMN "BRAND_ID"

-- changeset simone:4
ALTER TABLE "MARKETS"
ADD ("CHANNEL_ID" VARCHAR(20) NOT NULL);

-- rollback ALTER TABLE "MARKETS" DROP COLUMN "CHANNEL_ID"

-- changeset simone:5
ALTER TABLE "MARKETS_WAYS"
ADD ("BRAND_ID" VARCHAR(20));

-- rollback ALTER TABLE "MARKETS_WAYS" DROP COLUMN "BRAND_ID"

-- changeset simone:6
ALTER TABLE "MARKETS_WAYS"
ADD ("CHANNEL_ID" VARCHAR(20));

-- rollback ALTER TABLE "MARKETS_WAYS" DROP COLUMN "CHANNEL_ID"