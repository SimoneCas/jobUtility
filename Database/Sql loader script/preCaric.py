import sys
import os
import glob

print("Init Pre Caric")


#Estraggo info da file di properties
pathFileProp = "dati\\FIX_CONFIG_FILE.txt"
fileConfigOut = "dati\\CONFIGURATION_FILE.txt"

addedFile = [] #lista file aggiunti per controllo univocita caricamento

with open(pathFileProp) as f:
	with open(fileConfigOut,"w") as g:
		content = f.readlines()
		for line in content:
			if not line.startswith("#"):
				lineSpiltted = line.rstrip("\n").split(",")
				#print(lineSpiltted)

				#Estraggo nome file da directory dati\ con filtro
				#print("filtro:" + "dati\\"+lineSpiltted[1]+"*")
				fileCSVList = glob.glob("dati\\"+lineSpiltted[1]+"*")
				#print(fileCSVList)	

				#per ogni file trovati inserisco una entry nel file di configurazione 
				for entry in fileCSVList:						
					if entry in addedFile:
						print("###ERROR### file "+entry[5:]+" inserito più volte")	
						sys.exit()
					else:
						#print("write line:" + lineSpiltted[0]+","+entry[5:])
						g.write(lineSpiltted[0]+","+entry[5:]+"\n")
						addedFile.append(entry)



allFileCSVList = glob.glob("dati\\*.csv")
#print(allFileCSVList)

for aFile in allFileCSVList:
	if not aFile in addedFile:
		print("###ERROR###"+aFile + " non inserito in CONFIGURATION_FILE")
		
print("End Pre Caric")