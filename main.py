from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return "Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести"


@app.route('/promotion')
def promotion():
    return render_template("promotion.html")


@app.route('/image_mars')
def mars_img():
    return render_template("mars_img.html")


@app.route('/promotion_image')
def promotion_image():
    return render_template("моя маленькая американская бейба.html")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
