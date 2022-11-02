from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.5hwkona.mongodb.net/Cluster0?retryWrites=true&w=majority',
                     tlsCAFile=ca)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/yeojune')
def getyeojune():
    return render_template('yeojune.html')


@app.route('/woojung')
def getwoojung():
    return render_template('woojung.html')

@app.route('/seongjae')
def getseongjae():
    return render_template('seongjae.html')

@app.route('/jisub')
def getjisub():
    return render_template('jisub.html')

# <----- 윤여준 방명록----->
@app.route("/yjpost", methods=["POST"])
def yeojune_post():
    name_receive = request.form["name_give"]
    review_receive = request.form['review_give']

    doc = {
        'name': name_receive,
        'review': review_receive
    }

    db.yjpost.insert_one(doc)
    return jsonify({'msg': '방명록 작성 완료!'})


@app.route("/yjpost", methods=["GET"])
def yeojune_get():
    review_list = list(db.yjpost.find({}, {'_id': False}))
    return jsonify({'reviews': review_list})


# <----- 양우정 방명록 ----->

@app.route("/wjpost", methods=["POST"])
def woojung_post():
    name_receive = request.form['name_give']
    review_receive = request.form['review_give']

    doc = {
        'name': name_receive,
        'review': review_receive
    }

    db.woojung.insert_one(doc)

    return jsonify({'msg': '방명록 작성 완료!'})


@app.route("/wjpost", methods=["GET"])
def woojung_get():
    review_list = list(db.woojung.find({}, {'_id': False}))
    return jsonify({'reviews': review_list})

# <----- 유성재 방명록 ----->

@app.route("/sjpost", methods=["POST"])
def seongjae_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }
    db.seongjae.insert_one(doc)
    return jsonify({'msg': '방명록 작성 완료'})

@app.route("/sjpost", methods=["GET"])
def seongjae_get():
    cheer_up_list = list(db.seongjae.find({},{'_id':False}))
    return jsonify({'cheer_up': cheer_up_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=1000, debug=True)
