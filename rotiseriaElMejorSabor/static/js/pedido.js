//validar fecha, para que no pueda ser menor a la fecha actual
function compararFecha(){
    let fechaPedido=document.getElementById("fechaPedido").value;
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
    
    if(fechaPedido>fechaActualComparar){
        devolver= true;
        return true;
    }else if (fechaActualComparar == fechaPedido){
        devolver= true;
        return true;

    }else {
        alert('[ERROR] La fecha del pedido no puede ser anterior a la de fecha de hoy');
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
//mostrar para agregar comentario cuando selecciona devuelto o cancelado
function desactivarYActivarComentario(obj){
    if(obj.value==="5" || obj.value==="6"){
        document.getElementById("comentarioPedido").disabled = false;
        document.getElementById("comentarioPedido").focus();
    }else{
        document.getElementById("comentarioPedido").disabled = true;
    }
}



function validacion(){
    retornar = false;
    if(compararFecha()===true){
        retornar = true;
        return retornar;
    }else{
        return retornar;
    }
}
//validar fecha
let boton = document.getElementById("botonVerificar");
boton.addEventListener("click",verificarFechaBoton);