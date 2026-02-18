from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    return render_template("index.html", year=current_year)



@app.route('/guess/<name>')
def info(name):
    gender_endpoint = f"https://api.genderize.io?name={name}"
    response_gender = requests.get(url=gender_endpoint)
    gender_data = response_gender.json()
    gender = gender_data["gender"]

    age_endpoint = f"https://api.agify.io?name={name}"
    response_age = requests.get(url=age_endpoint)
    age_data = response_age.json()
    age = age_data["age"]
    return render_template("guess.html", name=name, age=age, gender=gender)

@app.route('/blog')
def blog():
    pass


if __name__ == "__main__":
    app.run(debug=True)
