from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/flashcard-editor")
def flashcard_editor():
    return render_template('flashcard_editor.html')


if __name__ == '__main__':
    app.run(debug=True)
