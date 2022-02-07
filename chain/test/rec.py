from cryptos import *

c = Bitcoin(testnet=True)

private_key = sha256('ola')
print('password: '+ private_key)

public_key = c.privtopub(private_key)

# print('public key: '+ public_key)

address = c.pubtoaddr(public_key)
print(address)

inputs = c.unspent(address)
print(inputs)

# outs = [{'value': 269845600, 'address': '2N8hwP1WmJrFF5QWABn38y63uYLhnJYJYTF'}, {'value': 100000, 'address': '3EfLcbaUkHPkD1in73tg7aBXxXVm4xKCm5'}]

# tx = c.mktx(inputs,outs)
# print('tx :'+str(tx))

#sign the transaction with private key

# tx2 = c.sign(tx,0,private_key)

# tx3 = c.sign(tx2,1,private_key)

# print(tx3)

# tx4 = c.serialize(tx)

# print(tx4)

# tf=c.pushtx(tx4)

# print(tf)




