#!/usr/bin/python3

from collections import Counter
import tokenize_weak
import sys

vocab_length = 20000
train_file = ''
v = []

def make_vocab():
    wordlist = []
    with open(train_file, 'r') as x:
        xx = x.read()
        for line in xx.split('\n'):
            line = tokenize_weak.format(line)
            y = line.lower().split()
            for word in y:
                wordlist.append(word)
        pass
    print('values read')
    wordset = set(wordlist)
    c = Counter(wordset)
    l = len(wordset)
    if l > vocab_length: l = vocab_length
    cc = c.most_common(l)
    #v = []
    for z in cc:
        v.append(z[0])
    #print(v)

def save_vocab():
    name = train_file.replace('train', 'vocab')
    if name == train_file:
        name += '.voc.txt'
    with open(name, 'w') as x:
        x.write('<s>\n</s>\n<unk>\n')
        for z in v:
            x.write(z + "\n")
        print('values written')
    pass

if __name__ == '__main__':
    train_file = 'train.big.from'

    if len(sys.argv) > 1:
        train_file = str(sys.argv[1])

    print(train_file)
    v = []
    make_vocab()
