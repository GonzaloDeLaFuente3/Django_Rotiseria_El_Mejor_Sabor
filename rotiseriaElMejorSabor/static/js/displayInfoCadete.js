const infoAdicionalCadete = document.getElementById('infoAdicionalCadete');
const guardarEmpleado = document.getElementById('guardarEmpleado');

function displayCadetes(){
    infoAdicionalCadete.classList.remove('d-none');
    guardarEmpleado.classList.add('d-none');
}

function displayEmpleados(){
    infoAdicionalCadete.classList.add('d-none');
    guardarEmpleado.classList.remove('d-none');
}