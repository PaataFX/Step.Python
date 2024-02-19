from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/starting")
def starting():
    return render_template("starting.html")

@app.route("/cc")
def cc():
    return render_template("CC.html")


if __name__ == "__main__":
    app.run(debug=True)