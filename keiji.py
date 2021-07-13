from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hel():
    return render_template('keiji.html')

@app.route('/syuninsya')
def hell():
    syuninsya=(["地山の掘削","土止め支保工","型枠支保工の組立","足場の組立等","建築物等の鉄骨の組立等","コンクリート造の工作物の解体等","酸素欠乏危険","有機溶剤","特定化学物質等"])
    return render_template('syuninsya.html',syuninsya=syuninsya,ssyuninsya=ssyuninsya)

@app.route('/tokubetsu')
def helloo():
    tokubetsu=(["玉掛け","フォークリフトの運転","アーク溶接等"])
    return render_template('tokubetsu.html',tokubetsu=tokubetsu)

if __name__ == "__main__":
    app.run(debug=True)