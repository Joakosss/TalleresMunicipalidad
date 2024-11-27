document.addEventListener('DOMContentLoaded', function () {
  const buttons = document.querySelectorAll('.btnInscribir');

  // Agrega evento click a cada botón de inscribirse
  buttons.forEach(btn => {
    btn.addEventListener('click', function() {
      const tallerId = this.getAttribute('data-id');

      // Muestra los datos del taller en modal 
      fetch(`/datos_taller/${tallerId}/`)
        .then(response => response.json())
         .then(data => {
          const f_ini = data.fechaIni;
          const f_fin = data.fechaFin;

          if (!document.querySelector('.swal2-container')) {
            Swal.fire({ 
              title: data.nombre,
              html: `
                <div style="text-align: left">
                  <p><strong>Fecha Inicio:</strong> ${data.fechaIni}</p> 
                  <p><strong>Fecha Termino:</strong> ${data.fechaFin}</p> 
                  <p><strong>Horario:</strong> ${data.horario}</p> 
                  <p><strong>Descripción:</strong> ${data.descripcion}</p> 
                </div>`,
              footer: '¿Desea inscribirse a este taller?',
              icon: 'question',
              showCancelButton: true,
              confirmButtonText: 'Confirmar',
              cancelButtonText: 'Cancelar'

            }).then((result) => {
              if (result.isConfirmed) {

                // Manda post request para inscribirse al taller
                fetch(`/inscribir_taller/${tallerId}/`, {
                  method: 'POST',
                  headers: {
                      'Content-Type': 'application/json',
                      'X-CSRFToken': getCookie('csrftoken')
                  },
                  body: JSON.stringify({
                      fecha_inicio: f_ini,
                      fecha_fin: f_fin
                  })
                })
                .then(response => {
                    if (!response.ok) {
                        return response.text().then(text => { throw new Error(text) });
                    }
                    return response.json();
                })
                .then(data => {
                    // Si hay error en la respuesta 
                    if (data.error) {
                      Swal.fire({
                          title: 'Error',
                          text: 'No se ha podido inscribir al taller',
                          icon: 'error'
                      });
                    } else {
                      // Inscribe exitosamente 
                      Swal.fire({
                        title: 'Inscripción exitosa',
                        text: 'Se ha inscrito correctamente al taller',
                        icon: 'success'
                      }).then(() => {
                        location.reload();
                  });
                }
              })
              .catch(error => {
                  console.error('Error:', error);
                  Swal.fire({
                    title: 'Error',
                    text: error.message,
                    icon: 'error'
                  });
              });
            } else if (result.dismiss === Swal.DismissReason.cancel) {
              Swal.close();
            }
          });
        }
      })
      .catch(error => console.error('Error:', error));
    });
  });
});

// Función para obtener el valor de la cookie
function getCookie(nombre) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, nombre.length + 1) === (nombre + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(nombre.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}