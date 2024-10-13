import logging
from flask import Flask, render_template, request

from helpers.database_helper import DatabaseHelper
from helpers.flashcard import Flashcard

app = Flask(__name__)


class WebApp:
    @app.route('/', methods=["GET"])
    def index():
        logging.info(f"A user is entering {request.url}")

        # Selects the flashcard deck to be displayed in the page
        flashcard_code = request.args.get("code")
        DEFAULT_CODE = "TEST101"
        is_invalid_code = False
        flashcards = DatabaseHelper.get_flashcards(flashcard_code)
        if flashcards is None:
            # Default Flashcard Deck
            flashcards = DatabaseHelper.get_flashcards(DEFAULT_CODE)
            if not flashcard_code is None:
                is_invalid_code = True

        return render_template("index.jinja", flashcard_topic=flashcards[0],
                               flashcards=flashcards[1], len=len, is_invalid_code=is_invalid_code,
                               flashcard_code=flashcard_code if flashcard_code else DEFAULT_CODE)

    @app.route("/flashcard-editor", methods=["GET", "POST"])
    def flashcard_editor():
        logging.info(f"A user is sending a {request.method} to {request.url}")
        is_new_deck_created = False

        # POST request functionality (For saving decks)
        if request.method == "POST":
            is_new_deck_created = True
            flashcard_count = 1
            flashcards: list[Flashcard] = []
            generated_code = None

            # Parses the data in order to transfer it to the database
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
            return render_template("flashcard_editor.jinja", generated_code=generated_code,
                                   is_new_deck_created=is_new_deck_created, len=len)

        # GET request functionality
        FLASHCARD_CODE = request.args.get("code")
        flashcard_deck = None
        if FLASHCARD_CODE:
            flashcard_deck = DatabaseHelper.get_flashcards(FLASHCARD_CODE)
        flashcards = flashcard_deck[1] if flashcard_deck else []
        deck_title = flashcard_deck[0] if flashcard_deck else ""

        return render_template("flashcard_editor.jinja",
                               is_new_deck_created=is_new_deck_created, len=len,
                               deck_title=deck_title, flashcards=flashcards,
                               is_invalid_code=not flashcard_deck and FLASHCARD_CODE,
                               flashcard_code=FLASHCARD_CODE)

    @app.errorhandler(Exception)
    def handle_error(error):
        return render_template("apology.jinja", status_code=error.code), error.code

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
