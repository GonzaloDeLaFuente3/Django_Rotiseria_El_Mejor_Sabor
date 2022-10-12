let notificaciones = []

const contenedorNotificaciones = document.getElementById('contenedorNotificaciones');
const contadorNotificaciones = document.getElementById('contadorNotificaciones');
const labelNotificacionesVacias = document.getElementById('labelNotificacionesVacias');

//PARA QUE LOS DATOS NO SE PIERDAN AL RECARGAR LA PAGINA
document.addEventListener('DOMContentLoaded',() =>{
    if(localStorage.getItem('notificaciones')){
        notificaciones = JSON.parse(localStorage.getItem('notificaciones'));
        actualizarNotificaciones();
    }
})

stockPlatos.forEach((producto) => {
    const div = document.createElement('div');
    div.classList.add('swiper-slide');
    div.classList.add('card');
    div.classList.add('h-100');
    div.innerHTML = `
    <img class="card-img-top" src=${producto.img} alt="comida"/>
    <div class="card-body p-4">
        <div class="text-center">
            <h5 class="fw-bolder">${producto.nombre}</h5>
            <div class="d-flex justify-content-center small text-warning mb-2">
                <div class="bi-star-fill"></div>
                <div class="bi-star-fill"></div>
                <div class="bi-star-fill"></div>
                <div class="bi-star-fill"></div>
                <div class="bi-star-fill"></div>
            </div>
            $${producto.precio}
        </div>
    </div>
    <div class="card-footer p-4 pt-0 border-top-0 bg-transparent">
        <div class="text-center">
        <a class="btn btn-outline-success mt-auto" type="button">Comprar</a>
        </div>
        <div class="text-center">
        <a class="btn btn-outline-primary mt-auto" type="button" id="agregar${producto.id}">Añadir al carrito</a>
        </div>
    </div>`

    if(producto.tipo_menu == "entrada"){
        contenedorEntrada.appendChild(div);
    }else if(producto.tipo_menu == "postre"){
        contenedorPostre.appendChild(div);
    }else{
        contenedorPrincipal.appendChild(div);
    }
    
    const boton = document.getElementById(`agregar${producto.id}`);
    boton.addEventListener('click', () =>{
        agregarCarrito(producto.id);
    })
})

const agregarCarrito = (prodId) => {
    if(carrito.some (prod => prod.id === prodId)){
        const prod = carrito.map(prod => {
            if(prod.id === prodId){
                prod.cantidad++;
            }
        })
    }else{
        const item = stockPlatos.find((prod) => prod.id === prodId);
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

    carrito.forEach((prod) => {
        const div = document.createElement('div');
        div.classList.add('pedidoCarrito');
        div.classList.add('row');
        div.classList.add('mx-2');
        div.classList.add('my-2');
        div.innerHTML = `
        <p class="col-sm-4 col-form-label">${prod.nombre}</p>
        <p class="col-sm-4 col-form-label">Precio: ${prod.precio}</p>
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
