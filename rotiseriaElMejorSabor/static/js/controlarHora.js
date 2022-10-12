function agregarHoras(fecha,horas){
    return new Date(fecha.getTime()+ horas * 3600000);
}

var date = new Date()
var horaActual = date.getHours() + ":" + date.getMinutes();
var dateMasUno = agregarHoras(date,1);
var horaActualMasUno = dateMasUno.getHours() + ":" + dateMasUno.getMinutes();
var table = document.getElementById("tablaRegistro");
var rows = table.rows;
//var agregarAtributo = rows[1].getElementsByTagName("td")[0];
// agregarAtributo.parentNode.setAttribute('class','table-danger');
// console.log(agregarAtributo);
for (var i = 1; i < (rows.length); i++){
    var x = rows[i].getElementsByTagName("td")[2];
    if(x.innerText <=  horaActual){
        x.parentNode.setAttribute('class','table-danger');
    }else if(( horaActual< x.innerText) && (x.innerText <= horaActualMasUno) ){
        x.parentNode.setAttribute('class','table-warning');
    }else if (x.innerText >horaActualMasUno){
        x.parentNode.setAttribute('class','table-success');
    }
}

setInterval(function(){ location.href = location.href; }, 60000 * 5)