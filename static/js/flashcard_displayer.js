document.addEventListener("DOMContentLoaded", () => {
  // Flashcard Bottom Buttons
  const createFlashcardsBtn = document.getElementById("createFlashcardsBtn");
  const nextFlashcardBtn = document.getElementById("flashcardNextBtn");
  const previousFlashcardBtn = document.getElementById("flashcardPreviousBtn");

  // Flashcard Components
  const flashcardText = document.getElementById("flashcardText");
  const revealBtn = document.getElementById("flashcardRevealBtn");
  const revealBtnTexts = {
    default: "Reveal Answer",
    toggled: "Display Defintion",
  };

  // Access Code Modal Components
  const submitBtn = document.getElementById("submitBtn");

  // Flashcards data
  const flashcards = []; // Each element of arr: { answer: "", definition: "" }
  let flashcardIndex = 0;

  function fillFlashcards() {
    let flashcardCount = 0;
    while (true) {
      const flashcardDefinition = document.getElementById(
        `flashcardDefinition${flashcardCount}`
      );
      const flashcardAnswer = document.getElementById(
        `flashcardAnswer${flashcardCount}`
      );

      if (!flashcardDefinition || !flashcardAnswer) {
        break;
      }

      flashcards.push({
        answer: flashcardAnswer.innerText,
        definition: flashcardDefinition.innerText,
      });
      flashcardCount++;
    }
  }

  function displayInvalidAccessCodeModal() {
    const invalidAccessCodeModal = new bootstrap.Modal(
      document.getElementById("invalidAccessCodeModal")
    );
    console.log(invalidAccessCodeModal);
    if (invalidAccessCodeModal) {
      invalidAccessCodeModal.show();
    }
  }

  function changeFlashcardContent() {
    revealBtn.textContent = revealBtnTexts.default;
    flashcardText.innerText = flashcards[flashcardIndex].definition;
  }

  // Flashcard Components Event Listeners
  revealBtn.addEventListener("click", () => {
    if (revealBtn.textContent === revealBtnTexts.default) {
      revealBtn.textContent = revealBtnTexts.toggled;
      flashcardText.textContent = flashcards[flashcardIndex].answer;
    } else {
      revealBtn.textContent = revealBtnTexts.default;
      flashcardText.textContent = flashcards[flashcardIndex].definition;
    }
  });

  // Flashcard Bottom Buttons Event Listeners
  createFlashcardsBtn.addEventListener("click", () => {
    window.location.href = "/flashcard-editor";
  });

  nextFlashcardBtn.addEventListener("click", () => {
    flashcardIndex++;
    if (flashcardIndex >= flashcards.length) {
      flashcardIndex = 0;
    }
    changeFlashcardContent();
  });

  previousFlashcardBtn.addEventListener("click", () => {
    flashcardIndex--;
    if (flashcardIndex < 0) {
      flashcardIndex = flashcards.length - 1;
    }
    changeFlashcardContent();
  });

  // Access Code Modal Event Listeners
  submitBtn.addEventListener("click", () => {
    const accessCodeInput = document.getElementById("accessCodeInput");
    if (accessCodeInput.value.length !== 7) {
      alert("Flashcard access code should contain strictly 7 characters!");
    } else {
      submitBtn.setAttribute("type", "submit");
    }
  });

  // onReady methods
  fillFlashcards();
  displayInvalidAccessCodeModal();
});
