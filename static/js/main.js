document.createEventListener("DOMContentLoaded", () => {
  const revealBtnTexts = {
    default: "Reveal Answer",
    toggled: "Display Defintion",
  };
  const revealBtn = document.getElementById("flashcardRevealBtn1");
  const flashcardText = document.getElementById("flashcardText1");
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
});
