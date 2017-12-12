class CoordinateStore(object):
    def __init__(self,size):
        self.size = size
        self.store = {}
        for row in range(self.size[1]+1):
            self.store[row] = [None]*(self.size[0]+1)

    def get_at(self, x,y):
        return self.store[y][x]

    def edit(self,x,y,value):
        self.store[y][x] = value

