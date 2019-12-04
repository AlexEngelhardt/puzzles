import hashlib

hashlib.md5('abc'.encode('utf-8')).hexdigest()

# salt = 'abcdef'
salt = 'yzbqklnj'
add = 1

check = salt + str(add)

while hashlib.md5((salt + str(add)).encode('utf-8')).hexdigest()[:5] != '00000':
    add += 1
    if add > 10_000_000:
        print('Timeout :D')
        break

print(add)

