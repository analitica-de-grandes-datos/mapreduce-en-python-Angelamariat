#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

    for line in sys.stdin:
        letter=line.strip()[0]
        sys.stdout.write("{}\t1\n".format(letter))