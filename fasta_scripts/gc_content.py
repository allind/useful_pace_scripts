#! /usr/bin/env python
from Bio import SeqIO
from Bio import SeqUtils
import sys
def main(argv):

	allseq = ""
	for seq in SeqIO.parse(sys.argv[1], 'fasta'):
		allseq += str(seq.seq)
			
		curra = str(seq.seq).count('A') + str(seq.seq).count('a')
		currc = str(seq.seq).count('C') + str(seq.seq).count('c')
		currg = str(seq.seq).count('G') + str(seq.seq).count('g')
		currt = str(seq.seq).count('T') + str(seq.seq).count('t')

		gc = float(currc + currg) / float(curra + currc + currg + currt)
		print(seq.id + '\t' + str(gc))

	a = allseq.count('A')
	c = allseq.count('C')
	g = allseq.count('G')
	t = allseq.count('T')
	mygc = float(c+g) / float(a+c+g+t)
	print(sys.argv[1] + '\t' + str(mygc))

if __name__ == "__main__":
  main(sys.argv)

