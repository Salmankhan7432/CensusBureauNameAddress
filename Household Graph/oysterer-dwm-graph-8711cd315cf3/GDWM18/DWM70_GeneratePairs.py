#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import DWM10_Parms

def generatePairs(logFile, mu, compareCache):
    print('\n>>Starting DWM70')
    print('\n>>Starting DWM70', file=logFile)
    pairList = []
    for key in compareCache:
        similarity = compareCache[key]
        if similarity >= mu:
            part = key.split(':')
            refID1 = part[0]
            refID2 = part[1]
            pairList.append((refID1, refID2))
    print('Total Pairs Linked =', len(pairList), ' at mu=', mu)
    print('Total Pairs Linked =', len(pairList), ' at mu=', mu, file=logFile)
    return pairList


def generatePairs2(logFile, compareCache):
    print('\n>>Starting DWM70')
    print('\n>>Starting DWM70', file=logFile)
    pairList = []
    for key in compareCache:
        similarity = compareCache[key]
        if similarity >= DWM10_Parms.mu:
            part = key.split(':')
            refID1 = part[0]
            refID2 = part[1]
            pairList.append((refID1, refID2, similarity))
    print('Total Pairs Linked =', len(pairList), ' at mu=', DWM10_Parms.mu)
    print('Total Pairs Linked =', len(pairList), ' at mu=', DWM10_Parms.mu, file=logFile)
    return pairList
