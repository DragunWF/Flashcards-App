# Firebase Realtime Database

## Database Structure

```json
{
  "flashcards": {
    "code": {
      "topic": "Topic of the flashcard deck",
      "flashcard1": {
        "definition": "The description of the answer",
        "answer": "The term described by the definition"
      }
    }
  }
}
```

## Scripts related to manipulating the database

- `helpers/database_helper.py`: Deals with operating and manipulating the database.
- `helpers/database_keys.py`: Contains an enum with the keys of the database as its values.
- `scripts/reset_db`: Deletes all flashcard keys that are user-generated. This is primarily utilized for testing purposes.
- `scripts/add_test_data.py`: Inserts the default flashcard decks that gets loaded when a user views the website.
- `scripts/flashcard_test_decks.py`: Contains the data for default flashcard decks.
