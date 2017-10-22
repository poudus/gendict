import csv

def output_decoration(fichier, word):
	fichier.write(word+'\n')
	fichier.write(word+'+\n')
	fichier.write(word+'!\n')
	fichier.write(word+'=\n')
	fichier.write(word+'$\n')
	fichier.write(word+'*\n')
	fichier.write(word+'%\n')
	fichier.write(word+'?\n')
	fichier.write(word+'&\n')
	fichier.write(word+'-\n')
	fichier.write(word+'_\n')
	return

def output_word1(fichier, word):
	for i in range(0,9):	
		output_decoration(fichier, word+str(i))
	return

def output_word2(fichier, word):
	for i in range(0,9):	
		for j in range(0,9):	
			output_decoration(fichier, word+str(i)+str(j))
	return

with open('./Prenoms.csv', 'rb') as fichier_input, open('./prenoms05.txt', 'w') as fichier_output:
	reader = csv.reader(fichier_input, delimiter=';')
	noline = 0
	for row in reader:
		if (noline > 0 and float(row[3]) > 0.5):
			output_word1(fichier_output, row[0])
			output_word1(fichier_output, row[0].title())
			output_word2(fichier_output, row[0])
			output_word2(fichier_output, row[0].title())
		noline+=1

