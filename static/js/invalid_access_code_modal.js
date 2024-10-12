document.addEventListener("DOMContentLoaded", () => {
  function displayInvalidAccessCodeModal() {
    const invalidAccessCodeModal = new bootstrap.Modal(
      document.getElementById("invalidAccessCodeModal")
    );
    if (invalidAccessCodeModal) {
      invalidAccessCodeModal.show();
    }
  }

  displayInvalidAccessCodeModal();
});
