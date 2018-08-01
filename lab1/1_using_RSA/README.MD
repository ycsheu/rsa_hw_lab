use python to encrypt P and decrypt




from Crypto.PublicKey import RSA

pubkey_filename = 'pub4096.pem'

f = open(public_filename,'r')

pubkey = RSA.importKey(f.read())

pubkey.e

pubkey.n

f.close()

f = open('P', 'rb')

P = f.read()

print(P)

P2 = int.from_bytes(bytearray(P), byteorder='little')

C = pow(P2, pubkey.e, pubkey.n)


f.close()

prikey_filename = 'pri4096.pem'

f = open(prikey_filename, 'r')

prikey = RSA.importKey(f.read

prikey.d

PI = pow(C, prikey.d, prikey.n)

print(PI==P2)

PS = PI.to_bytes(PI.bit_length() // 8 + 1, 'little')

print(PS.decode('ascii'))
