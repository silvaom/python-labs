#!/usr/bin/python3.6

#!/usr/bin/python3.6
#searches for a specific area on a given file

#import re
def get_area():
    success= 0
    area_buscar = input('Que area desea buscar ? ')
    file = open('archivo.conf', 'r')
    for line_num, line in enumerate(file):
        areas = re.findall(r'^\#[\w\s]*\w$', line)
        if area_buscar in areas:
            
            success = line_num
            break

    if success != 0:
        print(f'La busqueda fue exitosa,el area buscada esta en la linea:\n{success}')
        
    else:
        print(f'La busqueda del area {area_buscar} no produjo ningun resultado')
    
        

if __name__ =='__main__':
    import re
    get_area()