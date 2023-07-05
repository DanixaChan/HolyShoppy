// Reinicio de la animación fa-bounce (rebote del carro)
  let carrito_icon = document.getElementById("carro");
  
  carrito_icon.addEventListener("mousemove", function () {
    $(".fa-bounce", this).on("mouseleave", function () {
      $(this).removeClass("fa-bounce");
    });
    $(".fa-bounce", this).on("mouseenter", function () {
      $(this).addClass("fa-bounce");
    });
  });