# from datetime import datetime

from flask import Flask, render_template, json

app = Flask(__name__)


@app.route('/')
def base():
    return render_template('base.html')


"""
    files_json - использую в место списка соварей (импровезированная БД)
"""


@app.route('/clothes/')
def clothes():
    with open('files_json/clothes.json', encoding='UTF-8') as f:
        clothes_list = json.load(f)
    return render_template('clothes.html', clothes_list=clothes_list)


@app.route('/jackets/')
def jackets():
    with open('files_json/jackets.json', encoding='UTF-8') as f:
        jacket_list = json.load(f)
    return render_template('jackets.html', jacket_list=jacket_list)


@app.route('/shoes/')
def shoes():
    with open('files_json/shoes.json', encoding='UTF-8') as f:
        shoes_list = json.load(f)
    return render_template('shoes.html', shoes_list=shoes_list)


if __name__ == '__main__':
    app.run(debug=True)
