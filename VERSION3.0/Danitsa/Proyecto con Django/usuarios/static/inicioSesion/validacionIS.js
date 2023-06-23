const formInicioSesion = document.getElementById("form-session");
const inputs = document.querySelectorAll("#form-session input");
const password = document.getElementById("form_password");
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
});

formRegistro.addEventListener("submit", function (event) {
  if (formRegistro.checkValidity() === false) {
    event.preventDefault();
    event.stopPropagation();
  }
  formRegistro.classList.add("was-validated");
});

