from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient, DESCENDING

client = MongoClient('mongodb://test:test@13.125.177.83', 27017)
db = client.dbsparta

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/list', methods=['GET'])
def movie_star_list():
    mystar = list(
        db.mystar.find({},{'_id':0}).sort([("like", DESCENDING)])
    ) #{'_id',0} : 해당값은 가져올 필요가 없어서 안가져온다는 의미로 쓰임 / DECENDING : 내림차순
    return jsonify(mystar)

@app.route('/api/like', methods=['POST'])
def movie_star_like():
    name_receive = request.form['name_give']
    moviestar = db.mystar.find_one({'name':name_receive})
    moviestar_like = moviestar['like']

    db.mystar.update_one(
        {'name':name_receive}, 
        {'$set':{'like':moviestar_like + 1}}
    )

    return jsonify({'success':True})

@app.route('/api/delete', methods=['POST'])
def movie_star_delete():
    name_receive = request.form['name_give']

    db.mystar.delete_one(
        {'name':name_receive}
    )

    return jsonify({'success':True})

if __name__ == __name__:
    app.run('0.0.0.0', port=5000, debug=True)