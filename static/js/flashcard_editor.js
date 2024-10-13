document.addEventListener("DOMContentLoaded", function () {
  const flashcardContainer = document.getElementById("flashcardContainer");
  const addFlashcardBtn = document.getElementById("addFlashcardBtn");
  const saveDeckBtn = document.getElementById("saveDeckBtn");
  const backBtn = document.getElementById("goBackBtn");

  let flashcardCount = 1; // Initial flashcard count

  // Event listeners
  addFlashcardBtn.addEventListener("click", () => {
    addFlashcard();
  });

  saveDeckBtn.addEventListener("click", () => {
    if (isDeckDataValid()) {
      saveDeckBtn.setAttribute("type", "submit");
    } else {
      alert("Please make sure you at least have one valid card!");
    }
  });

  backBtn.addEventListener("click", () => {
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
      const definition = document.getElementById(
        `flashcardDefinition${i}`
      ).innerText;
      const answer = document.getElementById(`flashcardAnswer${i}`).innerText;

      // For the initial flashcard textbox inputs of the page
      if (i === 0) {
        document.getElementById("answer1").value = answer;
        document.getElementById("definition1").value = definition;
      } else {
        addFlashcard(answer, definition);
      }
    }

    // To leave one empty for the users to modify or add to the deck
    addFlashcard();
  }

  function isDeckDataValid() {
    for (let i = 1; i <= flashcardCount; i++) {
      if (
        document.getElementById(`answer${i}`).value &&
        document.getElementById(`definition${i}`).value
      ) {
        return true;
      }
    }
    return false;
  }

  // This condition determines if a pre-existing deck has been passed via Jinja
  if (document.getElementById("flashcardDefinition0")) {
    loadExistingDeck();
  }

  // On ready function calls
  onStart();
});
