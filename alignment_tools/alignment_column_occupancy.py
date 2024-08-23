#! /usr/bin/env python
from Bio import SeqIO
import statistics as st
import sys
def main(argv):

	seqs = {seq.id: str(seq.seq) for seq in SeqIO.parse(sys.argv[1], 'fasta')}
	seqlen = len(list(seqs.values())[0])

	#determine site occupancy
	site_occupancy = []
	for i in range(0, seqlen):
		neg = 0
		pos = 0
		for seq in seqs:
			if seqs[seq][i] == "-":
				neg += 1
			else:
				pos += 1
		percent_occ = pos / (neg + pos)
		site_occupancy.append(percent_occ)
	
	occ_metrics = {}

	for seq in seqs:
		currseq = seqs[seq]
		occs = []
		for i in range(0, seqlen):
			if currseq[i] != '-':
				occs.append(site_occupancy[i])
		occ_metrics[seq] = [len(occs), round(st.mean(occs), 4), round(st.median(occs), 4)]
		#occupied sites
		#print(seq, len(occs), round(st.mean(occs), 4), round(st.median(occs), 4))
	
	sorted_median_occs = sorted(list(occ_metrics.keys()), key = lambda x: occ_metrics[x][2], reverse=True)
	for m in sorted_median_occs:
		print(m + '\t' + str(occ_metrics[m][2]))
if __name__ == "__main__":
  main(sys.argv)
