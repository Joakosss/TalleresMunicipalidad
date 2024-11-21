document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.btnInscribir').forEach(btn => {
        btn.addEventListener('click', function() {
            const tallerId = this.getAttribute('data-id');
            fetch(`/datos_taller/${tallerId}/`)
                .then(response => response.json().then(response => response.json()).then(data => {
                    
                }))
                .then(data => {
                    document.getElementById('modalTallerId').innerText = `Id: ${data.id}`;
                    document.getElementById('modalNombreTaller').innerText = data.nombre;
                    document.getElementById('modalFechaInicio').innerText = `Descripción: ${data.descripcion}`;
                    document.getElementById('modalFechaFin').innerText = `Profesor: ${data.adulto}`;
                    document.getElementById('modalHorario').innerText = `Horario: ${data.horario}`;
                })
                .catch(error => console.error('Error:', error));
        });
    });
});
