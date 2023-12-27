from flask import Flask, render_template, request
from python_scripts import count_words

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

@app.route("/Programs")
def programs_page():
    return render_template("Python_Programs/programs.html")

@app.route("/Python_Programs/Word_Counter", methods=['GET', 'POST'])
def word_counter_page():
    if request.method == 'GET':
        return render_template("Python_Programs/Word_Counter/word_counter.html")
    elif request.method == 'POST':
        words = request.form["words"]     
        count = str(count_words.word_count(words))
        return render_template("Python_Programs/Word_Counter/word_counter.html", count=count) 



if __name__ == "__main__":
    app.run(debug=True)