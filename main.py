from flask import Flask, render_template, request

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


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return render_template("вова сказал, что АЮ не позер и за все шарит. ауф.html")
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

