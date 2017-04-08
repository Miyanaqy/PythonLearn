class people(object):
    def __init__(self,name):
        self.name = name
    def run(self):
        print("hello %s" % self.name)

class girl(people):
    pass

marry = girl("Marry")

marry.run()
