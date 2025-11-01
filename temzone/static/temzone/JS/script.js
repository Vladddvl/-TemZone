document.addEventListener("DOMContentLoaded", function () {
    // Модальное окно авторизации
    const authModal = document.getElementById("authModal");
    const openModalBtn = document.getElementById("openModalBtn");
    const authModalClose = document.getElementById("authModalClose");
  
    // Модальное окно регистрации
    const regModal = document.getElementById("regModal");
    const regModalClose = document.getElementById("regModalClose");
    const openRegModalLink = document.getElementById("openRegModalLink");
  
    // Открытие модального окна авторизации
    openModalBtn.addEventListener("click", function (event) {
      event.preventDefault();
      authModal.style.display = "flex";
    });
  
    // Закрытие модального окна авторизации
    authModalClose.addEventListener("click", function () {
      authModal.style.display = "none";
    });
  
    // Открытие модального окна регистрации по клику на ссылку Registration
    openRegModalLink.addEventListener("click", function (event) {
      event.preventDefault();
      authModal.style.display = "none";
      regModal.style.display = "flex";
    });
  
    // Закрытие модального окна регистрации
    regModalClose.addEventListener("click", function () {
      regModal.style.display = "none";
    });
  
    // Закрытие окон при клике вне модального окна
    window.addEventListener("click", function (event) {
      if (event.target === authModal) {
        authModal.style.display = "none";
      }
      if (event.target === regModal) {
        regModal.style.display = "none";
      }
    });
  });