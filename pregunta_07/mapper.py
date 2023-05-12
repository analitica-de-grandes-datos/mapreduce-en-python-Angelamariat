#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

    for line in sys.stdin:
        line_split = line.strip().split('  ')
        letter = line_split[0].strip()
        date = line_split[1].strip()
        value = line_split[-1].strip()
        sys.stdout.write("{}\t{}\t{}\n".format(letter, date, value))