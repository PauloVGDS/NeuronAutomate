from flask import Flask, render_template, request, url_for, redirect
import modules as md


app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True)

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        tabela = request.form["worksheets"]
        creditos = request.form["creditsInput"]
        rede = "BLIPS" if request.form["network"] == "" else request.form["network"]
        senha = "Blips1521" if request.form["password"] == "" else request.form["password"]

        if md.completeTest(rede, senha, tabela, creditos):
            return redirect(url_for("taskdone"))
            
        return redirect(url_for("complete"))
        
    worksheets = md.getWorksheets()
    return render_template("complete.html", worksheets=worksheets)
    
    

@app.route("/taskdone", methods=("GET", "POST"))
def taskdone():
    return render_template("taskdone.html")

