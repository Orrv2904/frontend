from flask import Flask, render_template
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

@app.route("/")
def index():
    return render_template("index.html")

text = [
    "Hamlet Aburto Sánchez",
    "Jerath Sánchez",
    "R2D2 Rodriguez"
]


@app.route("/first")
def first():
    return text[0]


@app.route("/second")
def second():
    return text[1]


@app.route("/third")
def third():
    return text[2]