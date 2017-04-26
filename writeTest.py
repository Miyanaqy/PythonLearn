'''
f = open('./testFile/test.txt', 'w')
f.write("\n I'm coming")
f.close()
'''
import os
dir = 'testFile/2'
if not os.path.exists(dir):
        os.makedirs(dir)
with open('./testFile/text.txt', 'w') as f:
    f.write("Hello world!")
