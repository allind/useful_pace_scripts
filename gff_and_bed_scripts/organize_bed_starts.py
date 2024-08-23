#! /usr/bin/env python
import sys
def main(argv):

	for line in open(sys.argv[1]):
		line = line.strip('\n')
		start = int(line.split('\t')[1])

		end = int(line.split('\t')[2])
		if start > end:
			tmp = start
			start = end
			end = tmp
		toprint = (line.split('\t')[0] + '\t' + str(start) + '\t' + str(end))
		if len(line.split('\t')) > 2:
			toprint += "\t" + "\t".join(line.split('\t')[3:])
		print(toprint)
			
if __name__ == "__main__":
  main(sys.argv)
