class Jar:
    def __init__(self, capacity=12):
        if capacity<0:
            raise ValueError
        self._capacity=capacity
        self.curr=0

    def __str__(self):
        return '🍪'*self.curr

    def deposit(self, n):
        if n+self.curr>self.capacity or n<0:
            raise ValueError
        else:
            self.curr=self.curr+n
       
    def withdraw(self, n):
       if self.curr-n<0 or n<0:
            raise ValueError
       else:
           self.curr=self.curr-n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.curr