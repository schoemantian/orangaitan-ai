function toggleUserPopup() {
    const popup = document.getElementById("user-popup");
    if (popup.style.display === "none") {
      popup.style.display = "block";
      document.addEventListener("click", closePopupOnClickOutside);
    } else {
      popup.style.display = "none";
      document.removeEventListener("click", closePopupOnClickOutside);
    }
  }
  
  function closePopupOnClickOutside(event) {
    const popup = document.getElementById("user-popup");
    const userButton = document.querySelector(".user-button");
  
    if (!popup.contains(event.target) && !userButton.contains(event.target)) {
      popup.style.display = "none";
      document.removeEventListener("click", closePopupOnClickOutside);
    }
  }
  