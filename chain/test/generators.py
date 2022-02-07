from cryptos import Bitcoin,sha256


class Random:
    def __init__(self, priv=''):
        self.priv = priv

    
    
    def string_byte(self):
        c = Bitcoin(testnet=True)
        private_key = sha256(self.priv)
        public_key = c.privtopub(private_key)
        return public_key
