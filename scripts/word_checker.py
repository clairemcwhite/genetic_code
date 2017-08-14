#Script to find words in proteomes
#python word_finder.py wordlistFile proteomeFile outfileName

import sys
from Bio import SeqIO

wordlistFile = sys.argv[1]
proteomeFile = sys.argv[2]
outfileName = sys.argv[3]


with open(wordlistFile, "r") as words:
   with open(outfileName, "a") as outfile:
	wordlist = str(words.read()).split("\n")
#	print wordlist[0]
#	print wordlist[1]
        wordlist = wordlist [:-1]
#	print wordlist
	
	for record in SeqIO.parse(proteomeFile, "fasta"):
		for word1 in wordlist[1:]:
                        testword = str(word1).replace("\r", "")
		        if testword in str(record.seq):
				#print testword
				#print record.id
				outfile.write(str(testword)+" " + str(record.id) + "\n")


















#
