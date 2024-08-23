#! /usr/bin/env python
import sys
def main(argv):

	genes = {}
	for line in open(sys.argv[1]):
		gene = line.split("\t")[0]
		if gene not in genes:
			genes[gene] = []
		if len(line.split('\t')) > 13:
			gos = [x.split('(')[0] for x in line.split('\t')[13].split('|')]
			for g in gos:
				if g not in genes[gene] and g != "-":
					genes[gene].append(g)
	#print(genes['g60093.t1'])
	#sys.exit()
	for g in genes:
		if len(genes[g]) < 1:
			print(g + '\t-')
		else:
			print(g + '\t' + ",".join(genes[g]))
		
if __name__ == "__main__":
  main(sys.argv)
