class Data():
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_list():
    def __init__(self):
        da = Data('point')
        self.head = da
    def add(self,data):
        da = Data(data)
        if self.head.next == None:
            self.head.next = da
            return
        da.next = self.head.next
        self.head.next = da

    def insert(self,data,index):
        daN = self.head.next
        da = Data(data)
        i = 0
        while daN:
            if i == index:
                da.next = daN.next
                daN.next = da
            daN = daN.next
            i += 1
        print "超出范围"

    def deleI(self,index):
        daN = self.head.next
        i = 0
        while daN:
            if i == index-1:
                daN1 = daN.next
                daN.next = daN1.next
                return daN1.data
            daN = daN.next
            i += 1

    def dele(self,data):
        daN = self.head.next
        while daN:
            if daN.next.data == data:
                daN1 = daN.next
                daN.next = daN1.next
                return daN1.data
            daN = daN.next
            i += 1

    def quest(self,index):
        daN = self.head.next
        i = 0
        while daN:
            if i == index:
                return daN.data
            daN = daN.next
            i += 1

