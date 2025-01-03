from flask import Flask
import os
import markdown

app = Flask(__name__)


@app.route("/")
def home():
    html = ""
    dct = "articles/"
    articles = []
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
    for f in os.listdir(dct):
        if os.path.isfile(os.path.join(dct, f)):
            articles.append(f"- [{f}]({f})")
    allarticles = markdown.markdown("\n".join(articles))

    return html.replace("<articles/>", allarticles)


@app.route("/<string:name>")
def txt(name):
    html = ""
    txt = ""
    with open("blog.html", "r", encoding="utf-8") as f:
        html = f.read()
    with open(os.path.join("articles/", name), "r", encoding="utf-8") as f:
        txt = f.readlines()
    oupt = [line.rstrip() + "<br>" for line in txt]
    # print(oupt)

    return (
        html.replace("<out2/>", "".join(oupt))
        .replace("<out1/>", name)
        .replace("<out3/>", name)
    )


@app.route("/about")
def about():
    html = ""
    with open("blog.html", "r", encoding="utf-8") as f:
        html = f.read()
    with open("about.txt", "r", encoding="utf-8") as f:
        txt = f.read()
    return (
        html.replace("<out2/>", txt)
        .replace("<out1/>", "關於")
        .replace("<out3/>", "關於")
    )


app.run(debug=True, host="0.0.0.0")
