class Jar:
    def __init__(self, capacity=0):

        if capacity >= 0 :
            self.capacity = capacity
        else:
            raise ValueError("Value Error")    
        

    def __str__(self):
        return self.capacity *"🍪"


    def deposit(self, n):

        if self.capacity < 12:
            self.capacity = n + self.capacity 
        else:
            raise ValueError("Value Error")

    def withdraw(self, n):
        if 0 < self.capacity <= 12 and n < self.capacity:
            return self.capacity - n
        else: 
            raise ValueError("Value Error")
        

    @property
    def capacity(self):
        return self.capacity
    @capacity.setter
    def capacity(self,capacity):
        self._capacity = capacity


    @property
    def size(self):
        return self.size
    @size.setter
    def size(self,size):

        self._size = size
