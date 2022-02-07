from blockchain import blockexplorer, exceptions, exchangerates, createwallet
from blockchain.wallet import Wallet
from chain.config import SERVICE_URL, API_KEY
from requests import post, get
import json
from fake_useragent import UserAgent

class Bitcoin:

    sender = ''
    reciever = ''
    amount = ''
    
    def __init__(self, hash='', block ='', currency='', convalue='',password='',label='',identifier=''):
        self.hash = hash
        self.block = block
        self.currency = currency
        self.convalue = convalue
        self.password = password
        self.label = label
        self.identifier = identifier

    def get_block(self):
        try:
            block = blockexplorer.get_block(self.block)
            return block.__dict__
        except exceptions.APIException:
            return 'block not found'
    
    def get_tx(self):
        tx_id =blockexplorer.get_tx(self.hash)
        return tx_id.__dict__
    
    def btc_rate(self):
        ticker = exchangerates.get_ticker()
        for k in ticker:
            return k, ticker[k].p15min
    def currency_converter(self):
        ccy = self.currency.upper()
        val = self.convalue
        btc = exchangerates.to_btc(ccy, val)
        return btc.__dict__

    def make_wallet(self):
        wallet = createwallet.create_wallet(self.password, '58ck39ajuiw', SERVICE_URL, label = self.label)

        return wallet.__dict__

    def check_balance(self):
        purse = Wallet(self.identifier,self.password,SERVICE_URL)
        response = purse.get_balance()
        return response

    def transfer(self):
        ua = UserAgent()

        h = {
            "Origin":"http://localhost:8000",
            "Host":"http://localhost:8000"",
            "Access-Control-Allow-Headers":"*",
            "content-Type":"application/json",
            "Access-Control-Allow-Origin":"*",
            "Access-Control-Allow-Methods":"POST",
            "User-Agent":ua.random
        }
        print(h)
        body = {
            "to":Bitcoin.reciever,
            "amount":Bitcoin.amount,
            "password":self.password,
            "from":Bitcoin.sender,
            "fee_per_byte":"0.000014",
            "api_code":"58ck39ajuiw"
        }
        response = post(SERVICE_URL+'merchant/'+self.identifier+'/payment',data=json.dumps(body), headers=h)

        return response.text

        # wallet = Wallet(self.identifier, self.password, SERVICE_URL)
        # payment = wallet.send(Bitcoin.reciever,Bitcoin.amount,Bitcoin.sender)
        # return payment.__dict__










# btc=Bitcoin()
# btc.currency='eur'
# btc.convalue=100
# x=btc.make_wallet()
# print(x['identifier'])