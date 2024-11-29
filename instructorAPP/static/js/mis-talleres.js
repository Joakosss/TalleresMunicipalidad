function misParticipantes(id_taller){
    let modalBody = document.getElementById("modal-body-id");
    modalBody.innerHTML = `<div class="spinner-border" role="status">
                            <span class="sr-only">Loading...</span>
                           </div>`;

    fetch(`get-participantes/${id_taller}`)
    .then(response=> response.json())
    .then(data=>{
        modalBody.innerHTML = '';
        modalBody.innerHTML = `<h5>Participantes</h5>`;
        const participantes = Array.isArray(data) ? data : [data];

        if (participantes.length === 0) {
            modalBody.innerHTML += `<p>No hay participantes inscritos</p>`;
        } else {
            participantes.forEach(element => {
                modalBody.innerHTML += mostrarParticipantes(element);
            });
        }
    });
};

function mostrarParticipantes(data){
    return `<p>Nombre:<strong> ${data.nombre_adulto_mayor} </strong></p>`;
}

