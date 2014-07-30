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
    L.extend([ [] for i in range(len(G.keys())-1) ])

    for i in range(1,len(G.keys())):
        

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-f")
    option, args = parser.parse_args()
    
    filename = option.f
    log.info("Filename: {}".format(filename))
    G = defaultdict(list)
    with open(filename, 'r') as f:
        for line in f.readlines():
            v1, v2, w = line.split()
            G[v1].append( (v2, int(w)) )
            G[v2].append( (v1, int(w)) )

