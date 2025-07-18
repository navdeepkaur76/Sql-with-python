import pymysql
import pymysql.cursors
conn= pymysql.connect(host='localhost',user='root')
a=conn.cursor()
sql="Create database happy"
a.execute(sql)
conn.commit()
a.close()
conn.close()
