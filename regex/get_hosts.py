#!/usr/bin/python3.6

#!/usr/bin/python3.6
#searches for a a host on a given file

#import re
def get_host():
    success= ''
    host_buscar = input('Que host desea buscar ? ')
    file = open('archivo.conf', 'r')
    for line in file:
        macs = re.findall(r'host\s(\w+)', line)
        if host_buscar in macs:
            
            success = line
            break

    if success != '':
        print('La busqueda fue exitosa, el resultado es el siguiente:\n')
        print(success)
    else:
        print(f'La busqueda del host {host_buscar} no produjo ningun resultado')
    
        

if __name__ =='__main__':
    import re
    get_host()