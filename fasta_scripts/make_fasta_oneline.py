#!/usr/bin/env python
import sys
from Bio import SeqIO

def convert_to_single_line(input_file):
    for record in SeqIO.parse(input_file, "fasta"):
        print(f">{record.description}")
        print(record.seq)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_fasta>")
        sys.exit(1)

    input_file = sys.argv[1]

    convert_to_single_line(input_file)
