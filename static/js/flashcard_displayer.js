document.addEventListener("DOMContentLoaded", () => {
  const createFlashcardsBtn = document.getElementById("createFlashcardsBtn");
  const revealBtnTexts = {
    default: "Reveal Answer",
    toggled: "Display Defintion",
  };
  const revealBtn = document.getElementById("flashcardRevealBtn");
  const flashcardText = document.getElementById("flashcardText");
  const flashcards = []; // Each element of arr: { answer: "", definition: "" }

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

  revealBtn.addEventListener("click", () => {
    if (revealBtn.textContent === revealBtnTexts.default) {
      revealBtn.textContent = revealBtnTexts.toggled;
      // TODO: Change in the future to be dynamic (Both Answer and Definition)
      flashcardText.textContent = "Functions";
    } else {
      revealBtn.textContent = revealBtnTexts.default;
      flashcardText.textContent =
        "A reusable block of code that performs a specific task when called.";
    }
  });

  createFlashcardsBtn.addEventListener("click", () => {
    window.location.href = "/flashcard-editor";
  });

  fillFlashcards();
});
