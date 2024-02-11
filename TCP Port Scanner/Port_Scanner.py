from socket import *

def conScan(tgtHost, tgtPort):
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((tgtHost, tgtPort))
        print('[+] %d/tcp open' % tgtPort)
        connskt.close()
    except:
        print('[-] %d/tcp closed' % tgtPort)

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('[-] Cannot resolve %s' % tgtHost)
        return

    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+] Scan resolve of: %s' % tgtName[0])
    except:
        print('\n[+] Scan resolve of: %s' % tgtIP)

    setdefaulttimeout(1)

    for tgtPort in tgtPorts:
        print('Scanning for the open port: %d' % tgtPort)
        conScan(tgtHost, int(tgtPort))

if __name__ == '__main__':
    portScan('google.com', [80, 28])
