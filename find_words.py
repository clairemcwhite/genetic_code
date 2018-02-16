from __future__ import print_function
from Bio import SeqIO
import argparse


def load_fasta(filename):

    prot_dict = SeqIO.to_dict(SeqIO.parse(filename, "fasta"))
    return prot_dict

def load_words(dictionaryfile):
     word_dict = {}

     with open(dictionaryfile, "r") as dictionary:
         for raw_word in dictionary.readlines():
             word= raw_word.replace("\n", "")
             word_dict[word] = 0  
     return word_dict 


def scan_proteins(prot_dict, word_dict, outfile):
    
    with open(outfile, "w") as final:
        for wordkey in word_dict.keys():
            for protvalue in prot_dict.values():
                if wordkey in protvalue:
                     word_dict[wordkey] += 1
            outphrase = wordkey + " " + str(word_dict[wordkey]) + "\n"
            final.write(outphrase)
         
  
parser = argparse.ArgumentParser(description='genetic code')

parser.add_argument('fastafile', action="store", type=str, help="table with annotations")
parser.add_argument('wordfile', action="store", type=str, help="Table to be annotated")
parser.add_argument('outfile', action="store", type=str, help="Table to be annotated")

args = parser.parse_args()

prot_dict = load_fasta(args.fastafile)
word_dict = load_words(args.wordfile)
scan_proteins(prot_dict, word_dict, args.outfile)










