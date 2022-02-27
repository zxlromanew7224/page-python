from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    #numero = [1,2,3,4,5 ]
    #return render_template("lista.html", num = numero)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
