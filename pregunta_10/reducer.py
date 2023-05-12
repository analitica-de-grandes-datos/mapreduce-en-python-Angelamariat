#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    numeros=[]
  
    for line in sys.stdin:

        key, val = line.split("\t")
        val = int(val)
        
        if key == curkey:
            
            numeros.append(val)
            
        else:

            if curkey is not None:
                
                numeros.sort()
                sys.stdout.write("{}\t{}\n".format(curkey, ','.join(str(x) for x in numeros)))

            curkey = key
            numeros= [val]

    numeros.sort()
    sys.stdout.write("{}\t{}\n".format(curkey, ','.join(str(x) for x in numeros)))