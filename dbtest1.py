import pymysql,pandas as pd

class StudentDao:

    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='test1234', db='my_db', charset='utf8')
        self.curs = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def getList(self):
        col = []
        ret = []
        sql = "select * from student order by _id desc"
        try:
            self.curs.execute(sql)
            rows = self.curs.fetchall()
            for e in rows:
                temp = {'_id':e[0],'name':e[1],'belong':e[2],'phone':e[3] }
                ret.append(temp)

            colname = self.curs.description
            for i in colname:
                col.append(i[0])

            emp = pd.DataFrame(list(rows), columns=col)

            print(emp[['_id','name','belong','phone']])
        except Exception as e:
            print(e)
        finally:
            print("조회완료")
            
        return ret
    
    def insStuInfo(self):

        sql = "insert into student values(%s, %s, %s, %s, %s)"
        self.curs.execute(sql, ('30000010', '마르치스','IDE','01033333333', 1))
        self.conn.commit()


    def upStuInfo(self):
        sql = "update student set name=%s, belong=%s where _id=%s"
        self.curs.execute(sql, ('장군이','CSE','30000010'))
        self.conn.commit()

    def delStuInfo(self):
        sql = "delete from student where _id=%s"
        self.curs.execute(sql, ('30000000'))
        self.conn.commit()



if __name__ == '__main__':
    #StudentDao().insStuInfo()
    #StudentDao().upStuInfo()
    #StudentDao().delStuInfo()
    
    emplist = StudentDao().getList()
    print(emplist)
