from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def films():
    return render_template("index.html", link="Перейти в кинотеатр")

@app.route("/person/")
def person():
    return render_template("main.html", link="Перейти в кинотеатр")

@app.route("/home/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
