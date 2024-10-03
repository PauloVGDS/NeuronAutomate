from flask import Flask, render_template, request, redirect



app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form", methods=("GET", "POST"))
def form():
    nome = request.form["rede"]
    return f"<h1 id='title'>Hello {nome}</h1>"

@app.route("/after")
def after():
    return f"After form"
