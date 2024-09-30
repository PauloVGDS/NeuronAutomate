from flask import Flask, render_template, request, redirect



app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True)

# The server can be initialized with 'Flask.run()'.
# Debug mode can be activated with 'debug=True'.
# Apparently we can use 'port' to specify the port of the server

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
