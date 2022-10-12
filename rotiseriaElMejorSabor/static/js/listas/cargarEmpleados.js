const contenedorCadetes = document.getElementById('contenedorCadetes');//donde van a ir los td
const contenedorEmpleados = document.getElementById('contenedorEmpleados');//donde van a ir los td

const contenedorModificarCadete = document.getElementById('contenedorModificarCadete');//modal de modificar
const contenedorModificarEmpleado = document.getElementById('contenedorModificarEmpleado');//modal de modificar

//cargar tabla de cadetes
listaCadetes.forEach((cadete)=>{
    const tabla = document.createElement('tr');
    tabla.innerHTML =`
        <td scope="row">${cadete.id}</th>
            <td>${cadete.cuil}</td>
            <td>${cadete.nombre}</td>
            <td>${cadete.apellido}</td>
            <td>${cadete.fechaNacimiento}</td>
            <td>${cadete.barrio}</td>
            <td>${cadete.localidad}</td>
            <td>${cadete.telefono}</td>
            <td>${cadete.fechaIngreso}</td>
            <td>${cadete.zona}</td>
            <td>${cadete.vigenciaCarnet}</td>
            <td>${cadete.patente}</td>
            <td>
                <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalModificarCadete" id="modificar${cadete.id}"><i class="bi bi-pencil-square"></i></button>
                <button class="btn btn-danger mx-1" id="eliminar${cadete.id}" ><i class="bi bi-trash-fill"></i></button>
            </td>
        `
    contenedorCadetes.appendChild(tabla);

    const boton = document.getElementById(`modificar${cadete.id}`);
    boton.addEventListener('click', () =>{
        modificarCadete(cadete.id);
    })
});

//cargar tabla de empleados
listaEmpleados.forEach((empleado)=>{
    const tabla = document.createElement('tr');
    tabla.innerHTML =`
        <td scope="row">${empleado.id}</th>
            <td>${empleado.cuil}</td>
            <td>${empleado.nombre}</td>
            <td>${empleado.apellido}</td>
            <td>${empleado.fechaNacimiento}</td>
            <td>${empleado.barrio}</td>
            <td>${empleado.localidad}</td>
            <td>${empleado.telefono}</td>
            <td>${empleado.fechaIngreso}</td>
            <td>
                <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalModificarEmpleado" id="modificar${empleado.id}"><i class="bi bi-pencil-square"></i></button>
                <button class="btn btn-danger mx-2" id="eliminar${empleado.id}" ><i class="bi bi-trash-fill"></i></button>
            </td>
        `
    contenedorEmpleados.appendChild(tabla);

    const boton = document.getElementById(`modificar${empleado.id}`);
    boton.addEventListener('click', () =>{
        modificarEmpleado(empleado.id);
    })
});


//MODAL DE MODIFICAR UN empleado
const modificarEmpleado = (empId) => {

    contenedorModificarEmpleado.innerHTML = ""
    const item = listaEmpleados.find((empleado) => empleado.id === empId);

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
        <span class="input-group-text" id="inputGroup-sizing-sm">Fecha de nacimiento:</span>
        <input type="date" class="form-control" value="${item.fechaNacimiento}">
    </div>
    <div class="input-group input-group-sm mb-2">
        <span class="input-group-text" id="inputGroup-sizing-sm">Barrio:</span>
        <input type="text" class="form-control" value="${item.barrio}">
    </div>
    <div class="input-group input-group-sm mb-2">
        <span class="input-group-text" id="inputGroup-sizing-sm">Localidad:</span>
        <input type="text" class="form-control" value="${item.localidad}">
    </div>
    <div class="input-group input-group-sm mb-2">
        <span class="input-group-text" id="inputGroup-sizing-sm">Telefono:</span>
        <input type="number" class="form-control" value="${item.telefono}">
    </div>
    <div class="input-group input-group-sm mb-2">
        <span class="input-group-text" id="inputGroup-sizing-sm">Fecha de ingreso:</span>
        <input type="date" class="form-control" value="${item.fechaIngreso}" readonly>
    </div>
    `
    contenedorModificarEmpleado.appendChild(info);
}

//MODAL DE MODIFICAR UN cadete
const modificarCadete = (cadId) => {
    var z1;
    var z2;
    var z3;
    var z4;
    var z5;

    contenedorModificarCadete.innerHTML = ""
    const item = listaCadetes.find((cadete) => cadete.id === cadId);

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
        <span class="input-group-text" id="inputGroup-sizing-sm">Fecha de nacimiento:</span>
        <input type="date" class="form-control" value="${item.fechaNacimiento}">
    </div>
    <div class="input-group input-group-sm mb-2">
        <span class="input-group-text" id="inputGroup-sizing-sm">Barrio:</span>
        <input type="text" class="form-control" value="${item.barrio}">
    </div>
    <div class="input-group input-group-sm mb-2">
        <span class="input-group-text" id="inputGroup-sizing-sm">Localidad:</span>
        <input type="text" class="form-control" value="${item.localidad}">
    </div>
    <div class="input-group input-group-sm mb-2">
        <span class="input-group-text" id="inputGroup-sizing-sm">Telefono:</span>
        <input type="number" class="form-control" value="${item.telefono}">
    </div>
    <div class="input-group input-group-sm mb-2">
        <span class="input-group-text" id="inputGroup-sizing-sm">Fecha de ingreso:</span>
        <input type="date" class="form-control" value="${item.fechaIngreso}" readonly>
    </div>
    <div class="input-group input-group-sm mb-3">
        <label class="input-group-text">Zona de entrega:</label>
        <select class="form-select">
            <option ${z1}>Seleccione una opción...</option>
            <option ${z2}>Norte</option>
            <option ${z3}>Sur</option>
            <option ${z4}>Este</option>
            <option ${z5}>Oeste</option>
        </select>
    </div>
    <div class="input-group input-group-sm mb-2">
        <span class="input-group-text" id="inputGroup-sizing-sm">Vigencia de carnet:</span>
        <input type="date" class="form-control" value="${item.vigenciaCarnet}" readonly>
    </div>
    <div class="input-group input-group-sm mb-2">
        <span class="input-group-text" id="inputGroup-sizing-sm">Patente:</span>
        <input type="text" class="form-control" value="${item.patente}">
    </div>
    `
    contenedorModificarCadete.appendChild(info);
}

