from flask import  Flask, render_template, url_for




app = Flask(__name__)

menu = ["Установка","Первое приложение","Обратная связь"]


@app.route("/")
def index():
    print(url_for('index'))
    return render_template('index.html',title ='Про Flask',menu=menu)


@app.route("/about")
def about():
    return render_template('index.html',title ='Про Flask',menu=menu)


@app.route("/profile/<path:username>/<path>")
def profile(username,path):
    return  f"Пользователь : {username},{path}"



# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('about'))
#     print(url_for('profile',username="abc",path='her'))
# #
if __name__=="__main__":
    app.run(debug=True)