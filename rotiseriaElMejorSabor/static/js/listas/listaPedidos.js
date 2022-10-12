const contenedorTabla = document.getElementById('contenedorPedidos');
const contenedorInformacion = document.getElementById('contenedorInformacion');
const botonAceptarPedido = document.getElementById('aceptarPedido');
const botonEnCamino = document.getElementById('pedidoenCamino');
const botonEntregado = document.getElementById('pedidoEntregado');

let listaPedidos = [
    {codigo: 1,fecha: "2022-09-07", hora: "15:38",menu: "Tarta de choclo x3, Medallones de pescado x12", precio: 1300,cliente: "Gabriel Avellaneda",domicilio: "La Carrera Fray Mamerto Esquiu",tipoEntrega: "Envío a domicilio",estado: "Pendiente",comentario: "Muy mal servicio"},
    {codigo: 2,fecha: "2023-12-01", hora: "18:48",menu: "Pizza Calabresa", precio: 800,cliente: "Tomas Cordero",domicilio: "Capital S.F.V.C",tipoEntrega: "Retira en el local",estado: "En preparación",comentario: "Mucha demora, la pizza se enfrío"},
    {codigo: 3,fecha: "2023-01-03", hora: "16:30",menu: "Napolitana", precio: 950,cliente: "Carlo Herrera",domicilio: "Capital S.F.V.C",tipoEntrega: "Retira en el local",estado: "Devuelto",comentario: "Buena atención"},
    {codigo: 4,fecha: "2022-11-13", hora: "21:40",menu: "3 Helados de chocolate", precio: 2500,cliente: "Esteban Frias",domicilio: "Valle Chico Av 22. y 39",tipoEntrega: "Retira en el local",estado: "En camino",comentario: "No hice este pedido"},
    {codigo: 5,fecha: "2024-09-16", hora: "22:30",menu: "12 Empanadas de pollo", precio: 1500,cliente: "De La Fuente Gonzalo",domicilio: "Capital S.F.V.C",tipoEntrega: "Envío a domicilio",estado: "Entregado",comentario: "Pedido por accidente"},
    {codigo: 6,fecha: "2020-10-25", hora: "20:38",menu: "6 Lomitos", precio: 7850,cliente: "Maria Pereyra",domicilio: "Valle Viejo El Bañado Casa 21 calle Elias Barrionuevo",tipoEntrega: "Retira en el local",estado: "Cancelado",comentario:"El lomito estaba muy salado"}
];

//CARGAR LOS PEDIDOS PENDIENTES DE UNA LISTA A UNA TABLA
listaPedidos.forEach((pedido) => {
    const tabla = document.createElement('tr');
    tabla.setAttribute("data-bs-toggle","modal");
    tabla.setAttribute("data-bs-target","#modalInformacion");
    tabla.setAttribute("onclick","cargarInformacion("+pedido.codigo+")");
    tabla.innerHTML = `
        <td scope="row">${pedido.codigo}</th>
        <td>${pedido.fecha}</td>
        <td>${pedido.hora}</td>
        <td>${pedido.menu}</td>
        <td>${pedido.precio}</td>
        <td>${pedido.cliente}</td>
        <td>${pedido.domicilio}</td>
        <td>${pedido.tipoEntrega}</td>
        <td>${pedido.estado}</td>`

    contenedorTabla.appendChild(tabla);
})

const cargarInformacion = (pedId) => {

    contenedorInformacion.innerHTML = ""
    botonAceptarPedido.classList.add('d-none');
    botonEnCamino.classList.add('d-none');
    botonEntregado.classList.add('d-none');
    botonEntregado.classList.remove('disabled');

    const item = listaPedidos.find((pedido) => pedido.codigo === pedId);

    if(item.estado == "Pendiente"){ //SI EL ESTADO DEL PEDIDO ES PENDIENTE
        botonAceptarPedido.classList.remove('d-none'); //EL BOTON ACEPTAR SE VISUALIZA
    }else if(item.estado == "En preparación"){  //DE LO CONTRARIO EL PEDIDO YA ESTA EN PREPARACION
        botonEnCamino.classList.remove('d-none'); //EL BOTON EN CAMINO SE VISUALIZA
    }else if(item.estado == "En camino"){ //DE LO CONTRARIO EL PEDIDO YA ESTA EN CAMINO
        botonEntregado.classList.remove('d-none'); //EL BOTON ENTREGADO TAMPOCO
    }else{
        botonEntregado.classList.remove('d-none'); //EL BOTON ENTREGADO TAMPOCO
        botonEntregado.classList.add('disabled');
    }
    const info = document.createElement('div');
    info.innerHTML = `
    <div class="row">
        <div class="col-sm-12">
            <strong>#Código:</strong>
            <span class="mx-2">${item.codigo}</span>
        </div>
    </div>
    <div class="row my-2">
        <div class="col-sm-12">
            <i class="bi bi-calendar-date-fill"></i>
            <strong>Fecha:</strong>
            <span class="mx-2">${item.fecha}</span>
        </div>
    </div>
    <div class="row">
        <div class="col-sm-12">
            <i class="bi bi-clock-fill"></i>
            <strong>Hora:</strong> 
            <span class="mx-2">${item.hora}</span>
        </div>
    </div>
    <div class="row my-2">
        <div class="col-sm-12">
            <i class="bi bi-box-seam"></i> 
            <strong>Menú:</strong>
            <span class="mx-2">${item.menu}</span>
        </div>
    </div>
    <div class="row">
        <div class="col-sm-12">
            <strong>$ Precio:</strong>
            <span class="mx-2">${item.precio}</span>
        </div>
    </div>
    <div class="row my-2">
        <div class="col-sm-12">
            <i class="bi bi-person-badge-fill"></i>
            <strong>Cliente:</strong>
            <span class="mx-2">${item.cliente}</span>
        </div>
    </div>
    <div class="row">
        <div class="col-sm-12">
            <i class="bi bi-geo-alt-fill"></i>
            <strong>Domicilio:</strong>
            <span class="mx-2">${item.domicilio}</span>
        </div>
    </div>
    <div class="row my-2">
        <div class="col-sm-12">
            <i class="bi bi-truck"></i>
            <strong>Tipo Entrega:</strong>
            <span class="mx-2">${item.tipoEntrega}</span>
        </div>
    </div>
    <div class="row">
        <div class="col-sm-12">
            <i class="bi bi-ui-checks-grid"></i>
            <strong>Estado:</strong>
            <span class="mx-2">${item.estado}</span>
        </div>
    </div>
    <div class="row mt-2 d-none" id="comentarioCliente">
        <div class="col-sm-12">
            <strong>Comentario del cliente:</strong>
            <textarea class="form-control" cols="15" rows="2" readonly style="resize: none;">${item.comentario}</textarea>
        </div>
    </div>
    `
    contenedorInformacion.appendChild(info);

    const comentarioCliente = document.getElementById('comentarioCliente');
    if(item.estado == "Devuelto" || item.estado == "Cancelado"){
        comentarioCliente.classList.remove('d-none');
    }
}