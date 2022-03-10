#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template,request

#Flaskオブジェクトの生成
app = Flask(__name__)


#「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/")



#「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/index")
def index():
    name = request.args.get("name")
    mazical = ["バナナと言ったら","黄色","黄色といったら","バナナ"]
    return render_template("index.html",name=name,mazical=mazical)


#以下を追加
@app.route("/index",methods=["post"])
def post():
    name = request.form["name"]
    mazical = ["バナナと言ったら","黄色","黄色といったら","バナナ"]
    return render_template("index.html", name=name, mazical=mazical)
#追加終わり

#おまじない
if __name__ == "__main__":
    app.run(debug=True)