from flask import Flask, render_template, request
from calculator import calculate

app = Flask(__name__)

@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    expression = ""
    result = ""

    if request.method == "POST":
        expression = request.form["expression"]
        button = request.form["button"]

        if button == "C":
            expression = ""

        elif button == "back":
            expression = expression[:-1]

        elif button == "=":
            result = calculate(expression)
            expression = str(result)

        else:
            expression += button

    return render_template(
        "index.html",
        expression=expression,
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)
