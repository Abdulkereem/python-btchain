from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from chain.bitcoin import Bitcoin

import sqlite3
sqlite3.connect('tmp/base.db')

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/base.db'
app.config['SECRET_KEY']='dfjfdkjfdkjfdk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Misaka(app)

db = SQLAlchemy(app)

btc = Bitcoin()






class Wallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(255))
    password = db.Column(db.String(255))
    email = db.Column(db.String(255))
    identifier = db.Column(db.String(255))
    address = db.Column(db.String(255))
    label = db.Column(db.String(255))

class Btc_Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(255))
    amount = db.Column(db.String(255))
    sender = db.Column(db.String(255))
    reciever = db.Column(db.String(255))
    date = db.Column(db.String(255))
    tx_hash = db.Column(db.String(255))

    




@app.route('/api/wallet',methods=['GET','POST'])
def index():
    if request.method == 'POST':
          
        data = request.json
        btc.password = data['password']
        btc.label = data['label']
        info=btc.make_wallet()
        new_wallet = Wallet(password=data['password'],
                            email=data['email'],
                            identifier=info['identifier'],
                            address=info['address'],
                            label=data['label'])
        db.session.add(new_wallet)
        db.session.commit()
        return jsonify({'status':'200'})

    return jsonify({'status':'get request'})

@app.route('/api/btc/balance',methods=['GET','POST'])
def check_balance():
    if request.method == 'POST':
        data = request.json
        user = Wallet.query.filter_by(user=data['user']).first()
        btc.identifier = user.identifier
        btc.password = user.password
        print(btc.check_balance())
        return jsonify({'msg':btc.check_balance()})

@app.route('/api/btc/transfer',methods=['POST'])
def make_transfer():
    data = request.json
    user = Wallet.query.filter_by(user=data['user']).first()
    btc.identifier = user.identifier
    btc.password = user.password
    btc.sender = user.address
    btc.reciever = data['address']
    btc.amount = data['amount']
    payment=btc.transfer()
    print(payment)
    # new_transaction = Btc_Transaction(user=user.id,
    #                         amount=data['amount'],tx_hash=payment['tx_hash'])
    # db.session.add(new_transaction)
    # db.session.commit()
    return jsonify({'msg':payment['success'],'status':'200'})







@app.route('/database')
def mig():
    db.create_all()
    return jsonify({'msg':'done'})   

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)
 