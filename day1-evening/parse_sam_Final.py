#!/usr/bin/env python

import numpy as np

numAlign = 0
numMatch = 0
chrom10 = []
lstMapq = []
num2l = 0
with open('SRR072893.sam','r') as f:
    for line in f:
        # count number of alignments
        numAlign += 1
        # count number of alignments that match perfectly to genome
        alignScore = int(line.split('NM:i:')[1].split('\t')[0])
        if alignScore == 0:
            numMatch += 1
        # for first 10 alginments print just the column indicating which chromosome read
        if numAlign <= 10:
            chrom10.append(line.split('\t')[2].split('\t')[0])
        # list of mapq scores
        lstMapq.append(int(line.split('\t')[4].split('\t')[0]))
        # number of reads that start alignment on chromosome 2L between base 10000 and 20000
        chromNum = line.split('\t')[2].split('\t')[0]
        baseStart = int(line.split('\t')[3].split('\t')[0])
        if (chromNum == '2L') and (baseStart >= 10000 and baseStart <= 20000):
            num2l += 1

print(numAlign)
print(numMatch)
print(chrom10)
print(np.average(lstMapq))
print(num2l)

#Count number of alignments
#Count number of alignments that match perfectly to the genome
#HINT: This is encoded in one of the sam format's optional fields.
#For the first 10 alignments, print just the column indicating which chromosome a given read aligns to
#HINT: .split()
#Calculate average MAPQ score across all reads
#HINT: think about string and numeric type conversions
#Count number of reads that start their alignment on chromosome 2L between base 10000 and 20000 (inclusive)
