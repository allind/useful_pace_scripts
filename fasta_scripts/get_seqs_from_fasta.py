#! /usr/bin/env python
#usage: script.py [seq list] [fasta]
from Bio import SeqIO
import sys
def main(argv):

	seqs = [line.strip('\n').strip('\t') for line in open(sys.argv[1])]
	seq_fs = {}
	for seq in SeqIO.parse(sys.argv[2], 'fasta'):
		if seq.id in seqs:
			#seq_fs[seq.id] = str(seq.seq)
			print(">" + seq.id)
			print(str(seq.seq))
	#for f in seqs:
	#	print(">" + f)
	#	print(seq_fs[f])
if __name__ == "__main__":
  main(sys.argv)
