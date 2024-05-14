

import json
import os
import time


class PokeCount(object):
    def __init__(self, path):
        self.file_name = "poke_count"
        self.path = path + "/" + self.file_name + ".json"
        self.cur_path = path + "/" + self.file_name + "_" + time.strftime("%Y%m%d", time.localtime()) + "_" + ".json"

        f = None
        cur_f = None
        try:
            if os.path.exists(self.path) is False:
                f = open(self.path, 'w', encoding="utf8")

            if os.path.exists(self.cur_path) is False:
                cur_f = open(self.cur_path, 'w', encoding="utf8")
        finally:
            if f:
                f.close()
            if cur_f:
                cur_f.close()


    def load_file(self, path):
        f = None
        try:
            f = open(path, 'r', encoding="utf8")
            jsonStr = f.read()
            if jsonStr is None or jsonStr == '':
                return {}
            return json.loads(jsonStr)
        finally:
            if f:
                f.close()

    def save_file(self, path, pokeJson):
        f = None
        try:
            f = open(path, 'w', encoding="utf8")
            str = json.dumps(pokeJson, ensure_ascii=False)
            # print(str)
            f.write(str)
        finally:
            if f:
                f.close()

    def increament(self, poke, size):
        pokeMap = self.load_file(self.path)
        if poke in pokeMap:
            pokeMap[poke] = pokeMap[poke] + size
        else:
            pokeMap[poke] = size
        self.save_file(self.path, pokeMap)

        pokeMap = self.load_file(self.cur_path)
        if poke in pokeMap:
            pokeMap[poke] = pokeMap[poke] + size
        else:
            pokeMap[poke] = size
        self.save_file(self.cur_path, pokeMap)

    def del_poke(self, poke):
        pokeMap = self.load_file(self.path)
        if poke in pokeMap:
            pokeMap.pop(poke)
        self.save_file(self.path, pokeMap)

        pokeMap = self.load_file(self.cur_path)
        if poke in pokeMap:
            pokeMap.pop(poke)
        self.save_file(self.cur_path, pokeMap)

    def show_count(self):
        pokeMap = self.load_file(self.cur_path)
        for key in pokeMap.keys():
            print("poke: %s , count: %d" % (key, pokeMap[key]))

    def show_count_origin(self):
        pokeMap = self.load_file(self.path)
        for key in pokeMap.keys():
            print("poke: %s , count: %d" % (key, pokeMap[key]))



# path = os.path.join(os.path.expanduser("~"), "Desktop")
# pokeCount = PokeCount(path)
# js = pokeCount.load_file(pokeCount.cur_path)
# pokeCount.increament("2323",3)
# pokeCount.increament("s11c",3)
# pokeCount.increament("大嘴sdc富",3)
# pokeCount.increament("大嘴av富",3)
# pokeCount.increament("香港",3)
# pokeCount.show_count()
# print("--------- del -----------")
# pokeCount.del_poke("test4")
# pokeCount.show_count()
# print("--------- origin -----------")
# pokeCount.show_count_origin()

