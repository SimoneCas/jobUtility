import sys
import os
import glob


print(sys.argv)

ambiente = ""
if len(sys.argv) - 1 >= 1:
	ambiente = sys.argv[1] 

if ambiente or ambiente.isspace():
	print("ambiente:" + ambiente)
else:
	print("AMBIENTE_NON_DEFINITO")
	print("I POSSIBILI PARAMETRI PER DEFINIRE L'AMBIENTE DI CARICAMENTO DA UTILIZZARE SONO:")
	print ("DEV - SVILUPPO LOCALE")
	print ("PROD - PRODUZIONE ACEA")
	sys.exit()

print("len(sys.argv):"+str(len(sys.argv)))
if len(sys.argv) - 1 >= 2:
	loadLimit = sys.argv[2]	
else:
	loadLimit = -1

print("loadLimit:" + str(loadLimit))

if ambiente == "HELP" :
	print("I POSSIBILI PARAMETRI PER DEFINIRE L'AMBIENTE DI CARICAMENTO DA UTILIZZARE SONO: ")
	print("DEV - SVILUPPO LOCALE")
	print("PROD - PRODUZIONE ACEA")
	print("SE SI VUOLE LIMITARE IL NUMERO DI RIGHE DA CARICARE PER TABELLA, LANCIARE IL COMANDO CON UN SECONDO PARAMETRO NUMERICO CHE INDICA IL NUMERO DI RIGHE MASSIMO DA CARICARE - DEFAULT: ALL")
	sys.exit()

if ambiente == "DEV" : 
	print("Caricamento dati in DEV")
	dbUrl = "USR655/USR655@//localhost:1521/xe"
elif ambiente == "PROD":	
	print("Caricamento dati in PROD")
	sys.exit()
else:
	print("AMBIENTE NON CONFIGURATO")
	sys.exit()

pathConfigurationFile= "dati\CONFIGURATION_FILE.txt"

with open(pathConfigurationFile) as f:
	content = f.readlines()
	for line in content:
		if not line.startswith("#"):
			lineSpiltted = line.rstrip("\n").split(",")
			print(lineSpiltted)
			cmd = "sqlldr " + dbUrl + " " + "control=dati\\control\\" + lineSpiltted[0] + " " + \
			"data=dati\\"+ lineSpiltted[1] + " " + "load=" + str(loadLimit) + " " + "log=dati\\log\\" + lineSpiltted[0][:-4]+".log" + \
			" " + "bad=dati\\bad\\" + lineSpiltted[0][:-4]+".bad"
			#print(cmd)
			os.system(cmd)
		else:
			print(line.rstrip("\n") + " skipped")

#controllo file di log
allFilelogList = glob.glob("dati\\log\\*.log")
for log in allFilelogList:
	if "SQL*Loader-" in open(log).read():
		print("###ERRORE### in log "+ log)
		

