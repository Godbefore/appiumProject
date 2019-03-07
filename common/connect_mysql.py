from pymysql import connect
# 未完成
def get_from_mysql(d=1):
    db=connect(host="127.0.0.1",user="root",password="123456",db="test",port=3306,charset="utf8")
    cur=db.cursor()
    sql="select * from user where ID=%s"%d
    cur.execute(sql)
    result=cur.fetchmany(1)
    id=result[0]
    name=result[1]
    password=result[2]
    cur.close()
    db.close()
    return id,name,password