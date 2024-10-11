# Flashcards-App

I got bored...

## Description

This Flashcards Web App is a simple and intuitive platform for creating, managing, and reviewing flashcards, designed to help users efficiently study and retain information. The app offers real-time interaction and a seamless user experience across multiple devices, making it ideal for learners who want to create their own flashcards or browse existing ones.

**Note:** This is still in development!

## Attributions

- [Flashcard Favicon](https://www.flaticon.com/free-icon/flash-card_6587388)

---

# Requirements

## Functional Requirements

1. **User Interface**
   - The app must have an intuitive and user-friendly interface where users can view and interact with flashcards.
2. **Display Flashcards**
   - The system must display existing flashcards (questions and answers).
   - Each flashcard should initially show only the question, and upon interaction (e.g., a click), it should reveal the answer.
3. **Add New Flashcards**
   - Users must be able to create new flashcards by providing a question and an answer through a form.
   - The system must save these flashcards and make them available immediately for review.
4. **Save Flashcards**
   - Flashcards created by users should be saved via a Firebase.
   - The system must persist user-created flashcards between sessions.
5. **Delete Flashcards**
   - Users should be able to delete a flashcard if they no longer need it.
6. **Edit Flashcards**
   - Users should be able to edit existing flashcards to change the question or answer.
7. **Navigation**
   - The app should allow users to easily navigate through different flashcards (e.g., “Next” and “Previous” buttons for browsing flashcards).

## Non-Functional Requirements

### Operational Requirements

- The app should be simple and intuitive to use, requiring minimal explanation or instruction.
- The interface should be clean, responsive, and accessible on both desktop and mobile devices.
- Flashcards must persist across user sessions. This can be achieved by saving data via Firebase.
- The app should work consistently across major browsers (e.g., Chrome, Firefox, Safari).
- The app should adapt to different screen sizes and devices (mobile, tablet, desktop) for a responsive user experience.

### Performance Requirements

- The app should load flashcards quickly, both from the initial set and user-created ones.
- It should respond in real-time when users interact with flashcards (e.g., clicking to reveal the answer).
- The app must be able to handle a growing number of flashcards without performance degradation, especially if stored on the server.
- The app should function consistently without crashing or losing user data.
- Data (flashcards) must be saved reliably and should not be lost unexpectedly.

### Security Requirements

- Storing flashcards on the server or supporting user accounts, the system should ensure data security and prevent unauthorized access or tampering with flashcards.
- User input (e.g., new flashcards) should be sanitized to avoid security issues like cross-site scripting (XSS).

### Cultural Requirements

- English language support

## Firebase Realtime Database Structure

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
