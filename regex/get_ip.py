#!/usr/bin/python  
# prints the ip from a given file and also the text (this can be changed)
                


def get_ip():
    file = list(open("/home/omar.silva/Documents/ejercicio6/archivo.conf", 'r').read().split('\n'))                    
    print('*********************\n')
    print('Las IPs usadas son las siguientes\n')
    print('*********************\n')
    for entry in file:
        #searches for the text, previous line of the IP
        texto = re.findall( r'[A-Z][a-z].+', entry )
        if texto:  
            print(str(texto))
        ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}', entry)
        for ip in ips:
            print(ip)
        

                    
if __name__ =='__main__':
    import re
    get_ip()