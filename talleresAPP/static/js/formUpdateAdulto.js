document.addEventListener("DOMContentLoaded", function () {
    const regionSelect = this.getElementById("region");
    const comunaSelect = this.getElementById("comuna");
    const botonModif= this.getElementById("botonModif");
    const botonCancel= this.getElementById("botonCancel");
    const btnModificar = this.getElementById("btnModificar");

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
            });
        } else{
            comunaSelect.innerHTML = '<option value="">Seleccione una comuna</option>';
        };
    });

    botonModif.addEventListener("click",function(){
        let pNombre = document.getElementById("p_nombre").value;
        let sNombre = document.getElementById("s_nombre").value;
        let pApellido = document.getElementById("p_apellido").value;
        let sApellido = document.getElementById("s_apellido").value;
        let genero = document.getElementById("genero").value;
        let email = document.getElementById("email").value;
        let region = document.getElementById("region").value;
        let comuna = document.getElementById("comuna").value;
        let direccion = document.getElementById("direccion").value;

        const errPNombre   = validaciones(document.getElementById("err_p_nombre"), pNombre == "" || !soloLetras(pNombre));
        const errSNombre   = validaciones(document.getElementById("err_s_nombre"), sNombre == "") || !soloLetras(sNombre);
        const errPApellido = validaciones(document.getElementById("err_p_apellido"), pApellido == "" || !soloLetras(pApellido));
        const errSApellido = validaciones(document.getElementById("err_s_apellido"), sApellido == "") || !soloLetras(sApellido);
        const errGenero    = validaciones(document.getElementById("err_genero"), genero == "");
        const errEmail     = validaciones(document.getElementById("err_email"), email == ""|| !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email));
        const errRegion    = validaciones(document.getElementById("err_region"), region == "");
        const errComuna    = validaciones(document.getElementById("err_comuna"), comuna == "");
        const errDireccion = validaciones(document.getElementById("err_direccion"), direccion == "");
         
        if (errPNombre && errSNombre && errPApellido && errSApellido && errGenero && errEmail && errRegion && errComuna && errDireccion) {
            botonModif.setAttribute("type", "submit");
            botonModif.click();
        }

    });

    btnModificar.addEventListener("click",function(){
        document.getElementById("formMod").classList.remove("d-none");
        document.getElementById("miPerfil").classList.add("d-none");
    });

    botonCancel.addEventListener("click",function(){
        document.getElementById("formMod").classList.add("d-none");
        document.getElementById("miPerfil").classList.remove("d-none");
    });



});


/* Funcion de validaciones que se reutiliza durante el proceso del formulario */
function validaciones(errorDoom, condicion){
    if (condicion) {
      errorDoom.classList.remove("d-none");
      return false;
    } else {
      errorDoom.classList.add("d-none");
      console.log(errorDoom+" "+'pasado');
      return true;
    }
  }

  /* Expresion regular para evitar numeros en nombres */
function soloLetras(e) {
    return /^[a-zA-ZñÑáéíóúÁÉÍÓÚüÜ]+$/.test(e);
  }
  