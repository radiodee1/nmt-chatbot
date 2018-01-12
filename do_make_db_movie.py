#!/usr/bin/python3

import codecs
import sqlite3
import os
from datetime import datetime

timeframe = 'movie_lines'
sql_transaction = []

connection = sqlite3.connect('{}.db'.format(timeframe))
c = connection.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS parent_reply(parent_id TEXT PRIMARY KEY, comment_id TEXT UNIQUE, parent TEXT, comment TEXT, subreddit TEXT, unix INT, score INT)")

def format_data(data):
    #data = str(data)

    data = data.replace('\n',' newlinechar ').replace('\r',' newlinechar ').replace('"',"'")
    data = data[:]
    #data = data.encode('utf8')
    return data

def transaction_bldr(sql):
    global sql_transaction
    sql_transaction.append(sql)
    if len(sql_transaction) > 1000:
        c.execute('BEGIN TRANSACTION')
        for s in sql_transaction:
            try:
                c.execute(s)
            except:
                pass
        connection.commit()
        sql_transaction = []

def sql_insert_replace_comment(commentid,parentid,parent,comment,subreddit,time,score):
    try:
        sql = """UPDATE parent_reply SET parent_id = ?, comment_id = ?, parent = ?, comment = ?, subreddit = ?, unix = ?, score = ? WHERE parent_id =?;""".format(parentid, commentid, parent, comment, subreddit, int(time), score, parentid)
        transaction_bldr(sql)
    except Exception as e:
        print('s0 insertion',str(e))

def sql_insert_has_parent(commentid,parentid,parent,comment,subreddit,time,score):
    try:
        sql = """INSERT INTO parent_reply (parent_id, comment_id, parent, comment, subreddit, unix, score) VALUES ("{}","{}","{}","{}","{}",{},{});""".format(parentid, commentid, parent, comment, subreddit, int(time), score)
        transaction_bldr(sql)
    except Exception as e:
        print('s0 insertion',str(e))

def sql_insert_no_parent(commentid,parentid,comment,subreddit,time,score):
    try:
        sql = """INSERT INTO parent_reply (parent_id, comment_id, comment, subreddit, unix, score) VALUES ("{}","{}","{}","{}",{},{});""".format(parentid, commentid, comment, subreddit, int(time), score)
        transaction_bldr(sql)
    except Exception as e:
        print('s0 insertion',str(e))

def sql_insert_complete(commentid,parentid,parent,comment,subreddit,time,score):
    try:
        sql = """INSERT INTO parent_reply (parent_id, comment_id,parent, comment, subreddit, unix, score) VALUES ("{}","{}","{}","{}","{}",{},{});""".format(parentid, commentid,parent, comment, subreddit, int(time), score)
        transaction_bldr(sql)
    except Exception as e:
        print('s0 insertion',str(e))


def acceptable(data):
    if len(data.split(' ')) > 50 or len(data) < 1:
        return False
    elif len(data) > 1000:
        return False
    elif data == '[deleted]':
        return False
    elif data == '[removed]':
        return False
    else:
        return True

def find_parent(pid):
    try:
        sql = "SELECT comment FROM parent_reply WHERE comment_id = '{}' LIMIT 1".format(pid)
        c.execute(sql)
        result = c.fetchone()
        if result != None:
            return result[0]
        else: return False
    except Exception as e:
        #print(str(e))
        return False

def find_existing_score(pid):
    try:
        sql = "SELECT score FROM parent_reply WHERE parent_id = '{}' LIMIT 1".format(pid)
        c.execute(sql)
        result = c.fetchone()
        if result != None:
            return result[0]
        else: return False
    except Exception as e:
        #print(str(e))
        return False
    
if __name__ == '__main__':
    create_table()
    row_counter = 0
    paired_rows = 0

    with codecs.open('{}.txt'.format(timeframe), 'rb',encoding='cp1252' ,buffering=1000) as z: # cp1252
        f = z.read()
        bucket = ''
        row = ''
        rownext = ''
        row_out = ''
        num = 0
        body = ''
        reply = ''
        done = False
        
        for j in range(len(f)): 
        
            
            if f[j] != '\n' and f[j] != '\r':
                bucket += f[j]
                done = False
            else:
                row = bucket[:]
                bucket = ''
                done = True
                row_counter += 1
                parent_id = num 
            
            
            if done:
                pos = 0
                row_in = row.split()
                for i in range(len(row_in)):
                    if row_in[i].endswith('+'):
                        pos = i + 1
                    pass
                row_out = ' '.join(row_in[pos:])
            
                comment_id = 'name-'+str(num)  
                commentnext_id = 'reply-'+ str(num+1)

            created_utc = 0 
            score = 5  
            
            
            subreddit = 0  
            parent_data = False  
            
            
            if done:
                reply  =  str(format_data(row_out))
            
            #reply = str(format_data(rownext_out))
            if done and body == '': body = reply[:]
            
            if acceptable(body) and acceptable(reply) and done :
                done = False
                
                #print(body, '-body-',row_counter)
                #print(reply,'-reply-',row_counter)
                
                sql_insert_complete(comment_id,parent_id,body,reply,subreddit,created_utc,score)
                body = reply[:]

            if done and row_counter % 100000 == 0:
                print('Total Rows Read: {}, Paired Rows: {}, Time: {}'.format(row_counter, paired_rows, str(datetime.now())))

            if done:
                num += 1

    os.system("mv movie_lines.db input.db")
