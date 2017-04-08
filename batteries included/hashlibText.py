import hashlib

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    print(md5.hexdigest())
    print(db[user] == md5.hexdigest())

login('michael', '123456')

def loading():
    md5 = hashlib.md5()
    md5.update('michael'.encode('utf-8'))
    db['michael'] += md5.hexdigest()
    md5.update('bob'.encode('utf-8'))
    db['bob'] += md5.hexdigest()
    md5.update('alice'.encode('utf-8'))
    db['alice'] += md5.hexdigest()
    for i in db:
        print(db[i])
        

loading()
def loginX(user,password):
    md5 = hashlib.md5()
    md5.update(user.encode('utf-8'))
    md6 = hashlib.md5()
    md6.update(password.encode('utf-8'))
    print(db[user] == md6.hexdigest() + md5.hexdigest())

loginX('michael', '123456')
