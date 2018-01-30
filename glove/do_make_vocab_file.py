#!/usr/bin/python3

if True:
    tokens = [
        '<unk>', '<s>', '</s>'
    ]
    limit = 15000
    e = open('glove.embed.txt','w')
    f = open("glove.42B.300d.txt",'r')
    g = open('glove.vocab.txt','w')
    h = f.readlines()
    if len(h) < limit: limit = len(h)

    for x in range(len(tokens)):
        g.write(tokens[x] + '\n')
        e.write(tokens[x] + ' ')
        for y in range(300):
            if x == y:
                e.write(str(1.0) + ' ')
            else:
                e.write(str(0.0) + ' ')
        e.write('\n')

    for x in range(limit - len(tokens)):
        z = str(h[x])
        zz = z.split()
        zz = zz[0]
        print(zz)
        g.write(zz + '\n')
        e.write(h[x])
    g.close()
    f.close()
    e.close()
    
