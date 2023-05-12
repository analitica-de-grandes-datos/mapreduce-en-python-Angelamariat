#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

# Esta funcion reduce los elementos que tienen la misma clave

if __name__ == '__main__':

    #Inicializamos una lista vacia
    sorted_data = []
    for line in sys.stdin:

        key, val = line.strip().split('\t')
        val = int(val)
        sorted_data.append((key,val))
    
    for sort in sorted(sorted_data, key=lambda x: x[1]):
        sys.stdout.write("{},{}\n".format(sort[0],sort[1]))