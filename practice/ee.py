class CustomDict(object):
    def __init__(self):
        self.store = []

    def __getitem__(self, key):
        for item in self.store:
            if item[0] == key:
                result = item
                return result[1]
        else:
            return 'KeyError'
    
    def __setitem__(self, key, value):
        for item in self.store:
            if item[0] == key:
                item[1] = value
                break
        else:
            self.store.append([key, value])

cdict = CustomDict() 
cdict["a"] = 1 
cdict["b"] = 2
print(cdict["a"])  # 1
print(cdict["c"])  # KeyError