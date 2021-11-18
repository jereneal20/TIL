class Element:
    def __init__(self, k: int):
        self.value = k

    value = -1
    next = None
    prev = None


class MyCircularDeque:
    maximum_size = -1
    current_size = 0

    def __init__(self, k: int):
        self.maximum_size = k
        self.front = None
        self.back = None

    def insertFront(self, value: int) -> bool:
        if self.current_size == self.maximum_size:
            return False

        elem = Element(value)
        if self.front:
            self.front.prev = elem
        elem.next = self.front

        self.front = elem
        if not self.back:
            self.back = self.front
        self.current_size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.current_size == self.maximum_size:
            return False
        elem = Element(value)
        if self.back:
            self.back.next = elem
        elem.prev = self.back

        self.back = elem
        if not self.front:
            self.front = self.back
        self.current_size += 1
        return True

    def deleteFront(self) -> bool:
        if self.current_size == 0:
            return False
        self.front = self.front.next
        if self.front:
            self.front.prev = None
        self.current_size -= 1
        if self.current_size == 0:
            self.back = None
        return True

    def deleteLast(self) -> bool:
        if self.current_size == 0:
            return False

        self.back = self.back.prev
        if self.back:
            self.back.next = None
        self.current_size -= 1
        if self.current_size == 0:
            self.front = None
        return True

    def getFront(self) -> int:
        if self.current_size == 0:
            return -1
        return self.front.value

    def getRear(self) -> int:
        if self.current_size == 0:
            return -1
        return self.back.value

    def isEmpty(self) -> bool:
        if self.current_size == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.current_size == self.maximum_size:
            return True
        return False

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()