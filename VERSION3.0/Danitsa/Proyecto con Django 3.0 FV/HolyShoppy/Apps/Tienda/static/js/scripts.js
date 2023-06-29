// Funcionalidad de 'sidenav'
// $(document).ready(function () {
//   $(".sidenav").sidenav();
// });

// $(document).ready(function () {
//   // Cierra el menú al hacer clic en un enlace
//   $(".navbar-nav li a").click(function(event) {
//     $(".navbar-collapse").collapse('hide');
//   });
// });
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
// Reinicio de la animación fa-bounce (rebote del carro)
let bolsita = document.getElementById("bolsita");

bolsita.addEventListener("mousemove", function () {
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
