#! /usr/bin/env python
import sys,re
def main(argv):
	

	all_iprs = {}
	
	filenums = len(sys.argv[1:])
	filenames = sys.argv[1:]
	headers = [f.split('/')[-1].split('_')[0] for f in filenames]
	pfam_ids = {line.split('-')[0]: '-'.join(line.split('-')[1:]).strip('\n') for line in open(sys.argv[1])}
	#pfam_ids = {line.split('\t')[0]: line.split('\t')[1].strip('\n')for line in open(sys.argv[1])}
	pfam_ids = {}

	pfam_counts = {}
	for i in range(0, len(headers)):
		name = headers[i]
		f = filenames[i]
		ofile = open(f)
		ofile.readline()
		for line in ofile:
			if len(line.split('\t')[14]) > 2:
				line = line.strip('\n')
				pline = line.split('\t')[14]
				pfams = re.findall('IPR\d*',pline,re.DOTALL)
				ids = re.split('IPR\d*\-', pline,maxsplit=200)
				p_ids = {pfams[i]: re.sub(' \(\d*\)', '', ids[i+1].strip(',')) for i in range(0, len(pfams))}
				for p in pfams:
					if p not in pfam_counts:
						pfam_counts[p] = {}
						for f in headers:
							pfam_counts[p][f] = 0
					if p not in pfam_ids:
						pfam_ids[p] = p_ids[p]
	for i in range(0, len(headers)):
		name=headers[i]
		f = filenames[i]
		for line in open(f):
			line = line.strip('\n')
			#pthr = line.split('\t')[7].split('-')[0]
			#if pthr in pfam_counts:
			#	pfam_counts[pthr][name] += 1

			pfams = list(set(['IPR' + e.split('-')[0] for e in line.split('\t')[14].split('IPR')]))
			#pfams = line.split('\t')[15].split(',')
			
			#print(line.split('\t')[14])
			for p in pfams:
				if p in pfam_counts:
					pfam_counts[p][name] += 1
	print("IPR\tAnnot\t" + "\t".join(headers))
	for p in pfam_counts:
		toprint=p + '\t' + pfam_ids[p] + '\t'
		for h in headers:
			toprint += str(pfam_counts[p][h]) + '\t'
		print(toprint)

			
			

if __name__ == "__main__":
  main(sys.argv)
