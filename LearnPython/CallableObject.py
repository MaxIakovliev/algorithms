import random
class PickRandom:
    def __init__(self, items):
        self._items=list(items)
        random.shuffle(self._items)
    
    def pick(self):
        try:
            return self._items.pop()
        except Exception as e:
            print(str(e))
    
    def __call__(self):
        return self.pick()

if __name__ =='__main__':
# here is few example how  pick method can be called
    p=PickRandom(range(9))
    print(p.pick())
    print(p())
