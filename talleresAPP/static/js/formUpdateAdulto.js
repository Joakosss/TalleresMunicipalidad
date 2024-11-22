document.addEventListener("DOMContentLoaded", function () {
    const regionSelect = this.getElementById("region");
    const comunaSelect = this.getElementById("comuna");

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

});


/* Funcion de validaciones que se reutiliza durante el proceso del formulario */
function validaciones(errorDoom, condicion){
    if (condicion) {
      errorDoom.classList.remove("d-none");
    } else {
      errorDoom.classList.add("d-none");
    }
  }