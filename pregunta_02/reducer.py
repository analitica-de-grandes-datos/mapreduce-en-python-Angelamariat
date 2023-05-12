#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

# Esta funcion reduce los elementos que tienen la misma clave

if __name__ == '__main__':

    curkey = None
    max_val = 0

    # cada linea de texto recibida es una entrada clave \tabulador valor

    for line in sys.stdin:

        key, val = line.split("\t")
        val = int(val)

        if key == curkey:
       
            if max_val < val:
                
                max_val = val
                
        else:

            if curkey is not None:

                sys.stdout.write("{}\t{}\n".format(curkey, max_val))

            curkey = key
            max_val = val
    sys.stdout.write("{}\t{}\n".format(curkey, max_val))