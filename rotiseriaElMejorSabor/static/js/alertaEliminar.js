const botonEliminar = document.querySelectorAll('.eliminar');




botonEliminar.forEach(boton => {
    boton.addEventListener('click', function(e){
        e.preventDefault();

        Swal.fire({
            title: "¿Confirmar la eliminacion?",
            showCancelButton: true,
            confirmButtonText: "Eliminar",
            confirmButtonColor: "#28a745",
            bachdrop: true,
            showLoaderOnConfirm: true,
            preConfirm:()=>{
                location.href = e.target.href;
            },
            allowOutsideClick:()=> false,
            allowEscapeKey:()=> false,
        })

    })
})

