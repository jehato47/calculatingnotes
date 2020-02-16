from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":

        lecture = request.form.get("lecture")

        if lecture == "Seç":
            return render_template("index.html")

        elif lecture == "Cpp":
            return redirect(url_for("cpp"))

        elif lecture == "Calculus":
            return redirect(url_for("calc"))

    else:
        return render_template("index.html", notes={})


@app.route('/calc', methods=["GET", "POST"])
def calc():
    if request.method == "POST":
        first_exam = request.form.get("first")
        second_exam = request.form.get("second")
        av = (int(first_exam) * 2/5) + (int(second_exam) * 3 / 5)

        if 90 <= av <= 100:
            letter = "AA"

        elif 80 <= av < 90:
            letter = "BA"

        elif 70 <= av < 80:
            letter = "BB"

        elif 60 <= av < 70:
            letter = "CB"

        else:
            letter = "FF"
        notes = {
            "firstNote": first_exam,
            "secondNote": second_exam,
            "average": round(av, 2),
            "letter": letter
        }
        return render_template("calc.html", notes=notes)
    return render_template("calc.html", notes={})


@app.route('/cpp', methods=["POST", "GET"])
def cpp():
    if request.method == "POST":
        first_exam = request.form.get("first")
        second_exam = request.form.get("second")
        lab = request.form.get("lab")
        av = (int(first_exam) * 15/100) + (int(second_exam) * 3/5) + (int(lab) * 1/4)

        if 90 <= av <= 100:
            letter = "AA"

        elif 80 <= av < 90:
            letter = "BA"

        elif 70 <= av < 80:
            letter = "BB"

        elif 60 <= av < 70:
            letter = "CB"

        else:
            letter = "FF"

        notes = {
            "first": first_exam,
            "second": second_exam,
            "average": round(av, 2),
            "letter": letter
        }
        return render_template("cpp.html", notes=notes)
    else:
        return render_template("cpp.html", notes={})


if __name__ == '__main__':
    app.run(debug=True)
