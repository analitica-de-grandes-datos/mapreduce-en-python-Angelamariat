#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

    for line in sys.stdin:
        key, value =line.strip().split(',')
        sys.stdout.write("{}\t{}\n".format(key, value))