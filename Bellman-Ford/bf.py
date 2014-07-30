import logging
import sys
from optparse import OptionParser
from collections import defaultdict

log_level=logging.INFO
log = logging.getLogger(__name__)
log.setLevel(log_level)

handler = logging.FileHandler('bf.log')
handler.setLevel(log_level)
log.addHandler(handler)

def BF(s, G):
    L = [ [sys.maxint if v != s else 0 for v in G.keys()] ]
    L.extend([ [None]*len(G.keys()) for i in range(len(G.keys())-1) ])

    for i in range(1,len(G.keys())):
        for v in G.keys():
            if s == v:
                L[i][v] = 0
            else:
                tmp_min = min([L[i-1][u]+w for u, w in G[v]])
                L[i][v] = min([tmp_min, L[i-1][v]])
    tmp = [None]*len(G.keys())
    for v in G.keys():
        tmp_min = min([L[-1][u]+w for u, w in G[v]])
        tmp[v] = min([tmp_min, L[-1][v]])
    if tmp != L[-1]:
        return None
    return L[-1]

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-f")
    parser.add_option("-s")
    option, args = parser.parse_args()
    
    filename = option.f
    s = int(option.s)
    log.info("Filename: {}".format(filename))
    G = defaultdict(list)
    with open(filename, 'r') as f:
        for line in f.readlines():
            v1, v2, w = [int(x) for x in line.split()]
            G[v1].append( (v2, int(w)) )
            G[v2].append( (v1, int(w)) )
    print BF(s, G)
