document.addEventListener("DOMContentLoaded", function () {
  const flashcardContainer = document.getElementById("flashcardContainer");
  const addFlashcardBtn = document.getElementById("addFlashcardBtn");

  let flashcardCount = 1; // Start with 1 flashcard

  // Add new flashcard when button is clicked
  addFlashcardBtn.addEventListener("click", () => {
    flashcardCount++;
    const newFlashcard = document.createElement("div");
    const definitionId = `definition${flashcardCount}`;
    const answerId = `answer${flashcardCount}`;

    newFlashcard.classList.add("flashcard", "mb-3");
    newFlashcard.innerHTML = `
        <h5 class="mb-3">Flashcard ${flashcardCount}</h5>
        <div class="mb-3">
          <label for="${definitionId}" class="form-label">Definition</label>
          <textarea name="${definitionId}" class="form-control" id="${definitionId}" rows="2" placeholder="Enter the flashcard definition"></textarea>
        </div>
        <div class="mb-3">
          <label for="${answerId}" class="form-label">Answer</label>
          <input name="${answerId}" "type="text" class="form-control" id="${answerId}" placeholder="Enter the flashcard answer">
        </div>
        <hr>
      `;
    flashcardContainer.appendChild(newFlashcard);
  });

  // Load, Save, Go Back event listeners can be added here
  document.getElementById("loadDeckBtn").addEventListener("click", () => {
    alert("Load flashcard deck functionality goes here.");
  });

  document.getElementById("saveDeckBtn").addEventListener("click", () => {
    alert("Save flashcard deck functionality goes here.");
  });

  document.getElementById("goBackBtn").addEventListener("click", () => {
    window.history.back(); // Navigates back to the previous page
  });
});
