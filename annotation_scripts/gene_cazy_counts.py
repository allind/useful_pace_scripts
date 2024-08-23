#! /usr/bin/env python
import sys
def main(argv):
	
	filenums = len(sys.argv[1:])
	filenames = sys.argv[1:]
	headers = [f.split('/')[-1].split('_')[0] for f in filenames]
	
	#pfam_counts = {line.split('-')[0].strip('\n'): {} for line in open(sys.argv[1])}
	pfam_counts = {}
	for i in range(0, len(headers)):
		f = filenames[i]
		for line in open(f):
			pfams = list(set([e for e in line.split('\t')[15].split('+')]))
			for p in pfams:
				if p not in pfam_counts:
					pfam_counts[p] = {}
					for h in headers:
						pfam_counts[p][h] = 0
	#for p in pfam_counts:
	#	for f in headers:
		#	pfam_counts[p][f] = 0

	for i in range(0, len(headers)):
		name=headers[i]
		f = filenames[i]
		for line in open(f):
			line = line.strip('\n')
			#pthr = line.split('\t')[7].split('-')[0]
			#if pthr in pfam_counts:
			#	pfam_counts[pthr][name] += 1

			#pfams = list(set(['IPR' + e.split('-')[0] for e in line.split('\t')[14].split('IPR')]))
			pfams = list(set([e for e in line.split('\t')[15].split('+')]))
			#pfams = line.split('\t')[15].split(',')
			
			#print(line.split('\t')[14])
			for p in pfams:
				if p in pfam_counts:
					pfam_counts[p][name] += 1
	print("Cazy\t" + "\t".join(headers))
	for p in pfam_counts:
		toprint=p + '\t'
		for h in headers:
			toprint += str(pfam_counts[p][h]) + '\t'
		print(toprint)

			
			

if __name__ == "__main__":
  main(sys.argv)
