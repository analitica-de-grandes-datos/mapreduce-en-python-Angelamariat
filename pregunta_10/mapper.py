#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    for line in sys.stdin:
        
        val, key = line.split("\t")
        key= list(key.strip().split(","))
        
        for letter in key:
            sys.stdout.write("{}\t{}\n".format(letter, val))