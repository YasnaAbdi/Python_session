from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    name = request.form['name']
    password = request.form['pass']
    return f"<h1>{name}</h1> is your name, <h1>{password}</h1> is your password"


if __name__ == "__main__":
    app.run(debug=True)
