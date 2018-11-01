#!/usr/bin/python3

from psycopg2 import connect
try:
    con = connect(
    'host=localhost dbname=projeto user=admin password=4linux'
    )
    cur = con.cursor()
except Exception as e:
    print('ERRO:{}'.format(e))
    exit()

#cur.execute("select * from produtos;")
cur.execute("select * from produtos where preco between '5' and '2000';")
print (cur.fetchall())

#cur.execute("insert into produtos(nome, preco,quantidade)values('video game', 1500, 5);")
#con.commit()

cur.close()
con.close()