document.addEventListener("DOMContentLoaded", function () {
    const articlePrincipal = document.getElementById("articleMisTalleres");

});

function misParticipantes(id_taller){
    const participantes = fetch(`get-participantes/${id_taller}`)
    .then(response=> response.json())
    .then(data=>{
        if (Array.isArray()) {
            data.forEach(element => {
                /* document.getElementById("articleMisTalleres").innerHtml = mostrarParticipantes(element); */
                console.log(element);
            });
        } else {
            /* document.getElementById("articleMisTalleres").innerHtml = mostrarParticipantes(data); */
            console.log(data);
        }
    });
};

function mostrarParticipantes(data){
    return `<p>${data}Hola</p>`;
}

