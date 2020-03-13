
#import re

def get_mac():
    mac_buscar = input('Que mac desea buscar ? ')
    file = open('archivo.conf', 'r')
    success = ''    
    for line in file:
        macs = re.findall(r'((?:[\da-fA-F]{2}[:\-]){5}[\da-fA-F]{2})', line)
        if mac_buscar in macs:
            success = line
            break   
        
    if success != '':
        print(f'La busqueda fue exitosa, el resultado es el siguiente:\n{line}')
    else:
        print(f'La busqueda por la mac {mac_buscar} fue fallida')
    
        
if __name__ == "__main__":
    import re
    get_mac()