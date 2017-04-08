'''
f = open('./testFile/test.txt', 'w')
f.write("\n I'm coming")
f.close()
'''
with open('./testFile/text.txt', 'w') as f:
    f.write("Hello world!")
