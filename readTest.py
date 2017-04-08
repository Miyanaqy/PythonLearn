'''
try:
    f = open('./testFile/test.txt', 'r')
    print(f.read())
except IOError as e:
    print("文件不存在")
finally:
    if f:
        f.close()
'''
with open('./testFile/test.txt', 'r') as f:
    print(f.read())
