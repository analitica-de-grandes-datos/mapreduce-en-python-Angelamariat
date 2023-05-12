#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

    for line in sys.stdin:
        line_split = line.strip().split('  ')
        letter = line_split[0]
        value = line_split[-1]
        sys.stdout.write("{}\t{}\t1\n".format(letter, value))