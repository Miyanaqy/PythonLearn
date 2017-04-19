def h():
    print('start')
    d = yield 5
    print(d)
    m = yield 6
    print(m)
    yield 7

c = h()
t = c.send(None)
print(t)
print('----------------------')

t = c.send('Lux')
print(t)
print('----------------------')

t = c.send('ACE')
print(t)
