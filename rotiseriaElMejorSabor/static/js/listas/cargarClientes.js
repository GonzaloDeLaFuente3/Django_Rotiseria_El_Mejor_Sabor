const contenedorClientes = document.getElementById('contenedorClientes');//donde van a ir los td
const contenedorModificarCliente = document.getElementById('contenedorModificarCliente');//modal de modificar


//cargar tabla de clientes 
listaClientes.forEach((cliente)=>{
    const tabla = document.createElement('tr');
    tabla.innerHTML =`
        <td scope="row">${cliente.id}</th>
            <td>${cliente.cuil}</td>
            <td>${cliente.nombre}</td>
            <td>${cliente.apellido}</td>
            <td>${cliente.barrio}</td>
            <td>${cliente.localidad}</td>
            <td>${cliente.zona}</td>
            <td>${cliente.telefono}</td>
            <td>
                <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalModificarCliente" id="modificar${cliente.id}"><i class="bi bi-pencil-square"></i></button>
                <button class="btn btn-danger mx-2" id="eliminar${cliente.id}" ><i class="bi bi-trash-fill"></i></button>
            </td>
        `
    contenedorClientes.appendChild(tabla);

    const boton = document.getElementById(`modificar${cliente.id}`);
    boton.addEventListener('click', () =>{
        modificarCliente(cliente.id);
    })
});

//MODAL DE MODIFICAR UN CLIENTE
const modificarCliente = (cliId) => {
    var z1;
    var z2;
    var z3;
    var z4;
    var z5;

    contenedorModificarCliente.innerHTML = ""
    const item = listaClientes.find((plato) => plato.id === cliId);

    switch(item.zona){
        case "norte":
            z1 = `value="1"`;
            z2 = "selected";
            z3 = `value="2"`;
            z4 = `value="3"`;
            z5 = `value="4"`;
            break;
        case "sur":
            z1 = `value="1"`;
            z2 = `value="2"`;
            z3 = "selected";
            z4 = `value="3"`;
            z5 = `value="4"`;
            break;
        case "este":
            z1 = `value="1"`;
            z2 = `value="2"`;
            z3 = `value="3"`;
            z4 = "selected";
            z5 = `value="4"`;
            break;
        case "oeste":
            z1 = `value="1"`;
            z2 = `value="2"`;
            z3 = `value="3"`;
            z4 = `value="4"`;
            z5 = "selected";
            break;
    }

    const info = document.createElement('div');
    info.innerHTML = `
    <div class="input-group input-group-sm mb-2">
        <span class="input-group-text" id="inputGroup-sizing-sm">Código:</span>
        <input type="number" class="form-control" value="${item.id}" readonly>
    </div>
    <div class="input-group input-group-sm mb-2">
        <span class="input-group-text" id="inputGroup-sizing-sm">Cuil:</span>
        <input type="number" class="form-control" value="${item.cuil}">
    </div>
    <div class="input-group input-group-sm mb-2">
        <span class="input-group-text" id="inputGroup-sizing-sm">Nombre:</span>
        <input type="text" class="form-control" value="${item.nombre}">
    </div>
    <div class="input-group input-group-sm mb-2">
        <span class="input-group-text" id="inputGroup-sizing-sm">Apellido:</span>
        <input type="text" class="form-control" value="${item.apellido}">
    </div>
    <div class="input-group input-group-sm mb-2">
        <span class="input-group-text" id="inputGroup-sizing-sm">Barrio:</span>
        <input type="text" class="form-control" value="${item.barrio}">
    </div>
    <div class="input-group input-group-sm mb-2">
        <span class="input-group-text" id="inputGroup-sizing-sm">Localidad:</span>
        <input type="text" class="form-control" value="${item.localidad}">
    </div>
    <div class="input-group input-group-sm mb-3">
        <label class="input-group-text">Zona:</label>
        <select class="form-select">
            <option ${z1}>Seleccione una opción...</option>
            <option ${z2}>Norte</option>
            <option ${z3}>Sur</option>
            <option ${z4}>Este</option>
            <option ${z5}>Oeste</option>
        </select>
    </div>
    <div class="input-group input-group-sm mb-2">
        <span class="input-group-text" id="inputGroup-sizing-sm">Precio:</span>
        <input type="number" class="form-control" value="${item.telefono}">
    </div>
    `
    contenedorModificarCliente.appendChild(info);
}