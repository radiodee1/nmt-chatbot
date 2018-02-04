#!/usr/bin/python3

import sqlite3
import pandas as pd
import os
import re
import core.tokenizer as ct

timeframes = ['input']

to_lower = True
test_on_screen = False
remove_caps = True

def format(content, do_tokenize=False):
    c = content.strip()
    c = re.sub('[][)(\n\r#@*^>:<]',' ', c)
    c = re.sub('[.]',' . ',c)
    c = re.sub('[!]',' ! ',c)
    c = re.sub('[?]',' ? ',c)
    c = re.sub('[,]',' , ',c)
    c = re.sub('[-]',' ',c)

    c = c.split()
    cx = []
    for i in range(len(c)):
        if to_lower: cc = c[i].lower().strip()
        else : cc = c[i].strip()
        if cc.startswith("http") or cc.startswith('(http'):
            cc = '<unk>'
        if not to_lower and (i == 0 or c[i-1].endswith('.') or c[i-1].endswith('?') or c[i-1].endswith('!')) :
            lst = list(cc)
            ## first letter
            if not remove_caps: lst[0] = lst[0].upper()
            else: lst[0] = lst[0].lower()
            cc = ''.join(lst)
        if not to_lower and (cc.isupper() or (len(cc) > 1 and cc[1].isupper())):
            cc = cc.lower()
        cx.append(cc)
    x = ' '.join(cx)
    if do_tokenize: x = ct.tokenize(x)

    if test_on_screen: print(x)
    return x

