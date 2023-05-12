#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

    #
    # itera sobre cada linea de codigo recibida
    # a traves del flujo de entrada
    #
    for line in sys.stdin:
        line_split=line.split(',')
        purpose=line_split[3]
        amount=line_split[4]
        sys.stdout.write("{}\t{}\n".format(purpose,amount))