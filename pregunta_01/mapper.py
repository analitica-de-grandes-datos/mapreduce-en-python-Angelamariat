#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
# Esta es la funcion que mapea la entrada a parejas (clave, valor)
#
import sys
if __name__ == "__main__":

    #
    # itera sobre cada linea de codigo recibida
    # a traves del flujo de entrada
    #
    for line in sys.stdin:
        line_split=line.split(',')
        word=line_split[2]
        sys.stdout.write("{}\t1\n".format(word))
