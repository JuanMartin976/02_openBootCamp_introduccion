/* Para el bucle Do While, deberás crear la misma estructura que en el While, pero solo se debe ejecutar una vez. */

/* let numeroWhile = parseInt(prompt('Ingrese un número entero menor que 3: '));
if (numeroWhile < 3){
    do {console.log(numeroWhile)
    numeroWhile = numeroWhile + 1}
    while (numeroWhile < 3)
}else{
    console.log('El número ingresado no es menor que 3.')
}; */

/* Por último, para el Switch, deberás crear la variable estacion, y distintos case para las cuatro estaciones del año. Dependiendo del valor de la variable estacion se deberá mandar un mensaje por consola informando de la estación en la que está. También habrá que poner un default para cuando el valor de la variable no sea una estación.  */

let estacion = prompt('¿En qué estación del año estamos?: ')
switch (estacion){
    case 'Primavera':
        console.log('Esperemos que crezcan muchas flores.')
        break;
    case 'Verano':
        console.log('Esperemos que no haga tanto calor.')
        break;
    case 'Otoño':
        console.log('Tenemos que ir preparándonos para el invierno.')
        break;
    case 'Invierno':
        console.log('Esperemos que no haga tanto frío.')
        break;
    default:
        console.log('Usted no ha ingresado una estación del año.')
};
