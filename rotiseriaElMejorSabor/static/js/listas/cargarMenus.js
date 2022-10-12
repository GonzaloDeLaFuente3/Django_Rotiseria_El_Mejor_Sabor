const contenedorMenus = document.getElementById('contenedorMenus'); //TABLA
const contenedorModificarMenu = document.getElementById('contenedorModificarMenu'); //MODAL
const botonAceptarPedido = document.getElementById('aceptarPedido');
const botonEnCamino = document.getElementById('pedidoenCamino');
const botonEntregado = document.getElementById('pedidoEntregado');

//CARGAR LOS MENUS DE UNA LISTA A UNA TABLA
listaPlatos.forEach((plato) => {
    const tabla = document.createElement('tr');

    tabla.innerHTML = `
        <td scope="row">${plato.id}</th>
        <td>${plato.nombre}</td>
        <td>${plato.descripcion}</td>
        <td>${plato.tipo_menu}</td>
        <td>${plato.tipo_comida}</td>
        <td>${plato.precio}</td>
        <td>${plato.vigencia}</td>
        <td>
            <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalModificarMenu" id="modificar${plato.id}"><i class="bi bi-pencil-square"></i></button>
            <button class="btn btn-danger mx-2" onClick = "eliminarMenu(${plato.id})"><i class="bi bi-trash-fill"></i></button>
        </td>`

    contenedorMenus.appendChild(tabla);

    const boton = document.getElementById(`modificar${plato.id}`);
    boton.addEventListener('click', () =>{
        modificarMenu(plato.id);
    })
})

//MODAL DE MODIFICAR UN MENU
const modificarMenu = (menId) => {
    var tm1;
    var tm2;
    var tm3;
    var tm4;
    
    var tc1;
    var tc2;
    var tc3;
    var tc4;
    var tc5;

    var v1;
    var v2;

    contenedorModificarMenu.innerHTML = ""
    const item = listaPlatos.find((plato) => plato.id === menId);

    switch(item.tipo_menu){
        case "entrada":
            tm1 = `value="1"`;
            tm2 = "selected";
            tm3 = `value="2"`;
            tm4 = `value="3"`;
            break;
        case "plato principal":
            tm1 = `value="1"`;
            tm2 = `value="2"`;
            tm3 = "selected";
            tm4 = `value="3"`;
            break;
        case "postre":
            tm1 = `value="1"`;
            tm2 = `value="2"`;
            tm3 = `value="3"`;
            tm4 = "selected";
            break;
    }
    switch(item.tipo_comida){
        case "Normal":
            tc1 = `value="1"`;
            tc2 = "selected";
            tc3 = `value="2"`;
            tc4 = `value="3"`;
            tc5 = `value="4"`;
            break;
        case "Vegetariano":
            tc1 = `value="1"`;
            tc2 = `value="2"`;
            tc3 = "selected";
            tc4 = `value="3"`;
            tc5 = `value="4"`;
            break;
        case "Celiaco":
            tc1 = `value="1"`;
            tc2 = `value="2"`;
            tc3 = `value="3"`;
            tc4 = "selected";
            tc5 = `value="4"`;
            break;
        case "Diabético":
            tc1 = `value="1"`;
            tc2 = `value="2"`;
            tc3 = `value="3"`;
            tc4 = `value="4"`;
            tc5 = "selected";
            break;
    }
    switch(item.vigencia){
        case "SI":
            v1 = "selected";
            v2 = `value="1"`;
            break;
        case "NO":
            v1 = `value="1"`;
            v2 = "selected";
            break;
    }

    const info = document.createElement('div');
    info.innerHTML = `
    <div class="input-group input-group-sm mb-2">
        <span class="input-group-text" id="inputGroup-sizing-sm">Código:</span>
        <input type="number" class="form-control" value="${item.id}" readonly>
    </div>
    <div class="input-group input-group-sm mb-2">
        <span class="input-group-text" id="inputGroup-sizing-sm">Nombre:</span>
        <input type="text" class="form-control" value="${item.nombre}">
    </div>
    <div class="input-group input-group-sm mb-2">
        <span class="input-group-text" id="inputGroup-sizing-sm">Descripción:</span>
        <input type="text" class="form-control" value="${item.descripcion}">
    </div>

    <div class="input-group input-group-sm mb-3">
        <label class="input-group-text">Tipo de plato:</label>
        <select class="form-select">
            <option ${tm1}>Seleccione una opción...</option>
            <option ${tm2}>entrada</option>
            <option ${tm3}>plato principal</option>
            <option ${tm4}>postre</option>
        </select>
    </div>
    <div class="input-group input-group-sm mb-3">
        <label class="input-group-text">Tipo de comida:</label>
        <select class="form-select">
            <option ${tc1}>Seleccione una opción...</option>
            <option ${tc2}>Normal</option>
            <option ${tc3}>Vegetariano</option>
            <option ${tc4}>Celiaco</option>
            <option ${tc5}>Diabético</option>
        </select>
    </div>
    <div class="input-group input-group-sm mb-2">
        <span class="input-group-text" id="inputGroup-sizing-sm">Precio:</span>
        <input type="number" class="form-control" value="${item.precio}">
    </div>
    <div class="input-group input-group-sm mb-3">
        <label class="input-group-text">Vigencia:</label>
        <select class="form-select">
            <option ${v1}>SI</option>
            <option ${v2}>NO</option>
        </select>
    </div>
    `
    contenedorModificarMenu.appendChild(info);
}