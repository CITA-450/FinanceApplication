# import Flask, render_template, request, jsonify
import flask


app = flask(__name__)


@app.route("/")
def index():
    return render_template("interest calculator.html", interest=interest, total=total)


@app.route("/calculate", methods=["POST"])
def calculate():
    principal = float(request.form["principal"])
    rate = float(request.form["rate"]) / 100
    time = float(request.form["time"])

    interest = principal * rate * time
    total = principal + interest

    return jsonify(interest=interest, total=total)


if __name__ == "__main__":
    app.run(debug=True)
