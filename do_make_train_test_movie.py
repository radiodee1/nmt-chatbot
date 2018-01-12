#!/usr/bin/python3

import sqlite3
import pandas as pd
import codecs
import os

timeframes = ['input']

def format(c):
    c = c + '\n'
    return c


for timeframe in timeframes:
    connection = sqlite3.connect('{}.db'.format(timeframe))
    c = connection.cursor()
    limit = 5000
    last_unix = 0
    cur_length = limit
    counter = 0
    test_done = False
    test_once = False
    print('cursor rowcount', c.rowcount)

    while cur_length > counter  or (c.rowcount == -1 and not test_once):

        df = pd.read_sql("SELECT * FROM parent_reply WHERE parent NOT NULL and score > 0 ".format(last_unix),connection)
        last_unix = 0 
        cur_length = len(df)

        if not test_done:
            with codecs.open('test.from','a', 'utf-8-sig') as f:
                for content in df['parent'].values:
                    content = format(content)
                    f.write(content)

            with codecs.open('test.to','a', 'utf-8-sig') as f:
                for content in df['comment'].values:
                    content = format(content)                
                    f.write(content)

            test_done = True

        else:
            with codecs.open('train.from','a', 'utf-8-sig') as f:
                for content in df['parent'].values:
                    content = format(content)
                    f.write(content)

            with codecs.open('train.to','a', 'utf-8-sig') as f:
                for content in df['comment'].values:
                    content = format(content)
                    f.write(content)

        counter += 1
        if counter % 20 == 0:
            print(counter,'rows completed so far')
        
        test_once = True

    os.system('mv test.from test.to new_data/.')
    os.system('mv train.from train.to new_data/.')
