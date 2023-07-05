const formRegistro = document.getElementById("registro");
const inputs = document.querySelectorAll("#registro input, #registro select");
const password = document.getElementById("form_password");
const confirmPassword = document.getElementById("form_password_confirm");

// Validaciones de formulario
inputs.forEach((input) => {
  input.addEventListener("blur", function (event) {
    if (input.checkValidity() === false) {
      input.classList.remove("is-valid");
      input.classList.add("is-invalid");
    } else {
      input.classList.remove("is-invalid");
      input.classList.add("is-valid");
    }
  });

  input.addEventListener("keyup", function (event) {
    if (input.checkValidity() === false) {
      input.classList.remove("is-valid");
      input.classList.add("is-invalid");
    } else {
      input.classList.remove("is-invalid");
      input.classList.add("is-valid");
    }
  });

  input.addEventListener("change", function (event) {
    if (input.checkValidity() === false) {
      input.classList.remove("is-valid");
      input.classList.add("is-invalid");
    } else {
      input.classList.remove("is-invalid");
      input.classList.add("is-valid");
    }
  });
});

formRegistro.addEventListener("submit", function (event) {
  if (formRegistro.checkValidity() === false) {
    event.preventDefault();
    event.stopPropagation();
  }
  formRegistro.classList.add("was-validated");
});

// Función para validar la confirmación de contraseña
function validatePassword() {
  if (password.value !== confirmPassword.value) {
    confirmPassword.setCustomValidity("Las contraseñas no coinciden");
  } else {
    confirmPassword.setCustomValidity("");
  }
}

// Agregar evento de validación a confirmPassword
confirmPassword.addEventListener("input", validatePassword);
confirmPassword.addEventListener("blur", validatePassword);
// Agregar evento de validación a formRegistro
formRegistro.addEventListener("submit", validatePassword);

function mostrarContrasena(){
  let tipo = document.getElementById("form_password");
  if(tipo.type == "password"){
      tipo.type = "text";
  }else{
      tipo.type = "password";
  }
  document.getElementById('toggle-password').querySelector('i').classList.toggle('bi-eye-fill');
  document.getElementById('toggle-password').querySelector('i').classList.toggle('bi-eye-slash-fill');
}

function mostrarContraConfirmada(){
  let tipo = document.getElementById("form_password_confirm");
  if(tipo.type == "password"){
      tipo.type = "text";
  }else{
      tipo.type = "password";
  }
  document.getElementById('toggle-password2').querySelector('i').classList.toggle('bi-eye-fill');
  document.getElementById('toggle-password2').querySelector('i').classList.toggle('bi-eye-slash-fill');
}


//Registro - Reinicio Animación fa-beat-fade para Botón .regreso-inicio
let regresoInicio = document.getElementById("regreso-inicio");

regresoInicio.addEventListener("mousemove", function () {
  $(".fa-beat-fade", this).on("mouseleave", function () {
    $(this).removeClass("salta");
  });
  $(".fa-beat-fade", this).on("mouseenter", function () {
    $(this).addClass("salta");
  });
});

function validarCorreo() {
  var correo = document.getElementById('form_correo').value;
  var regex = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/;
  
  if (!regex.test(correo)) {
      // El correo no es válido
      document.getElementById('form_correo').setCustomValidity('Debe colocar un correo electrónico válido');
  } else {
      // El correo es válido
      document.getElementById('form_correo').setCustomValidity('');
  }
}