from cryptos import *

c = Bitcoin(testnet=True)

private_key = sha256('abdul')
print('password: '+ private_key)

public_key = c.privtopub(private_key)

print('public key: '+ public_key)

address = c.pubtoaddr(public_key)
print(address)

# inputs = c.unspent(address)
# print(inputs)

# outs = [{'value': 0.00028, 'address': 'mpQjhrgwSyxkE2KGRUREM9cwY6YAnKM47s'}]

# tx = c.mktx(inputs,outs)
# print('tx :'+str(tx))

# sign the transaction with private key

# tx2 = c.sign(tx,-0,private_key)

# tx3 = c.sign(tx2,-1,private_key)

# print(tx3)

# tx4 = c.serialize(tx)

# print(tx4)

# tf=c.pushtx(tx4)

# print(tf)




