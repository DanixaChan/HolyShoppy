// Funcionalidad de 'sidenav'
$(document).ready(function () {
  $(".sidenav").sidenav();
});

// Reinicio de la animación fa-bounce (rebote del carro)
let carrito = document.getElementById("carro");

carrito.addEventListener("mousemove", function () {
  $(".fa-bounce", this).on("mouseleave", function () {
    $(this).removeClass("fa-bounce");
  });
  $(".fa-bounce", this).on("mouseenter", function () {
    $(this).addClass("fa-bounce");
  });
});

//Redireccion de página
function irRegistro() {
  location.href = "./registro.html";
}
