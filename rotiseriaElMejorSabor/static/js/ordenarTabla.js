/**
 * Funcion para ordenar una tabla... tiene que recibir el numero de columna a
 * ordenar y el tipo de orden
 * @param int n
 * @param str tipo - ['str'|'int']
 */
 function sortTable(n,tipo) {
    var table, rows, switching, i, x, y, debeCambiar, direccion, contador = 0;//contador es como un contador
    //debeCambiar es debe cambiar
   
    table = document.getElementById("tablaRegistro");
    
    switching = true;
   //Establezca la dirección de clasificación en ascendente:
    direccion = "asc";
   
  /*Hacer un bucle que continuará hasta que no se haya realizado ningún cambio:*/
    while (switching) {
      //empezar diciendo: no se realiza ningún cambio:
      switching = false;
      rows = table.rows;
      /*Recorre todas las filas de la tabla (excepto la primera, que contiene encabezados de tabla):*/
      for (i = 1; i < (rows.length - 1); i++) {
        //empezar diciendo que no debería haber cambios:
        debeCambiar = false;
        /*Obtenga los dos elementos que desea comparar, uno de la fila actual y otro de la siguiente:*/
        x = rows[i].getElementsByTagName("TD")[n];
        y = rows[i + 1].getElementsByTagName("TD")[n];
        /*comprueba si las dos filas deben cambiar de lugar, según la dirección, asc o desc:*/
        if (direccion === "asc") {
          if ((tipo==="str" && x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) || (tipo==="int" && parseFloat(x.innerHTML) > parseFloat(y.innerHTML)) || (tipo==="date" && new Date(x.innerText) > new Date(y.innerText)) || (tipo==="float" && (parseFloat(x.innerText) > parseFloat(y.innerText))) ) {
            //si es así, márquelo como un interruptor y rompa el ciclo:
            debeCambiar= true;
            break;
          }
        } else if (direccion === "desc") {
          if ((tipo==="str" && x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) || (tipo==="int" && parseFloat(x.innerHTML) < parseFloat(y.innerHTML)) || (tipo==="date" && new Date(x.innerText) < new Date(y.innerText)) || (tipo==="float" && (parseFloat(x.innerText) < parseFloat(y.innerText)))) {
            //si es así, márquelo como un interruptor y rompa el ciclo:
            debeCambiar = true;
            break;
          }
        }
      }
      if (debeCambiar) {
        /*Si se ha marcado un cambio, haga el cambio y marque que se ha hecho un cambio:*/
        //parentNode= es el padre del nodo actual
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
        //Cada vez que se realiza un cambio, aumenta este conteo en 1:
        contador ++;
      } else {
        /*Si no se ha realizado ningún cambio Y la dirección es "asc", establezca la dirección en "desc" y vuelva a ejecutar el ciclo while.*/
        if (contador == 0 && direccion == "asc") {
          direccion = "desc";
          switching = true;
        }
      }
    }
  }