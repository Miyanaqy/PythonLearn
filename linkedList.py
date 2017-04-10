class Node(object):
    def __init__(self, data, _next=None):
        self.data = data
        self._next = _next

class LinkedList(object):
    def __init__(self):
        self.length = 0

    def getIndex(self, index):
        if index < 0 or index => self.length:
            print('error:out of bounds')
