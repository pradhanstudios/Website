from flask import Flask, render_template, request, url_for
from python_scripts import count_words, a_star
import json

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
    # print(request.args.getlist)
    if (arr := request.args.get("arr")) and (start := request.args.get("start")) and (end := request.args.get("end")) and (size := request.args.get("size")):
        arr = json.loads(arr)
        size = int(size)
        blockers = []
        start = tuple(map(lambda x: int(x), tuple(start.split(','))))
        end = tuple(map(lambda x: int(x), tuple(end.split(','))))
        # print(start, type(start), end, type(end))
        # print(arr)
        # for some reason the json stringify gets rid of all of the zeros after the last number and it makes zeroes null ????
        for i in range(size):
            N = len(arr[i])
            for j in range(N):
                if arr[i][j] == None:
                    arr[i][j] = 0
                elif arr[i][j] == 9:
                    blockers.append({"x": i, "y": j})
            arr[i] += [0] * (size - N)
        path, moves = a_star.use_a_star(arr, start, end)
        # path = 0
        # print(path)
        if path != "No Solution":
            path = [{"x": coord[0], "y": coord[1]} for coord in path]
        # print(path)
            
            return render_template("Python_Programs/Pathfinding/Show/show.html", blockers=blockers, path=path)
        else:
            return render_template("Python_Programs/Pathfinding/Show/show.html", blockers=blockers, error="No Solution")
    return render_template("Python_Programs/Pathfinding/pathfinding.html")

if __name__ == "__main__":

    app.run(debug=True)