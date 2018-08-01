use python3 to encrypt P and decrypt



```python
from Crypto.PublicKey import RSA
pubkey_filename = 'pub4096.pem'
f = open(pubkey_filename,'r')
# read publickey
pubkey = RSA.importKey(f.read())
pubkey.e
pubkey.n
f.close()
# read file P
f = open('P', 'rb')
P = f.read()
print(P)
# convert to biginteger
P2 = int.from_bytes(bytearray(P), byteorder='little')
# do encryption
C = pow(P2, pubkey.e, pubkey.n)
f.close()

# decryption
# read privatekey
prikey_filename = 'pri4096.pem'
f = open(prikey_filename, 'r')
prikey = RSA.importKey(f.read())
prikey.d
# do decryption
# P = C^d mod n
PI = pow(C, prikey.d, prikey.n)
# check whether the biginteger is the same
print(PI==P2)
# convert to bytes
# // means the result is integer only
# 7 // 5 = 1
# 7 /  5 = 1.4
PS = PI.to_bytes(PI.bit_length() // 8 + 1, 'little')
# bytes to string
print(PS.decode('ascii'))
```
