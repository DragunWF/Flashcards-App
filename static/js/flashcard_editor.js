document.addEventListener("DOMContentLoaded", function () {
  const flashcardContainer = document.getElementById("flashcardContainer");
  const addFlashcardBtn = document.getElementById("addFlashcardBtn");

  let flashcardCount = 1; // Start with 1 flashcard

  // Add new flashcard when button is clicked
  addFlashcardBtn.addEventListener("click", () => {
    addFlashcard();
  });

  // Load, Save, Go Back event listeners can be added here
  document.getElementById("loadDeckBtn").addEventListener("click", () => {
    // TODO
  });

  document.getElementById("saveDeckBtn").addEventListener("click", () => {
    // TODO
  });

  document.getElementById("goBackBtn").addEventListener("click", () => {
    window.location.href = "/";
  });

  // Utility functions
  function onStart() {
    const codeModal = new bootstrap.Modal(document.getElementById("codeModal"));
    if (codeModal) {
      codeModal.show();
    }
  }

  function addFlashcard(answer = null, definition = null) {
    flashcardCount++;
    const newFlashcard = document.createElement("div");
    const definitionId = `definition${flashcardCount}`;
    const answerId = `answer${flashcardCount}`;

    const flashcardDefinition = definition === null ? "" : definition;
    const flashcardAnswer = answer === null ? "" : answer;

    newFlashcard.classList.add("flashcard", "mb-3");
    newFlashcard.innerHTML = `
        <h5 class="mb-3">Flashcard ${flashcardCount}</h5>
        <div class="mb-3">
          <label for="${definitionId}" class="form-label">Definition</label>
          <textarea 
            name="${definitionId}" 
            class="form-control" 
            id="${definitionId}" 
            rows="2" 
            placeholder="Enter the flashcard definition"
          >${flashcardDefinition}</textarea>
        </div>
        <div class="mb-3">
          <label for="${answerId}" class="form-label">Answer</label>
          <input 
            name="${answerId}" 
            "type="text" 
            class="form-control" 
            id="${answerId}"
            value="${flashcardAnswer}" 
            placeholder="Enter the flashcard answer" 
          />
        </div>
        <hr />
      `;
    flashcardContainer.appendChild(newFlashcard);
  }

  function loadExistingDeck() {
    const flashcardCount = parseInt(
      document.getElementById("flashcardCount").innerText
    );
    for (let i = 0; i < flashcardCount; i++) {
      addFlashcard(
        document.getElementById(`flashcardAnswer${i}`).innerText,
        document.getElementById(`flashcardDefinition${i}`).innerText
      );
    }
    // To leave one empty for the users to modify or add to the deck
    addFlashcard();
  }

  // This condition determines if a pre-existing deck has been passed via Jinja
  if (document.getElementById("flashcardDefinition0")) {
    loadExistingDeck();
  }

  // On ready function calls
  onStart();
});
