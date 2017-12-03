#1
import pymysql
def connDb():
    #我们要想联接数据库,需要知道数据库的哪些信息:
    #iP地址 ,端口号,用户名和密码
    pymysql.Connect( host="172.0.0.1", user="root", password="root",database="pirate", port=3306, charset='utf8')
    #按住connect +ctrl ,进入后再次点击Connection
    #查询user表中所有的数据,并且倒叙打印
    sql = "selcet * from hd_user order by id desc"
    curs = conn.cursor()
    curs.exeute(sql)
    result = curs.fetchone()
   # result = curs.fetchall()
    if __name__ == '__main__':
        print(connDb())





