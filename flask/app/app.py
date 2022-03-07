# ルーティング操作

# Flask と render_template(HTMLを表示させるための関数)をインポート
from flask import Flask, render_template, request


# Flaskオブジェクトの生成
app = Flask(__name__)


# --書き方--
# @aaa.route("xxxxx")   xxxxx -> URL
# def zzzzz() :     xxxxにアクセスしたとき、zzzzz()を実行する
#       return yyyyyyyyy


# 「/」へアクセスがあった場合に、"Hello Wordl" の文字列を返す
@app.route("/")
def hello():
    return "Hello World"

# 「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/index")
def index():
    name = request.args.get("name")     # WebページのURLで、name=xxxxxと入力されたとき、xxxxxを取得する
    return render_template("index.html", name=name)     # index.htmlに、nameというデータをnameという変数のデータにして送る
#    return render_template("index.html")


# おまじない
if __name__ == "__main__" :
    app.run(debug=True)