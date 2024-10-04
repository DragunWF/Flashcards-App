import logging
from flask import Flask, render_template, request

from helpers.database_helper import DatabaseHelper
from helpers.flashcard import Flashcard

app = Flask(__name__)


class WebApp:
    @app.route('/', methods=["GET"])
    def index():
        logging.info(f"A user is entering {request.url}")
        FLASHCARD_CODE = request.args.get("code")
        flashcards = DatabaseHelper.get_flashcards(FLASHCARD_CODE)
        if flashcards is None:
            flashcards = DatabaseHelper.get_flashcards("TEST101")  # Default
        return render_template("index.html", flashcard_topic=flashcards[0],
                               flashcards=flashcards[1], len=len)

    @app.route("/flashcard-editor", methods=["GET", "POST"])
    def flashcard_editor():
        logging.info(f"A user is sending a {request.method} to {request.url}")
        if request.method == "POST":
            flashcard_count = 1
            flashcards: list[Flashcard] = []
            generated_code = None
            while True:
                definition = request.form.get(f"definition{flashcard_count}")
                answer = request.form.get(f"answer{flashcard_count}")
                if definition is None or answer is None:
                    break
                flashcards.append(Flashcard(answer, definition))
                flashcard_count += 1
                generated_code = DatabaseHelper.create_flashcard_deck(
                    request.form.get("topic"), flashcards
                )
            return render_template("flashcard_editor.html", generated_code=generated_code)
        return render_template("flashcard_editor.html")

    @staticmethod
    def start():
        # Logging Configuration
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s]: %(message)s",
            datefmt="%b-%d-%Y %I:%M %p",  # %I for 12-hour format and %p for AM/PM
        )

        # Run the application
        DatabaseHelper.start_database()
        app.run(debug=True)


if __name__ == "__main__":
    WebApp.start()
