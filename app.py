from flask import Flask, render_template, request
from time import sleep
from modules import *


app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def index():
    worksheets = ["CNC 4040", "CNC 6040", "CNC 1060", "Flatbed"]
    return render_template("index.html",worksheets=worksheets)

@app.route("/form", methods=("GET", "POST"))
def form():
    tabela = request.form["worksheets"]
    creditos = request.form["creditsInput"]
    rede = request.form["network"]
    senha = request.form["password"]
    
    #completeTest(rede, senha, tabela, creditos)
    return f"<h1 id='title'>{tabela}, {creditos}, {rede}, {senha}</h1>"

