#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

# Esta funcion reduce los elementos que tienen la misma clave

if __name__ == '__main__':

    curkey = None
    max_val = 0
    min_val=0

    # cada linea de texto recibida es una entrada clave \tabulador valor

    for line in sys.stdin:

        key, val = line.split("\t")
        val=float(val)
        
        if key == curkey:

            if val > max_val:
                max_val = val
            
            if val < min_val:
                
                min_val = val
                
        else:
            #
            # Se cambio de clave. Se reinicia el acumulador.
            #
            if curkey is not None:
                #
                # una vez se han reducido todos los elementos
                # con la misma clave se imprime el resultado en
                # el flujo de salida
                #
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, max_val,min_val))

            curkey = key
            max_val = val
            min_val = val
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, max_val, min_val))