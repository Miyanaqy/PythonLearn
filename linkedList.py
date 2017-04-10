class Node(object):
    def __init__(self, data, _next=None):
        self.data = data
        self._next = _next
    def __repr__(self):
        return str(self.data)

class LinkedList(object):
    def __init__(self):
        self.length = 0
        self.node = Node("Null")
        self.endNode = self.node

    def isEmpty(self):
        return (self.length == 0)

    def append(self, data):
        node = Node(data)
        self.endNode._next = node
        self.endNode = node
        self.length += 1

    def insert(self, data, index):
        if self.isEmpty():
            print("This linked list is empty.")
            return
        if index < 0 or index >= self.length:
            print('error:out of bounds')
            return
        node = self.node
        for i in range(index):
            node = node._next
        q = Node(data)
        q._next = node._next
        node._next = q
        self.length += 1

    def delete(self, index):
        if self.isEmpty():
            print("This linked list is empty.")
            return
        if index < 0 or index >= self.length:
            print('error:out of bounds')
            return
        node = self.node
        for i in range(index):
            node = node._next
        q = node._next
        node._next = q._next
        self.length -= 1

    def getElem(self, index):
        if self.isEmpty():
            print("This linked list is empty.")
            return
        if index < 0 or index >= self.length:
            print('error:out of bounds')
            return
        node = self.node
        for i in range(index+1):
            node = node._next
        return node.data

    def getIndex(self, data):
        if self.isEmpty():
            print("This linked list is empty.")
            return
        node = self.node
        j = 0
        while(node._next != None):
            node = node._next
            if node.data == data:
                return j
            j += 1
        print('list have not %s' % data)

    def update(self, data, index):
        node = self.node
        for i in range(index+1):
            node = node._next
        node.data = data

    def __repr__(self):
        if self.isEmpty():
            return "This linked list is empty."
        node = self.node
        strlist = ''
        for i in range(self.length):
            node = node._next
            strlist += str(node.data) + ' '
        return strlist
        
ll = LinkedList()
for i in range(10):
    ll.append(i)

print(ll)
print(ll.getIndex(5))
ll.update(10,0)
print(ll)
ll.delete(10)
ll.delete(0)
print(ll)
ll.insert(100, 0)
print(ll)
print(ll.getElem(5))
