#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

# Esta funcion reduce los elementos que tienen la misma clave

if __name__ == '__main__':

    curkey = None
    suma = 0
    count=0 

    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        key, val, contador = line.split("\t")
        val = float(val)
        contador=int(contador)

        if key == curkey:
            #
            # No se ha cambiado de clave. Aca se acumulan los valores para la misma
            # clave.
            #
            suma += val
            count += contador
        else:
            #
            # Se cambio de clave. Se reinicia el acumulador.
            #
            if curkey is not None:
             
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, suma/count))

            curkey = key
            suma = val
            count= contador
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, suma/count))