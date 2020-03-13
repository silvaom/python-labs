#!/usr/bin/python3.6
#import re
#looks for a given ip on a given file
def get_ip():
    success = ''
    ip_buscar = input('Que ip desea buscar ? ')
    file = open('archivo.conf', 'r')
    
    for line in file:
        ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)
        if ip_buscar in ips :
            success = line
            break
        
           
    if success  != '':
        print(f'La {ip_buscar} fue encontrada:\n{line}')
    else:
        print(f'La busqueda de la ip: {ip_buscar} fue fallida')

if __name__ == '__main__':
    #this code will only execute when run as a script. Not when imported
    import re
    get_ip()
    
        