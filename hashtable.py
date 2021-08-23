class Hashtable:
    def __init__(self, max=1):
        self.max = max
        self.arr = [[] for i in range(self.max)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        
        found =False
        for index, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][index] = (key,value)
                found = True
                break
        
        if not found:
            self.arr[h].append((key,value))
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0]==key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, kv in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

t = Hashtable(10)
getHash = t.get_hash("march 2")
print(getHash)
t["march 2"] = 100
print(t.arr)
getvalue = t["march 2"]
print(getvalue)
del t["march 2"]

