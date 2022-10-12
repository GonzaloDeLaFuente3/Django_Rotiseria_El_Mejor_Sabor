//validar fecha, para que no pueda ser menor a la fecha actual
function compararFecha(){
    let fechaNacimiento=document.getElementById("fechaNacimiento").value;
    let fechaActual = new Date();
    let mes = (fechaActual.getMonth()+1).toString()
    let devolver = false;
    if(mes.length<= 1){
        mes = "0"+ mes;
    }
    let dia = fechaActual.getDate().toString();
    if(dia.length<= 1){
        dia = "0"+ dia;
    }
    let fechaActualComparar = fechaActual.getFullYear() + "-" + mes + "-" +dia;
    
    if(fechaNacimiento<fechaActualComparar){
        devolver= true;
        return devolver;
    }else {
        alert('[ERROR] La fecha de nacimiento del empleado es incorrecta, Ingrese una fecha valida');
        return devolver;
    }
}

function verificarFechaBoton(){
    if(compararFecha()===true){
        document.getElementById("verificar").innerHTML="La fecha es valida"
        document.getElementById("verificar").style.color="green";
    }else{
        document.getElementById("verificar").innerHTML="La fecha no es valida"
        document.getElementById("verificar").style.color="red";
    }
}

//validar fecha
let boton = document.getElementById("botonVerificar");
boton.addEventListener("click",verificarFechaBoton);
/////////
function validacion(){
    retornar = false;
    if(compararFecha()===true){
        retornar = true;
        return retornar;
    }else{
        return retornar;
    }
}