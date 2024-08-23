#! /usr/bin/env python
from Bio import SeqIO
import sys
def main(argv):

	for seq in SeqIO.parse(sys.argv[1], 'fasta'):
		print(">" + seq.id + '\n' + str(seq.seq).strip('*'))
if __name__ == "__main__":
  main(sys.argv)
