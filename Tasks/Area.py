class rec:
    def __init__(self,w = 0,l = 0):
        self.width = w
        self.length = l
    def Area(self):
        return self.width*self.length


E1 = rec()

E1.width = 5
E1.length = 6

print(E1.Area())



