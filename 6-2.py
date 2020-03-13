
#!/usr/bin/python3.6
#imprime aquellas Ip libres, no asignadas por el DHCP. En un archivo a parte se encuentran las IP asignadas


#import re
def get_free_ips():

    dhcp_ips = []
    #arma una lista con todas las ips
    for i in range(1, 255 ):
        dhcp_ips.append(f'192.168.88.{i}')
    file = list(open("/path/to/some/file", 'r').read().split('\n'))
    i = 0 
    print('*********************\n') 
    print('The following IPs are not in use:\n')
    print('*********************')
    for line in file:
        
        ips = re.findall(r'^([0-9A-F]{2}[:-]){5}([0-9A-F]{2})$', line)

        if ips not in dhcp_ips:
            #print('\n')
            print(dhcp_ips[i])
        i += 1
       
         
    
        
if __name__ == '__main__':
     import re
     get_free_ips() 
            
        


