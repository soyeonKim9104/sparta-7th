from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost',27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/order')
def order_get():
    orders = list(db.orders.find({}, {"_id":0}))
    return jsonify({
        "orders" : orders
    })

@app.route('/order', methods=["POST"])
def order_post():
    name = request.form.get('name', '')
    amount = request.form.get('amount', '')
    address = request.form.get('address', '')
    phone = request.form.get('phone', '')

    db.orders.insert_one({
        "name": name,
        "amount": amount,
        "address": address,
        "phone": phone
    })

    print(name,amount,address,phone)
    return jsonify({"success":"ok"})

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, debug=True)