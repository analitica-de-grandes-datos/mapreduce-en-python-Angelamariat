#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

# Esta funcion reduce los elementos que tienen la misma clave

if __name__ == '__main__':

    sort_data=[]
    
    for line in sys.stdin:

        key, date, val = line.split("\t")
        val=int(val)
        
        sort_data.append((key,date,val))
        
    contador=0
    for sort in sorted(sort_data, key=lambda x: x[2]):
        
        if contador<=5:   
            sys.stdout.write("{}   {}   {}\n".format(sort[0],sort[1],sort[2]))
            contador+=1