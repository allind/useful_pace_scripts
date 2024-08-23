#! /usr/bin/env python
import sys
def main(argv):

	for line in open(sys.argv[1]):
		line = line.strip('\n')
		if "#" not in line:

			#gene id, ec, hmmer, dbcan, diamond

			geneid = line.split('\t')[0]
			ec = line.split('\t')[1]
			hmmer = line.split('\t')[2]
			dbcan = line.split('\t')[3]
			diamond = line.split('\t')[4]

			if "+" in line:
				hmmer_parsed = [e.split('(')[0] for e in hmmer.split('+')]
				dbcan_parsed = [e.split('_')[0] for e in dbcan.split('+')]
				diamond_parsed = [e for e in diamond.split('+') if "." not in e]
				all_ids = list(set(hmmer_parsed + dbcan_parsed + diamond_parsed))
				if "-" in all_ids:
					all_ids.remove('-')

				gh = "+".join(all_ids)
			else:
				hmmer_parsed = hmmer.split('(')[0]
				dbcan_parsed = dbcan.split('_')[0]

				all_ids = list(set([hmmer_parsed, dbcan_parsed, diamond]))
				if "-" in all_ids:
					all_ids.remove('-')
				if len(all_ids) > 1:
					#check if subfam
					major_fam = []
					for l in all_ids:
						if "_" in l:
							major_fam.append(l.split('_')[0])
						else:
							major_fam.append(l)
					if len(list(set(major_fam))) == 1:
						gh = list(set(major_fam))[0]
					else:
						print("ERROR: Disagreement " + line)
				else:
					gh = all_ids[0]
			
			print(geneid + '\t' + gh)
			
if __name__ == "__main__":
  main(sys.argv)
