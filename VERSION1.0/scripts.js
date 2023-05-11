function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}

var boton = document.getElementById("bPromociones");

boton.addEventListener("click", function() {
  window.location.href = "./promo.html";
});

function ir_menu()
{
     location.href = "./index.html";
}

function ir_promocion()
{
     location.href = "./promo.html";
}

function ir_categorias()
{
     location.href = "./pagCategorias.html";
}

function ir_contactos()
{
     location.href = "./contacto.html";
}