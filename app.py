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

@app.route('/yjpost/delete', methods=['POST'])
def delete_review():
    name_receive = request.form['name_give']
    db.yjpost.delete_one({'name': name_receive})
    return jsonify({'msg': '삭제 완료!'})


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

@app.route('/wjpost/delete', methods=['POST'])
def wj_delete_review():
    name_receive = request.form['name_give']
    db.woojung.delete_one({'name': name_receive})
    return jsonify({'msg': '삭제 완료!'})

# <----- 유성재 방명록 ----->

@app.route("/sjpost", methods=["POST"])
def seongjae_post():
    name_receive = request.form['name_give']
    review_receive = request.form['review_give']

    doc = {
        'name': name_receive,
        'review': review_receive
    }
    db.seongjae.insert_one(doc)
    return jsonify({'msg': '방명록 작성 완료'})

@app.route("/sjpost", methods=["GET"])
def seongjae_get():
    review_list = list(db.seongjae.find({},{'_id':False}))
    return jsonify({'reviews': review_list})

@app.route('/sjpost/delete', methods=['POST'])
def sj_delete_review():
    name_receive = request.form['name_give']
    db.seongjae.delete_one({'name': name_receive})
    return jsonify({'msg': '삭제 완료!'})

# <----- 이지섭 방명록 ----->
@app.route("/jspost", methods=["POST"])
def jisub_post():
    name_receive = request.form['name_give']
    review_receive = request.form['review_give']

    doc = {
        'name': name_receive,
        'review': review_receive
    }
    db.jisub.insert_one(doc)
    return jsonify({'msg': '방명록 작성 완료'})

@app.route("/jspost", methods=["GET"])
def jisub_get():
    review_list = list(db.jisub.find({},{'_id':False}))
    return jsonify({'reviews': review_list})

@app.route('/jspost/delete', methods=['POST'])
def js_delete_review():
    name_receive = request.form['name_give']
    db.jisub.delete_one({'name': name_receive})
    return jsonify({'msg': '삭제 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
