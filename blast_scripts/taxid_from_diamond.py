#! /usr/bin/env python
from ete3 import NCBITaxa
import sys
def main(argv):

	ncbi = NCBITaxa()
	count = {}
	taxes = {}
	taxids = {}
	phyla = {}
	for line in open(sys.argv[1]):
		line = line.strip('\n')
		if len(line.split('\t')[17]) > 0:
			taxid = int(line.split('\t')[17])
			gene = line.split('\t')[0]
			if gene not in count:
				count[gene] = 0
			if gene not in taxes:
				taxes[gene] = []
				taxids[gene] = []
				phyla[gene] = []
			if count[gene] < 5:

				taxname = list(set(ncbi.get_taxid_translator([taxid]).values()))[0]
				taxes[gene].append(taxname)
				taxids[gene].append(taxid)
				#print(gene)
				#print(line)
				#print(ncbi.get_lineage_translator([taxid]))
				#print(line)
				#print(ncbi.get_lineage_translator([taxid]))
				
				if bool(ncbi.get_lineage_translator([taxid])) and len(list(ncbi.get_lineage_translator([taxid]).values())[0]) > 2:
					ranks = ncbi.get_rank(e for e in ncbi.get_lineage_translator([taxid])[taxid])
					rank_s = {ranks[e]: e for e in ranks}
					names = ncbi.get_taxid_translator(ncbi.get_rank(e for e in ncbi.get_lineage_translator([taxid])[taxid]))
					if "phylum" in rank_s:
						phyla[gene].append(names[rank_s['phylum']])
					elif "clade" in rank_s:
						phyla[gene].append(names[rank_s['clade']])

			count[gene] += 1

	for tax in taxes:
		print(tax + '\t' + ','.join(taxes[tax]) + '\t' + ",".join(phyla[tax]))
if __name__ == "__main__":
  main(sys.argv)
