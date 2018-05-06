
# -*- coding: utf-8 -*-

TILES_NUM_INHANDS=14
TILES_NUM_MAX=18        #四槓子の場合

class MajongRoleDetection:
    def __init__(self,handtiles,agari,furotiles=[],tenpai_check=False):
        # todo:テンパイチェック機能をつける。
        # todo:カンチェック機能をつける。
        # ポン・チーの場合の条件分岐をつける。
        # カンの場合どうするか・・・
        if len(handtiles) + len(furotiles) > TILES_NUM_MAX - 1:
            raise(ValueError ("too many tiles"))
        self.handtiles = sorted(handtiles)
        self.furotiles = sorted(furotiles)
        self.agari = agari

    def getTiles(self):
        return {'tiles': self.handtiles, 'agari':self.agari} 

    def isKokushiMusou(self,juusanmen=False):
        kokushi_hands = [1,9,11,19,21,29,31,32,33,34,41,42,43]
        alltiles = self.handtiles[:]        #copy list
        if juusanmen == True:
            return set(alltiles) == set(kokushi_hands) and self.agari in kokushi_hands
        alltiles.append(self.agari)     #add tsumo to list
        return set(alltiles) == set([1,9,11,19,21,29,31,32,33,34,41,42,43])

    def isChitoitsu(self):
        alltiles = self.handtiles[:]
        alltiles.append(self.agari)
        for tile in set(alltiles):
            if alltiles.count(tile) != 2:
                return False

        return True

    def append_pattern(self,pattern_list,pattern):
        flag=True
        for p in pattern_list:
            if p == pattern:
                flag=False
        if flag == True:
            p2 = {
                "atama": pattern["atama"],
                "anko": pattern["anko"],
                "shuntsu": pattern["shuntsu"],
                "remain": pattern["remain"]
            }
            pattern_list.append(p2)

    def mentsu_pattern(self,patterns,results):
        next_patterns = []
        for p in patterns:
            shuntsu = list(p["shuntsu"])
            anko =  list(p["anko"])
            shuntsutiles = list(p["remain"])
            for t in shuntsutiles:
                if shuntsutiles.count(t) > 0 and shuntsutiles.count(t+1) > 0 and shuntsutiles.count(t+2) > 0:
                    shuntsu.append(t)
                    for i in [0,1,2]:
                        shuntsutiles.remove(t+i)
                    p2 = {
                        "atama":int(p["atama"]),
                        "anko":sorted(anko),
                        "shuntsu":sorted(shuntsu),
                        "remain":sorted(shuntsutiles)
                        }
                    self.append_pattern(next_patterns,p2)
                    break

            shuntsu = list(p["shuntsu"])
            anko =  list(p["anko"])
            ankotiles = list(p["remain"])
            for t in ankotiles:
                num = ankotiles.count(t)
                if num == 3:
                    anko.append(t)
                    for i in [0,1,2]:       #３個消す
                        ankotiles.remove(t)
                    p2 = {
                        "atama":int(p["atama"]),
                        "anko":sorted(anko),
                        "shuntsu":sorted(shuntsu),
                        "remain":sorted(ankotiles)
                        }
                    self.append_pattern(next_patterns,p2)
                    break

        #print(next_patterns)
        #print "\n"
        #print "results="+str(results)

        flag=True
        for np in next_patterns:
            if len(np["remain"]) < 1:
                r={"atama":int(np["atama"]),"anko":sorted(list(np["anko"])),"shuntsu":sorted(list(np["shuntsu"]))}
                results.append(r)
            else:
                flag=False

        if flag==False:
            self.mentsu_pattern(next_patterns,results)
                
    def agari_pattern(self):
        alltiles = self.handtiles[:]
        alltiles.append(self.agari)
        #２枚以上あるのを頭候補としてとする
        patterns = []
        results = []
        for tile in set(alltiles):
            num = alltiles.count(tile)
            if num in [2,3]:
                remain_tile=alltiles[:]
                for i in [0,1]:       #２個消す
                    remain_tile.remove(tile)
                p = {"remain":remain_tile[:], "atama": tile, "anko":[], "shuntsu":[]}
                patterns.append(p)

        results = []
        self.mentsu_pattern(patterns,results)

        print "r="+str(results)
        return results

    def removeAnko(self,remain_tiles):
        pass


    def isToitoi(self):
        pass

    def isSuanko(self):
        pass

    def isDaisangen(self):

        pass
    

class MajongPointCalculate:
    tiles = []

    def __init__(self,tiles,tsumo):
        self.tiles = sorted(tiles)
        self.tsumo = tsumo

    def getTiles(self):
        return {'tiles': self.tiles, 'tsumo':self.tsumo} 

if __name__=='__main__':
    pass