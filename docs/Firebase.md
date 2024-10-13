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
