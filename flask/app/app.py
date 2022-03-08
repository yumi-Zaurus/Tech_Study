# ルーティング操作

# Flask と render_template(HTMLを表示させるための関数)をインポート
from flask import Flask, render_template, request


# Flaskオブジェクトの生成
app = Flask(__name__)




# 「/」へアクセスがあった場合に、"Hello Wordl" の文字列を返す
@app.route("/")
def hello():
    return "Hello World"

# 「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/index")
def index():
    name = request.args.get("name")
    okyo = ["色不異空", "空不異色", "色即是天","空即是色"]
    return render_template("index.html", name=name, okyo=okyo)
#    return render_template("index.html")


# おまじない
if __name__ == "__main__" :
    app.run(debug=True)