import threading
import socket

with open('list.txt') as f:
    for line in f:
        for domain in line.split():
            print("----------------------------------------------------------------------------------")
            print(domain)
            target = domain
            #ip = socket.gethostbyname(target)
            exception = [80,8080,443,8443,2052,2053,2082,2083,2086,2087,2095,2096,8880]
            c=0
            def inc():
                global c
                c += 1

            def portscan(port):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                try:
                    con = s.connect((target,port))

                    print('Port :',port,"is open.")
                    with open("%s.txt" %target, "a") as f:
                        f.write("Port: ")
                        f.write(str(port))
                        f.write(" is open.\n")
                    if port in exception :
                        pass
                    else :
                        inc()
                        print(port)
                        con.close()
                except:
                    pass
            r = 1
            for x in range(1,65535):

                t = threading.Thread(target=portscan,kwargs={'port':r})

                r += 1
                t.start()
            print('\n')
            print('Open ports:', c)
            print("----------------------------------------------------------------------------------")
