import re
# mac example:    
#       00-9D-41-F7-27-7E
mac_buscar = input('Que mac desea buscar ? ')
pattern = '^ (((\ d | ([af] | [AF])) {2}:) {5} (\ d | ([af] | [AF])) {2}) $ | ^ (((\ d | ([af] | [AF])) {2} -) {5} (\ d | ([af] | [AF])) {2}) $ | ^ $'
re_obj = re.compile(pattern)
file = open('archivo.conf', 'r')

for line in (file):
    match = re_obj.search(line)
    if match:
         
       print ("MATCH -> " , match)