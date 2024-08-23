#! /usr/bin/env python
#input: script.py gff
import sys
def main(argv):

	gff = open(sys.argv[1])
	for line in gff:
		line = line.strip('\n')
		if len(line) > 1 and "#" not in line[0] and line.split('\t')[2] == "transcript":
			genename = line.split('\t')[-1].split(';')[1].split('=')[1]
			chrom = line.split('\t')[0]
			print(chrom + '\t' + genename + '\t' + line.split('\t')[3] + '\t' + line.split('\t')[4])
if __name__ == "__main__":
	main(sys.argv)

