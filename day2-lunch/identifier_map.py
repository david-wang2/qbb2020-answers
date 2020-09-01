#!/usr/bin/env python

"""Auto-run change the output"""

__author__ = "David Wang"
__copyright__ = "Copyright 2020, Johns Hopkins University"
__credits__ = ["David Wang"]
__license__ = "None"
__version__ = "0.1"
__maintainer__ = "David Wang"
__email__ = "dwang106@jhu.edu"
__status__ = "Production"

import sys

def map_identifier(mapPath,ctabPath,default):
    # parse the map file to create a dictionary
    flymap = dict()
    with open(mapPath,'r') as f:
        for line in f:
            flybase = line.split('\t')[0]
            uniprot = line.split('\t')[1].split('\n')[0]
            flymap[flybase] = uniprot

    # parse ctabfile to find whether the gene names are there
    lstOut = []
    with open(ctabPath,'r') as f:
        flag = True
        for line in f:
            if (flag):
                lstOut.append(line)
                flag = False
            else:
                # find the gene name
                geneName = line.split()[8]
                if geneName in flymap.keys():
                    lstOut.append(line.split(geneName)[0] + flymap[geneName] + line.split(geneName)[1])
                elif(default):
                    lstOut.append(line.split(geneName)[0] + 'N\A' + line.split(geneName)[1])

    outStr = ""
    count = 0
    for i in range(len(lstOut)):
        if (count < 100):
            outStr += lstOut[i]
        else:
            break
        count += 1
    
    return outStr

if __name__ == "__main__":
    # Decomposes arguments in order to find the path
    mapPath = ""
    ctabPath = ""
    default = ""
    args = sys.argv
    for i in range(len(args)):
        if (args[i] == '-m'):
            mapPath = args[i+1]
        elif (args[i] == '-c'):
            ctabPath = args[i+1]
        elif (args[i] == '-d'):
            default = bool(args[i+1])
    
    mapPath = '/home/protein/Documents/qbb_bootcamp/qbb2020-answers/day2-lunch/parsed_map.dat'
    ctabPath = '/home/protein/Documents/qbb_bootcamp/qbb2020-answers/day2-lunch/stringtie/SRR072893/t_data.ctab'
    
    default = True
    out = map_identifier(mapPath,ctabPath,default)
    outFile = "mapped_t_data.ctab"
    with open(outFile,'w') as f:
        f.write(out)

    default = False
    out = map_identifier(mapPath,ctabPath,default)
    outFile = "mapped_t_data_noDefault.ctab"
    with open(outFile,'w') as f:
        f.write(out)
