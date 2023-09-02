from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("routes/index.html")


if __name__ == "__main__":
    app.run(debug=True, port=4242)
