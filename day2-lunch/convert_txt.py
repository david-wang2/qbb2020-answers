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

if __name__ == "__main__":
    # Decomposes arguments in order to find the path
    path = ""
    ff = ""
    args = sys.argv
    for i in range(len(args)):
        if (args[i] == '-p'):
            path = args[i+1] + '/'
        if (args[i] == '-f'):
            ff = args[i+1]
    
    # Decompose file
    lstID = []
    with open('fly.txt','r') as f:
        for line in f:
            # check if the word DRONE is in the file line
            if 'DROME' in line:
                # split the line
                if len(line.split()) == 4:
                    lstID.append((line.split()[3],line.split()[2]))
                elif len(line.split()) == 5:
                    lstID.append((line.split()[4],line.split()[3]))

    outStr = ""
    for flybase, uniprot in lstID:
        outStr += flybase + '\t' + uniprot + '\n'

    outFile = "parsed_map.dat"
    with open(outFile,'w') as f:
        f.write(outStr)
