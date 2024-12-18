document.addEventListener("DOMContentLoaded", function () {
  /* rescatamos el doom de los elementos necesarios en una primera instancia */
  const botonForm = this.getElementById("botonForm");
  const regionSelect = this.getElementById("region");
  const comunaSelect = this.getElementById("comuna");
  let flagPaso = 1;
  const paso1 = this.getElementById('paso1');
  const paso2 = this.getElementById('paso2');
  const paso3 = this.getElementById('paso3');

  botonForm.addEventListener("click", function () {
    /* validamos por paso */
    if (flagPaso == 1) {
      let pNombre = document.getElementById("p_nombre").value;
      let sNombre = document.getElementById("s_nombre").value;
      let pApellido = document.getElementById("p_apellido").value;
      let sApellido = document.getElementById("s_apellido").value;
      let fecha_nacimiento = document.getElementById("fecha_nacimiento").value;
      let genero = document.getElementById("genero").value;

      const errPNombre   = validaciones(document.getElementById("err_p_nombre"), pNombre == "" || !soloLetras(pNombre));
      const errSNombre   = validaciones(document.getElementById("err_s_nombre"), sNombre == "") || !soloLetras(sNombre);
      const errPApellido = validaciones(document.getElementById("err_p_apellido"), pApellido == "" || !soloLetras(pApellido));
      const errSApellido = validaciones(document.getElementById("err_s_apellido"), sApellido == "") || !soloLetras(sApellido);
      const errFechaNac  = validaciones(document.getElementById("err_nacimiento"), fecha_nacimiento == "");
      const errGenero    = validaciones(document.getElementById("err_genero"), genero == "");

      /* si se cumplen todas las condiciones seguimos al paso 2 */
      if (errPNombre && errSNombre && errPApellido && errSApellido && errFechaNac && errGenero) {
        flagPaso = 2;
        paso1.classList.add("d-none");
        paso2.classList.remove("d-none");
        document.getElementById('circle2').classList.add('activo');
      }

    } else if (flagPaso==2){
      let rut = document.getElementById("rut_adulto_mayor").value;
      let email = document.getElementById("email").value;
      let region = document.getElementById("region").value;
      let comuna = document.getElementById("comuna").value;
      let direccion = document.getElementById("direccion").value;

      const errRut    = validaciones(document.getElementById("err_rut"), rut == "" || !/^\d{7,8}[0-9kK]$/.test(rut));
      const errEmail  = validaciones(document.getElementById("err_email"), email == ""|| !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email));
      const errRegion = validaciones(document.getElementById("err_region"), region == "");
      const errComuna = validaciones(document.getElementById("err_comuna"), comuna == "");
      const errDirecc = validaciones(document.getElementById("err_direccion"), direccion == "");

      if (errRut && errEmail && errRegion && errComuna && errDirecc) {
        flagPaso = 3;
        paso2.classList.add("d-none");
        paso3.classList.remove("d-none");
        document.getElementById('circle3').classList.add('activo');
        botonForm.innerHTML = "Registrar";
      }


    } else {
      let clave1 = document.getElementById("contrasenia1").value;        
      let clave2 = document.getElementById("contrasenia2").value;    
      const errClaves = validaciones(document.getElementById("err_contrasenia"), clave1 != clave2 || clave1 == "");

      if (errClaves) {
        botonForm.setAttribute("type", "submit");
        botonForm.click();
      }

    }
  });
  
  /* Esperamos que region se modifique para entregarle los datos a comuna segun la region que seleccionemos */
  regionSelect.addEventListener('change', function() {
    const regionId = this.value;
    if (regionId) {
        fetch(`/get_comunas/?region_id=${regionId}`).then(response => response.json()).then(data => {
            comunaSelect.innerHTML = '<option value="" disabled selected>Seleccione una comuna</option>';
            data.forEach(comuna => {
                const option = document.createElement('option');
                option.value = comuna.id;
                option.textContent = comuna.nombre;
                comunaSelect.appendChild(option);
            });
            comunaSelect.removeAttribute('disabled');
        });
    } else{
        comunaSelect.innerHTML = '<option value="">Seleccione una comuna</option>';
        comunaSelect.setAttribute('disabled', 'disabled');
    };
});
  /* Esperamos que comuna se modifique para activar la casilla de dirección */
  comunaSelect.addEventListener('change', function() {
    const direccion = document.getElementById('direccion');
    direccion.removeAttribute('disabled');
  });
});

/* Funcion de validaciones que se reutiliza durante el proceso del formulario */
function validaciones(errorDoom, condicion){
  if (condicion) {
    errorDoom.classList.remove("d-none");
    return false;
  } else {
    errorDoom.classList.add("d-none");
    return true;
  }
}

/* Expresion regular para evitar numeros en nombres */
function soloLetras(e) {
  return /^[a-zA-ZñÑáéíóúÁÉÍÓÚüÜ]+$/.test(e);
}
