
document.addEventListener('DOMContentLoaded', function() {
    /* Accede al doom del seelect region y comuna */
    const regionSelect = document.getElementById('id_1-region');
    const comunaSelect = document.getElementById('id_1-comuna');
    const direccion = document.getElementById('id_1-direccion');
    /* Cuando region tiene un cambio e ejecuta */
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

    comunaSelect.addEventListener('change', function() {
        const comunaId = this.value;
        if (comunaId) {
            direccion.removeAttribute('disabled');
        }
    });

});