from flask import Flask, render_template, request, url_for
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

@app.route("/Programs/Word_Counter", methods=['GET', 'POST'])
def word_counter_page():
    if request.method == 'GET':
        return render_template("Python_Programs/Word_Counter/word_counter.html")
    elif request.method == 'POST':
        words = request.form["words"]     
        count = count_words.word_count(words)
        count = {k: v for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True)}
        count = [{"word": word, "num": num} for word, num in count.items()]
        # word_ul = '''
        # <ul class="word">
        #     <h1 class="words_word">{}</h1>
        #     <h1 class="word_count">{}</h1>
        # </ul>
        # '''

        # formatted = ""
        # for word, num in count.items():
        #     formatted += word_ul.format(word, num)

        return render_template("Python_Programs/Word_Counter/word_counter.html", count=count) 

@app.route("/Programs/Pathfinding")
def pathfinding_page():
    if (arr := request.args.get("arr")) and (start := request.args.get("start")) and (end := request.args.get("end")):
        return f'''{arr} | {start} | {end}'''
    return render_template("Python_Programs/Pathfinding/pathfinding.html")

if __name__ == "__main__":
    app.run(debug=True)