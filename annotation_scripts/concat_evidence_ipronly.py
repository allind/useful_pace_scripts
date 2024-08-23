#!/usr/bin/env python
#usage: script.py [fasta] [interpro] [cdd] [cog] [kog] [prk] [tigr] [loc] [dbcan]
from Bio import SeqIO
import sys
def main(argv):
	#0-CDD,1-Gene3D,2-Hamap,3-PANTHER,4-Pfam,5-PIRSF,6-PRINTS,7-ProSitePatterns,8-ProSiteProfiles,9-SFLD,10-SMART,11-SUPERFAMILY,12-TIGRFAM,13-Interpro,14-cdd,15-cog,16-kog,17-prk,18-tigr
	#new:
	#0-CDD, 1-Coils, 2-FunFam, 3-Gene3D, 4-MobiDBLite, 5-NCBIfam, 6-PANTHER, 7-Pfam, 8-PIRSF, 9-PRINTS, 10-SFLD, 11-SMART, 12-SUPERFAMILY, 13-Interpro,14-cdd,15-cog,16-kog,17-prk,18-tigr
	seqs = {seq.id: [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []] for seq in SeqIO.parse(sys.argv[1], 'fasta')}
	
	#ipr_pos = {"CDD": 0, "Gene3D": 1, "Hamap": 2, "PANTHER": 3, "Pfam": 4, "PIRSF": 5, "PRINTS": 6, "ProSitePatterns": 7, "ProSiteProfiles": 8, "SFLD": 9, "SMART": 10, "SUPERFAMILY": 11, "TIGRFAM": 12}
	ipr_pos = {"CDD": 0,  "Coils": 1,  "FunFam": 2,  "Gene3D": 3,  "MobiDBLite": 4,  "NCBIfam": 5,  "PANTHER": 6,  "Pfam": 7,  "PIRSF": 8,  "PRINTS": 9,  "SFLD": 10,  "SMART": 11,  "SUPERFAMILY ": 12}
	for line in open(sys.argv[2]):
		line = line.strip('\n')
		gene = line.split('\t')[0]
		if len(line.split('\t')) >= 13 and '-' not in line.split('\t')[11]:
			seqs[gene][13].append("-".join(line.split('\t')[11:13]))
		ident = line.split('\t')[3]

		if ident in ipr_pos:
			pos = ipr_pos[ident]

			seqs[gene][pos].append('-'.join(line.split('\t')[4:6]).strip('--'))
	
	#cdd
#	for line in open(sys.argv[3]):
#		line = line.strip('\n')
#		gene = line.split('\t')[0].split(' ')[0]
#		if "Site" not in line:
#			seqs[gene][14].append('-'.join(line.split('\t')[9:11]))
	
	#cog
#	for line in open(sys.argv[4]):
#		line = line.strip('\n')
#		gene = line.split('\t')[0].split(' ')[0]
#		if "Site" not in line:
#			seqs[gene][15].append('-'.join(line.split('\t')[9:11]))
	
	#kog
#	for line in open(sys.argv[5]):
#		line = line.strip('\n')
#		gene = line.split('\t')[0].split(' ')[0]
#		seqs[gene][16].append(line.split('\t')[12])
	
	#prk
#	for line in open(sys.argv[6]):
#		line = line.strip('\n')
#		gene = line.split('\t')[0].split(' ')[0]
#		if "Site" not in line:
#			seqs[gene][17].append('-'.join(line.split('\t')[9:11]))
	
#	#tigr
#	for line in open(sys.argv[7]):
#		line = line.strip('\n')
#		gene = line.split('\t')[0].split(' ')[0]
#		if "Site" not in line:
#			seqs[gene][18].append('-'.join(line.split('\t')[9:11]))
	
	#deeploc
#	deep = open(sys.argv[3])
#	deep.readline()
#	for line in deep:
#		line = line.strip('\n')
#		gene = line.split(',')[0]
#		loc = line.split(',')[1]
#		ev = line.split(',')[2]
#		name = loc + '-' + ev
#		seqs[gene][14].append(name.strip('-'))
	

	#dbcan = open(sys.argv[3])
	#for line in dbcan:
#		line = line.strip('\n')
#		gene = line.split('\t')[0]
#		annot = line.split('\t')[1]
#		seqs[gene][15].append(annot)
	#get everything together
	#print("Gene\tCDD-IPR\tGene3D\tHamap\tPANTHER\tPfam\tPIRSF\tPRINTS\tProSitePatterns\tProSiteProfiles\tSFLD\tSMART\tSUPERFAMILY\tTIGRFAM\tInterpro\tcdd\tcog\tkog\tprk\ttigr\tdeeploc\tdbcan")#\tdeeptmhmm\tdbcan")
	print("Gene\tCDD-IPR\tGene3D\tHamap\tPANTHER\tPfam\tPIRSF\tPRINTS\tProSitePatterns\tProSiteProfiles\tSFLD\tSMART\tSUPERFAMILY\tTIGRFAM\tInterpro\tdbcan")
	for seq in seqs:
		toprint = seq + '\t'
		for e in seqs[seq]:
			
			if len(e) > 0 and len(e[0]) > 1:
				uniq = list(set(e))
				if len(uniq) < len(e):
					add = ""
					for j in uniq:
						add += j + ' (' + str(e.count(j)) + '),'
					add = add.strip(',')
					toprint += add + '\t' 
				else:
					toprint += ",".join(e) + '\t'
			else:
				toprint += "-\t"
		toprint = toprint.strip('\t')
		print(toprint)
if __name__ == "__main__":
  main(sys.argv)
