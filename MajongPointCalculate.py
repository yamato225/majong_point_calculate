
# -*- coding: utf-8 -*-

TILES_NUM_INHANDS=14

class MajongPointCalculate:
    tiles = []

    def __init__(self,tiles,tsumo):
        if len(tiles) != TILES_NUM_INHANDS - 1:
            raise ValueError("wrong tiles")
        self.tiles = sorted(tiles)
        self.tsumo = tsumo

    def getTiles(self):
        return {'tiles': self.tiles, 'tsumo':self.tsumo} 

    def isKokushiMusou(self):
        alltiles = self.tiles[:]        #copy list
        alltiles.append(self.tsumo)     #add tsumo to list
        return set(alltiles) == set([1,9,11,19,21,29,31,32,33,34,41,42,43])

if __name__=='__main__':
    pass