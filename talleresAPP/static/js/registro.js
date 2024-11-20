document.addEventListener("DOMContentLoaded", function () {
  const btnNext1 = this.getElementById("btnNext1");
  let flagPaso = 1;
  const paso1 = this.getElementById('paso1');
  const paso2 = this.getElementById('paso2');
  const paso3 = this.getElementById('paso3');

  btnNext1.addEventListener("click", function () {
    if (flagPaso == 1) {
      let pNombre = document.getElementById("p_nombre").value;
      let sNombre = document.getElementById("s_nombre").value;
      let pApellido = document.getElementById("p_apellido").value;
      let sApellido = document.getElementById("s_apellido").value;
      let fecha_nacimiento = document.getElementById("fecha_nacimiento").value;
      let genero = document.getElementById("genero").value;
      
      let errorpNom = document.getElementById("err_p_nombre");
      let errorsNom = document.getElementById("err_s_nombre");
      let errorPApe = document.getElementById("err_p_apellido");
      let errorSApe = document.getElementById("err_s_apellido");
      let errorNaci = document.getElementById("err_nacimiento");
      let errorGenero = document.getElementById("err_genero");

      if (pNombre == "") {
        errorpNom.classList.remove("d-none");
      } else {
        errorpNom.classList.add("d-none");
    }
    
      if (sNombre == "") {
        errorsNom.classList.remove("d-none");
      } else {
        errorsNom.classList.add("d-none");
    }
    
    if (pApellido == "") {
        errorPApe.classList.remove("d-none");
      } else {
        errorPApe.classList.add("d-none");
      }

      if (sApellido == "") {
        errorSApe.classList.remove("d-none");
      } else {
        errorSApe.classList.add("d-none");
      }

      if (fecha_nacimiento == "") {
        errorNaci.classList.remove("d-none");
      } else {
        errorNaci.classList.add("d-none");
      }

      if (genero == "") {
        errorGenero.classList.remove("d-none");
      } else {
        errorGenero.classList.add("d-none");
      }

      if (pNombre != "" && sNombre != "" && pApellido != "" && sApellido != "" && fecha_nacimiento != "" && genero != "") {
        flagPaso = 2;
        paso1.classList.add("d-none");
        paso2.classList.remove("d-none");
        document.getElementById('circle2').classList.add('activo');
      }

    } else if (flagPaso==2){

    } else {
        
    }
  });
});
