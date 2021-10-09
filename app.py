from flask import Flask, request, render_template, flash
from Models.sen_para import get_response
from Models.sum import _run_article_summary

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def home():
    # text = "We are creating an instance of the Flask class and calling it app. Here we are creating a new web application."
    # result = get_response(text, 5)
    return render_template('index.html')


@app.route("/service")
def services():
    return render_template('index2.html')


@app.route("/get_paraphrase", methods=['POST'])
def get_para():
    paraphrase = request.form['paraphrase']
    result = get_response(paraphrase, 5)

    for i in range(len(result)):
        para = result[i]

    return render_template('index2.html', out_put="{}".format(para))


@app.route("/get_summary", methods=['POST'])
def get_sum():
    article = request.form['article']
    result = _run_article_summary(article)

    return render_template('index2.html', summary="{}". format(result))


if __name__ == "__main__":
    app.run(debug=True)
