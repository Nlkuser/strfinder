# Imports :
import sys
import os
import colorama
import time
import random
from os import walk
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


citation = ("Sur internet, vous ne trouverez que ce que des gens ont bien voulu y laisser.","2","3")
def aff():
	print("""
	                         __..--.._		STRFIND - BETA
	  .....              .--~  .....  `.		by NLK
	.":    "`-..  .    .' ..-'"    :". `		with /OSINT
	` `._ ` _.'`"(     `-"'`._ ' _.' '		FR
	     ~~~      `.          ~~~
	              .'
	             /
 	           (
 	            ^---'
		""")
	print(random.choice(citation))


"""
a faire :
Leet mode
message aléatoire dans l'affichage
PARAMETRE SYSTEM
"""

def clear():
    if sys.platform == ('win32'):
        os.system("cls")
    else:
        os.system("clear")


data_preference = "1" # A MODIFIER DANS LA CONFIG

clear()
aff()
print("""
	Commande à effectuer ?
		- start
		- config
		- credit
	""")
cmd = input("> ")
if cmd == "config":
	print("""
		bla bla
		""")
else:
	clear()
	aff()

# - - - - - - Recherche de fichier - - - - - - 
print(Fore.GREEN+"\nRecherche de fichier . . .")
filelist = []
for (dirpath, dirnames, filenames) in walk(os.getcwd()):
    filelist.extend(filenames)
    txt = [nfile for nfile in filelist if ".txt" in nfile]
    sql = [nfile for nfile in filelist if ".sql" in nfile]
    break

print("    - Fichier pris en charge : ",len(txt + sql)," | ","TXT : ",len(txt)," | ","SQL : ",len(sql),)
if len(txt+sql) == 0:
	print("Attention, aucun fichier n'est repéré pour être automatiquement recherché.")
else:
	print("| ", end = "")
	for n in txt:
		print(n, end = " | ")

	print("\n")
# - - - - - - Recherche de fichier - - - - - - 

print(Fore.GREEN+"	[ 1 - Email:Pass ] <- ","\n	[ 2- IP ]\n	[ 3 - Pseudo ]\n	[ 4 - Brut ]")
mode = input("Mode : ")

if mode == "1" or mode == "" and data_preference == "1":
	print(Fore.GREEN+"Entrez les informations :")
	emain = input("Email : ")
	mdp = input("Mot de passe : ")
elif mode == "2" or mode == "" and data_preference == "2":
	print(Fore.GREEN+"Entrez l'information :")
	ip = input("IP : ")
elif mode == "3" or mode == "" and data_preference == "3":
	print(Fore.GREEN+"Entrez l'information :")
	pseudo = input("Pseudo : ")
elif mode == "4" or mode == "" and data_preference == "4":
	print(Fore.GREEN+"Entrez les informations :")
	emain = input("Email : ")
	mdp = input("Mot de passe : ")
	ip = input("IP : ")
	pseudo = input("Pseudo : ")
else:
	mode = data_preference



numt = 0
result = 0
clear()
aff()
# print(f"{emain} | {mdp}...") A AJOUTER PAR MODE
for filename in txt:

	fileresult = 0
	num = 0
	print("\n",Fore.GREEN+filename,":") # Show current file

	with open(filename, "r") as file:
		for line in file:
			num+=1
			numt+=1
			data = line.split(":")
			if emain in data[0] and emain != "":
				print("[ ligne n°",str(num),"]",Fore.RED+" - ",Fore.GREEN+data[0],Fore.RED+" - ",data[1], end="")
				result += 1
				fileresult += 1
			elif mdp in data[1] and mdp != "":
				print("[ ligne n°",str(num),"]",Fore.RED+" - ",data[0],Fore.RED+" - ",Fore.GREEN+data[1], end="")
				result += 1
				fileresult += 1

		if fileresult == 0:
			print("No data found in "+filename)

	print("")

print(numt," ligne ont été verifié pour ", end="")
if result == 0:
	print("aucun résultat. . . on aide comme on peux !")
else:
	print(result,"ligne correspondante a vos recherches.")
