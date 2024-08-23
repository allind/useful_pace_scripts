#! /usr/bin/env python
from ete3 import NCBITaxa
import sys
def main(argv):
		

	for line in open(sys.argv[1]):
		#ncbi = NCBITaxa("/pollard/data/projects/alind/eukdetect/ncbi_met_and_arch/busco/alien/nr_dl/taxdump-current/taxa.sqlite")
		ncbi = NCBITaxa()
		line = line.strip('\n')
		#taxid = line.split('\t')[1].split(';')[0]
		species = line.split("\t")[0]
		#if len(taxid) < 1:
		#	lineage = "Noinfo"
		#else:
		#taxid = int(taxid)
		classes = []
		#print(species)
		#print(ncbi.get_name_translator([species]))
		if len(list(ncbi.get_name_translator([species]).values())) == 0:
			taxid=1
		else:
			taxid = list(ncbi.get_name_translator([species]).values())[0][0]
		#print(taxid)

		lineage = ncbi.get_lineage(taxid)
		ranks = ncbi.get_rank(lineage)			
		rank_ids = {ranks[v]:v for v in ranks}
		#if "phylum" in rank_ids:
		#	classes.append(list(ncbi.get_taxid_translator([rank_ids["phylum"]]).values())[0])
		#if "clade" in rank_ids:
		#	print(rank_ids)
		#	classes.append(list(ncbi.get_taxid_translator([rank_ids["clade"]]).values())[0])
		#elif "kingdom" in rank_ids:
		#	classes.append(list(ncbi.get_taxid_translator([rank_ids["kingdom"]]).values())[0])
		#else:
		#	classes.append("Noclass")
		#classes = set(classes)
		if 33634 in ranks:
			print(species + '\t' + "Stramenopiles")
		#lineage = "-".join(classes).replace(' ', '_')
		#print(gene + '\t' + lineage + '-' + gene)
		#print(species + '\t' + lineage)
if __name__ == "__main__":
  main(sys.argv)
