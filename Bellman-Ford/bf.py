import logging
import sys
from optparse import OptionParser
from collections import defaultdict

log_level=logging.DEBUG
log = logging.getLogger(__name__)
log.setLevel(log_level)

handler = logging.FileHandler('bf.log')
handler.setLevel(log_level)
log.addHandler(handler)

def BF(s, V, G):
    L = [ dict([ (v, sys.maxint) if v != s else (s, 0) for v in V]) ]
    L.extend([ dict([(v, None) for v in V]) for i in range(len(V)-1) ])


    for i in range(1,len(V)):
        for v in V:
            log.debug("i: {}\tv: {}".format(i,v))
            if s == v:
                L[i][v] = 0
            else:
                log.debug("L[i-1]: {}".format(L[i-1]))
                possible_transitions = [L[i-1][u]+w for u, w in G[v]]
                possible_transitions.append(sys.maxint)
                tmp_min = min(possible_transitions)
                L[i][v] = min([tmp_min, L[i-1][v]])
    tmp = dict([(v,None) for v in V])
    for v in V:
        possible_transitions = [L[-1][u]+w for u, w in G[v]]
        possible_transitions.append(sys.maxint)
        tmp_min = min(possible_transitions)
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
    log.info("Filename: {}\tStarting vertex: {}".format(filename, s))
    G = defaultdict(list)
    V = set()
    with open(filename, 'r') as f:
        for line in f.readlines():
            v1, v2, w = [int(x) for x in line.split()]
            G[v2].append( (v1, int(w)) )
            V.add(v1)
            V.add(v2)
    if log_level == logging.DEBUG:
        log.debug("Graph G: {}".format(G))
    print BF(s, V, G)
