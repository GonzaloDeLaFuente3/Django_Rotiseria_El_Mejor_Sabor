
const horaDesde = document.getElementById('horaDesde');
const horaHasta = document.getElementById('horaHasta');

var date = new Date();

var horaPedido = document.getElementById('horaPedido');
//Esto haré para corregir el problema de los minutos y las horas por
//el cambio de formato ya que usa el de 12 horas
if (date.getMinutes().toString().length == 1){
    date.value = "0"+date.getMinutes();
}
if(date.getHours().toString().length == 1){
    date.value = "0"+date.getHours();
}

horaPedido.value = date.getHours()+":"+date.getMinutes();

function cambiarFecha(){
    horaPedido.removeAttribute("disabled");
}

function validar(){
    return false;
}

