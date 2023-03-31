// Selecciona el botón de hamburguesa y el menú de navegación
const button = document.querySelector(".navbar-toggler");
const menu = document.querySelector(".navbar-collapse");

// Agrega un evento de clic al botón de hamburguesa
button.addEventListener("click", () => {
  // Alternar la clase "show" en el menú de navegación
  menu.classList.toggle("show");
});