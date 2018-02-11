#!/usr/bin/python3

import sqlite3
import pandas as pd
import os
import tokenize_weak
import sys
#import core.tokenizer as ct

timeframes = ['input']

print(sys.argv)

if len(sys.argv) > 1:
    z = sys.argv[1].split('.')
    z = '.'.join(z[:-1])
    timeframes = [str(z)]

to_lower = True
test_on_screen = False
remove_caps = True

def format(s):
    return tokenize_weak.format(s)

for timeframe in timeframes:
    connection = sqlite3.connect('{}.db'.format(timeframe))
    c = connection.cursor()
    limit = 100 #5000
    last_unix = 0
    cur_length = limit
    counter = 0
    test_done = False

    while cur_length == limit:

        df = pd.read_sql("SELECT * FROM parent_reply WHERE unix > {} and parent NOT NULL and score > 0 ORDER BY unix ASC LIMIT {}".format(last_unix,limit),connection)

        try:
            last_unix = df.tail(1)['unix'].values[0]
        except:
            print('error')

            last_unix = 0

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
            limit = 5000
            cur_length = limit

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
            print(counter*limit, counter, 'rows completed so far')
            
    if not test_on_screen: os.system('mv train.from train.to test.from test.to new_data/.')
