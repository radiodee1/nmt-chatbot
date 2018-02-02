#!/usr/bin/python3

import sqlite3
import pandas as pd
import os
import re
import core.tokenizer as ct

timeframes = ['input']

to_lower = True
test_on_screen = True
remove_caps = True

def format(content):
    c = content.strip()
    c = re.sub('[][)(\n\r#@*^><]',' ', c)
    #c = ct.tokenize(c)

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
    x = ct.tokenize(x)

    if test_on_screen: print(x)
    return x



for timeframe in timeframes:
    connection = sqlite3.connect('{}.db'.format(timeframe))
    c = connection.cursor()
    limit = 5000
    last_unix = 0
    cur_length = limit
    counter = 0
    test_done = False

    while cur_length == limit:

        df = pd.read_sql("SELECT * FROM parent_reply WHERE unix > {} and parent NOT NULL and score > 0 ORDER BY unix ASC LIMIT {}".format(last_unix,limit),connection)
        last_unix = df.tail(1)['unix'].values[0]
        cur_length = len(df)

        if not test_done:
            with open('test.from','a', encoding='utf8') as f:
                for content in df['parent'].values:
                    content = format(content)
                    f.write(content+'\n')

            with open('test.to','a', encoding='utf8') as f:
                for content in df['comment'].values:
                    content = format(content)
                    f.write(str(content)+'\n')

            test_done = True
            #limit = 5000

        else:
            with open('train.from','a', encoding='utf8') as f:
                for content in df['parent'].values:
                    content = format(content)
                    f.write(content+'\n')

            with open('train.to','a', encoding='utf8') as f:
                for content in df['comment'].values:
                    content = format(content)
                    f.write(str(content)+'\n')

        counter += 1
        if counter > 3 and test_on_screen: exit()
        if counter % 20 == 0:
            print(counter*limit,'rows completed so far')
            
    if not test_on_screen: os.system('mv train.from train.to test.from test.to new_data/.')
