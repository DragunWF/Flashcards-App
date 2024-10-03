from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route("/flashcard-editor", methods=["GET", "POST"])
def flashcard_editor():
    if request.method == "POST":
        pass
    return render_template('flashcard_editor.html')


if __name__ == "__main__":
    app.run(debug=True)
