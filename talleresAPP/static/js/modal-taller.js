document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.btnInscribir').forEach(btn => {
      btn.addEventListener('click', function() {
          const tallerId = this.getAttribute('data-id');
          fetch(`/datos_taller/${tallerId}/`)
              .then(response => response.json())
              .then(data => {
                if (!document.querySelector('.swal2-container')) {
                    Swal.fire({ 
                      title: data.nombre, 
                      Text: 'FECHA: '+  `${data.fechaIni}`,
                      html: `
                      <div style="text-align: left">
                        <p><strong>Fecha Inicio:</strong> ${data.fechaIni}</p> 
                        <p><strong>Fecha Termino:</strong> ${data.fechaFin}</p> 
                        <p><strong>Horario:</strong> ${data.horario}</p> 
                        <p><strong>Descripción:</strong> ${data.descripcion}</p> 
                      </div>`,
                      footer: '¿Desea inscribirse a este taller?',
                      icon: 'info',
                      showCancelButton: true,
                      confirmButtonText: 'Confirmar',
                      cancelButtonText: 'Cancelar'
                    });
                  }
              })
              .catch(error => console.error('Error:', error));
      });
  });
});