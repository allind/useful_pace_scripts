#! /usr/bin/env python
#usage: script.py [fasta] [to remove]
from Bio import SeqIO
import sys
def main(argv):

	remove = [line.strip('\n').strip('>') for line in open(sys.argv[2])]
	for seq in SeqIO.parse(sys.argv[1], 'fasta'):
		if seq.id not in remove:
			print(">" + seq.id + '\n' + str(seq.seq))
if __name__ == "__main__":
  main(sys.argv)
