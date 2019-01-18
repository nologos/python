import os
import pymysql

ca = os.path.expanduser("~/Certificates/BaltimoreCyberTrustRoot.crt.pem")
ssl = {'ca':ca, 'check_hostname':True}

cnx = pymysql.connect(user="administratorr@people1", password='S123523DsaqdAS1D5236fdwDOKOeqweqPAq!wecKSDAPOJK', host="people1.mysql.database.azure.com", port=3306, database='people2', ssl=ssl)

cur_new=cnx.cursor()
cur= cnx.cursor()
cur2= cnx.cursor()

cur_new.execute("use new")
cur_new.execute("create table tt("
                "ID VARCHAR(20)"
                "PRIMARY KEY ID"
                ")")

query1 = "select * from connectionproperties"
cur.execute(query1)
asd =cur.execute(query1)
cur2.execute("""
show tables;
""")
print(cur.fetchmany())
print(asd)

asd2 =cur.execute("show databases;")
print(asd2)

for row in cur.fetchall():
    print(row)
cur.execute("use people2;")
cur.execute("show tables;")
print("printing tables")
print(cur.fetchall())
cur.execute("select * from connectionproperties;")
print(cur.fetchall())

print("printing cur2")
print(cur2.fetchall())

cnx.close()
