class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("wrong capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * '🍪'

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Exceeded the capacity")
        self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not enough cookies available")
        self._size -= n
        self._capacity += n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


jar = Jar()
jar.deposit(3)
jar.withdraw(1)
print(jar)
