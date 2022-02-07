import requests
import json
from generators import Random
keys = Random()
headers = {
  'Accept': 'application/json',
  'X-API-KEY': '50doNxRp3EXohGsgyqsPDU0rVRTAwG'
}

# headers = json.dumps(headers)


def get_balance():
      r = requests.get('https://onchain.io/api/address/balance/TESTNET3/moCdE5TA9pZHrjSQC17Gsjkz7sGSL9diR6', params={}, headers = headers)
      print(r.json())


def get_address(private_key):
  headers = {
  "Accept": "application/json",
  "X-API-KEY": "50doNxRp3EXohGsgyqsPDU0rVRTAwG"
  }
  keys.priv = private_key
  pbk = str(keys.string_byte())
  param = {
    'coin_type':'BITCOIN',
    'public_key': pbk
  }
  r = requests.get('https://onchain.io/api/address/BITCOIN/'+pbk, params=param, headers = headers)
  a=r.json()
  print(a)


def create_tx(to='',amount=0,_from='',from_address='',miner_fee=''):
      body = {
                "coin_type": "BITCOIN",
                "recipients": [
                  {
                    "to": to,
                    "amount": amount
                  }
                ],
                "from": _from,
                "from_address": from_address,
                "miners_fee": miner_fee
              }
      r = requests.post('https://onchain.io/api/transaction/create/TESTNET3', params={}, headers = headers,data=body)

      return r.status_code

_from = '0421e3f67bade244bd6831da20880c59b12b348fde1c123ab5c76690387f96ee1ca89725fd851064471be624da994671b31693566a2de90cb5328b782b3b2877fd'

tx = create_tx(to='mpQjhrgwSyxkE2KGRUREM9cwY6YAnKM47s',amount=0.00028,_from=_from,from_address='moCdE5TA9pZHrjSQC17Gsjkz7sGSL9diR6',miner_fee=0.00011)      

print(tx)