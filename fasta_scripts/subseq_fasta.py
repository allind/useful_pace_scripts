#! /usr/bin/env python
from Bio import SeqIO
from Bio.Seq import Seq
import sys
def main(argv):
    
    contig = sys.argv[2]
    start = int(sys.argv[3])
    end = int(sys.argv[4])
    rc = False
    if start > end:
        tmp = end
        end = start
        start = tmp
        rc = True
    for seq in SeqIO.parse(sys.argv[1], 'fasta'):
        if seq.id == contig:
            if rc:
                print(">" + seq.id + ":" + str(start) + '-' + str(end) + '-')
                print(str(Seq(str(seq.seq)[start-1:end]).reverse_complement()))
            else:
                print(">" + seq.id + ":" + str(start) + '-' + str(end) + '+')
                print(str(seq.seq)[start-1:end])


if __name__ == "__main__":
  main(sys.argv)
