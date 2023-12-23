from flask import Flask, render_template, Blueprint

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Home/index.html")

@app.route("/Ritik")
def ritik_about():
    return render_template("Ritik/about.html")

@app.route("/Samik")
def samik_about():
    return render_template("Samik/about.html")

if __name__ == "__main__":
    app.run(debug=True)