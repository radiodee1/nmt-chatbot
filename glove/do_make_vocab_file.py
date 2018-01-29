#!/usr/bin/python3

if True:
    f = open("glove.42B.300d.txt",'r')
    g = open('glove.vocab.txt','w')
    h = f.readlines()
    for z in h:
        z = str(z)
        zz = z.split()
        zz = zz[0]
        print(zz)
        g.write(zz)
    g.close()
    f.close()
    
