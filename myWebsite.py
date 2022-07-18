from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "dec@2021"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/portfolio", methods=['GET', 'POST'])
def portfolio():
    return render_template("portfolio.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=True)
