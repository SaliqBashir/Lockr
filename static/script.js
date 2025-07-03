  function togglePassword(id, btn) {
    const input = document.getElementById(id);
    if (input.type === "password") {
      input.type = "text";
      btn.textContent = "👁️";
    } else {
      input.type = "password";
      btn.textContent = "🙈";
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.getElementById("searchInput");
  const rows = document.querySelectorAll(".vault-row");

  searchInput.addEventListener("input", function () {
    const searchValue = searchInput.value.toLowerCase();

    rows.forEach(row => {
      const website = row.children[0].textContent.toLowerCase();
      const username = row.children[1].textContent.toLowerCase();

      if (website.includes(searchValue) || username.includes(searchValue)) {
        row.style.display = "";
      } else {
        row.style.display = "none";
      }
    });
  });
});

