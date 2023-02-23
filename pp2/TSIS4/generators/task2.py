class Even:
    def __init__(self, max):
        self.x = 0
        self.max = max
    def __iter__(self):
        return self
    def __next__(self):
        self.x += 2
        if(self.x > self.max):
            raise StopIteration
        else:
            return self.x
    __call__ = __next__

n = int(input())
gen = iter(Even(n), n)

for i in gen:
    print(i)