from pymysql import connect

db=connect(host="127.0.0.1",user="root",password="123456",db="test",port=3306,charset="utf8")
cur=db.cursor()
sql="select * from student where iD>1 or score>90 limit %d offset %d"
cur.execute(sql)
result=cur.fetchmany(3)
for row in result:
    id=row[0]
    name=row[1]
    print(id,name)
cur.close()
db.close()