const botonEliminar = document.querySelectorAll('.eliminar');

botonEliminar.forEach(boton => {
    boton.addEventListener('click', function(e){
        e.preventDefault();
        console.log(e.target.href);
        Swal.fire({
            title: "¿Confirmar la eliminacion?",
            showCancelButton: true,
            confirmButtonText: "Eliminar",
            confirmButtonColor: "#28a745",
            bachdrop: true,
            showLoaderOnConfirm: true,

            preConfirm:()=>{

                console.log(e.target.href);
                location.href = e.target.href;
            },
            allowOutsideClick:()=> false,
            allowEscapeKey:()=> false,
        })

    })
})

