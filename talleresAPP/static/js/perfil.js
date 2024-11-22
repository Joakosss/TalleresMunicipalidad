const btnDelete = document.getElementById("btnDelete");

btnDelete.addEventListener("click", confirmarEliminar);

function confirmarEliminar(){
    Swal.fire({
      title: "¿Estas seguro?",
      text: "No podras recuperar esta cuenta!",
      icon: "warning",
      confirmButtonText: "Confirmar",
      confirmButtonColor: "#3085d6",
      showCancelButton: true,
      cancelButtonText: "Cancelar",
      cancelButtonColor: "#d33",
      reverseButtons: true
    }).then((result) => {
      if (result.isConfirmed) {
        fetch("/delete_adulto").then(() => {
            Swal.fire({
              title: "Eliminado con exito!",
              text: "",
              icon: "success"
            }).then(() => {
              window.location.href = "/login";
            });
        });
      };
    });
}

