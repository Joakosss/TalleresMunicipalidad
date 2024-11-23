document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.btnInscribir').forEach(btn => {
      btn.addEventListener('click', function() {
          const tallerId = this.getAttribute('data-id');
          fetch(`/datos_taller/${tallerId}/`)
              .then(response => response.json())
              .then(data => {
                  document.getElementById('modalNombreTaller').innerText = data.nombre;
                  document.getElementById('modalFechaInicio').innerText = `Fecha Inicio: ${data.fechaIni}`;
                  document.getElementById('modalFechaFin').innerText = `Fecha Termino: ${data.fechaFin}`;
                  document.getElementById('modalHorario').innerText = `Horario: ${data.horario}`;
              })
              .catch(error => console.error('Error:', error));
      });
  });
});


function mostrarAlerta() {
  alert('¡Botón clicado!');
}
