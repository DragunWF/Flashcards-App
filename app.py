import logging
from flask import Flask, render_template, request

from utils.database_helper import DatabaseHelper

app = Flask(__name__)


class WebApp:
    @app.route('/', methods=["GET"])
    def index():
        return render_template('index.html')

    @app.route("/flashcard-editor", methods=["GET", "POST"])
    def flashcard_editor():
        if request.method == "POST":
            pass
        return render_template('flashcard_editor.html')

    @staticmethod
    def start():
        # Logging Configuration
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(levelname)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # Run the application
        DatabaseHelper.start_database()
        app.run(debug=True)


if __name__ == "__main__":
    WebApp.start()
