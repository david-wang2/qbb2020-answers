#!/usr/bin/env python3

import sys
from fasta_iterator_class import FASTAReader

target = sys.argv[1]
query = sys.argv[2]
k = int(sys.argv[3])

#target = 'subset.fa'
#query = 'droYak2_seq.fa'
#k = 11

query_kmers = {}
for seq_id, sequence in FASTAReader(open(query)):
    for i in range(0,len(sequence)-k+1):
        kmer = sequence[i:(i+k)].upper()
        query_kmers.setdefault(kmer,[])
        query_kmers[kmer].append(i)

kmers_matched = []
outStr = ""
for seq_id, sequence in FASTAReader(open(target)):
    target_kmers = {}
    for i in range(0,len(sequence)-k+1):
        kmer = sequence[i:(i+k)].upper()
        target_kmers.setdefault(kmer,[])
        target_kmers[kmer].append(i)
    for kmer in query_kmers.keys():
        if kmer in target_kmers.keys():
            print(kmer)
            kmers_matched.append((seq_id,str(target_kmers[kmer]),str(query_kmers[kmer]),str(kmer)))
            outStr += seq_id + ', ' + str(target_kmers[kmer]) + ', ' + str(query_kmers[kmer]) + ', ' + str(kmer) + '\n'

with open('output.dat','w') as f:
    f.write(outStr)
