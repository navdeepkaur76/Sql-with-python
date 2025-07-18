import pymysql
import pymysql.cursors
conn= pymysql.connect(host='localhost',user='root',db='happy')
a=conn.cursor()

sql = """CREATE TABLE SMILE (
        EMP_NO INT,
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
a.execute(sql)
conn.commit()
a.close()
conn.close()

