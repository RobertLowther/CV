from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/experience")
def experience():
    return render_template("experience.html")


@app.route("/skills")
def skills():
    return render_template("skills.html")


@app.route("/education")
def education():
    return render_template("education.html")


@app.route("/qualifications")
def qualifications():
    return render_template("qualifications.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
