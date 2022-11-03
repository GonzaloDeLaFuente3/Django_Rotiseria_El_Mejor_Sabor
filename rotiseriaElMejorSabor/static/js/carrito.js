
const contenedorCarrito = document.getElementById('contenedorCarrito');
const contadorCarrito = document.getElementById('contadorCarrito');
const precioTotal = document.getElementById('precioTotal');
const botonVaciar = document.getElementById('vaciarCarrito');
const botonComprar = document.getElementById('comprarCarrito');
const labelCarritoVacio = document.getElementById('labelCarritoVacio');

//PARA QUE LOS DATOS NO SE PIERDAN AL RECARGAR LA PAGINA
document.addEventListener('DOMContentLoaded',() =>{
    if(localStorage.getItem('carrito')){
        carrito = JSON.parse(localStorage.getItem('carrito'));
        actualizarCarrito();
    }
})

botonVaciar.addEventListener('click', () =>{
    carrito.length = 0;
    actualizarCarrito();
})

const agregarCarrito = (prodId) => {
    if(carrito.some (prod => prod.id === prodId)){
        const prod = carrito.map(prod => {
            if(prod.id === prodId){
                prod.cantidad++;
            }
        })
    }else{
        const item = listaPlatos.find((prod) => prod.id === prodId);
        carrito.push(item);
    }
    
    actualizarCarrito();
}

const eliminarDelCarrito = (prodId) => {
    const item = carrito.find((prod) => prod.id === prodId);
    carrito.splice(carrito.indexOf(item),1);
    actualizarCarrito();
}

const actualizarCarrito = () => {
    contenedorCarrito.innerHTML = ""

    //INFORMACION A MOSTRAR EN EL MODAL
    carrito.forEach((prod) => {
        const div = document.createElement('div');
        div.classList.add('pedidoCarrito');
        div.classList.add('row');
        div.classList.add('mx-2');
        div.classList.add('my-2');
        div.innerHTML = `
        <p class="col-sm-4 col-form-label">${prod.nombre}</p>
        <p class="col-sm-4 col-form-label">Precio: $${prod.precio}</p>
        <p class="col-sm-3 col-form-label" id="cantidad">Cantidad: ${prod.cantidad}</p>
        <div class="col-sm-1">
            <button class="btn btn-danger" onClick = "eliminarDelCarrito(${prod.id})"><i class="bi bi-trash-fill"></i></button>
        </div>`

        contenedorCarrito.appendChild(div);
    })
    localStorage.setItem('carrito',JSON.stringify(carrito));
    contadorCarrito.innerText = carrito.length;
    if(contadorCarrito.textContent == "0"){
        labelCarritoVacio.classList.remove('d-none');
        contadorCarrito.classList.add('d-none');
        botonVaciar.classList.add('disabled');
        botonComprar.classList.add('disabled');
    }else{
        labelCarritoVacio.classList.add('d-none');
        contadorCarrito.classList.remove('d-none');
        botonVaciar.classList.remove('disabled');
        botonComprar.classList.remove('disabled');
    }
    precioTotal.innerText = carrito.reduce((acc,prod) => acc + prod.precio*prod.cantidad, 0);
}
