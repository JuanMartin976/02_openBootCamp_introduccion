""" Usando un if, crear una condición que compare si la variable numeroIf es positivo, negativo, o 0.
Pista: Los números inferiores a 0 son negativos y los superiores, positivos. """

""" numeroIf = int(input('Ingrese un número entero: '))
if numeroIf == 0:
    print('El número ingresado es cero.')
elif numeroIf < 0:
    print('El número ingresado es negativo.')
else:
    print('El número ingresado es positivo.') """

""" Crea un bucle While, este bucle tendrá que tener como condición que la variable numeroWhile sea inferior a 3, el bloque de código que tendrá el bucle deberá:
    * Incrementar el valor de la variable en uno cada vez que se ejecute.
    * Mostrarlo por pantalla cada vez que se ejecute. """

""" numeroWhile = int(input('Ingrese un número entero menor que 3: '))
if numeroWhile < 3:
    while numeroWhile < 3:
        print(numeroWhile)
        numeroWhile = numeroWhile + 1
else:
    print('El número ingresado no es menor que 3.') """

""" Para el bucle Do While, deberás crear la misma estructura que en el While, pero solo se debe ejecutar una vez. """

""" Para el bucle For, crea una variable numeroFor, esta variable tendrá como valor 0 y su condición será que la variable sea igual o menor que 3, se irá incrementando en 1 su valor cada vez que se ejecute y deberá mostrarse por pantalla. """

numeroFor = 0
while numeroFor <= 3:
    print(numeroFor)
    numeroFor = numeroFor + 1 
