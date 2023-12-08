// Get references to the modal and overlay
var modal3 = document.getElementById("modalOverlay3");
var openButton = document.getElementById("partner-btn");
var closeButton = document.getElementById("closeModal3");

// Open the modal when the "Sign Up" button is clicked
openButton.addEventListener("click", function () {
  modal3.style.display = "block";
});

// Close the modal when the close button is clicked
closeButton.addEventListener("click", function () {
  modal3.style.display = "none";
});

// Close the modal when the overlay (outside the modal) is clicked
modal3.addEventListener("click", function (event) {
  if (event.target === modal3) {
    modal3.style.display = "none";
  }
});

