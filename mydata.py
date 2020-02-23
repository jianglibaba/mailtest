import pymysql
import pandas as pd
#import os

class Tools():

    # 获取数据库的数据
    @staticmethod
    def getData():
        # 打开数据库连接
        connect = pymysql.connect(host='192.168.1.137',port=3306,user='mail_user',password='ah7032',database='mail_db')
        # 使用cursor()方法创建一个游标对象c
        c = connect.cursor()
        # 使用execute()方法执行SQL语句
        c.execute("SELECT * FROM users")
        # 获取所有记录列表
        data = c.fetchall()

        data_list = []
        for row in data:
            temp_list = []
            temp_list.append(row[0])
            temp_list.append(row[1])
            temp_list.append(row[2])
            temp_list.append(row[3])
            data_list.append(temp_list)
        connect.close()
        return data_list

    # 新增数据的数据库操作
    @staticmethod
    def addData(account, pwd, comment):
        connect = pymysql.connect(host='192.168.1.137',port=3306,user='mail_user',password='ah7032',database='mail_db')
        c = connect.cursor()
        command = "insert into users values(null,'%s','%s','%s')" % (account, pwd, comment)
        c.execute(command)
        connect.commit()
        connect.close()

    # 删除数据的数据库操作
    @staticmethod
    def delData(id):
        connect = pymysql.connect("192.168.1.137", "mail_user", "ah7032", 'mail_db')
        c = connect.cursor()
        command = "delete from users where id = %s" % id
        c.execute(command)
        connect.commit()
        connect.close()

     # 编辑数据的数据库操作（设comment为0，暂停账户）
    @staticmethod
    def pauseData(id):
        connect = pymysql.connect("192.168.1.137", "mail_user", "ah7032", 'mail_db')
        c = connect.cursor()
        command = "update users set comment = 0 where id = %s" % id
        c.execute(command)
        connect.commit()
        connect.close()

    # 保存为csv文件
    @staticmethod
    def saveData():
            connect = pymysql.connect("192.168.1.137", "mail_user", "ah7032", 'mail_db')
            command = "SELECT * FROM users"

            df = pd.read_sql(command, con=connect)
            df.to_csv("data.csv")
            connect.close()

    #修改密码
    @staticmethod
    def changepwd(id,newwpwd):
        connect = pymysql.connect("192.168.1.137", "mail_user", "ah7032", 'mail_db')
        c = connect.cursor()
        command = "update users set password = %s where id = %s" % (newwpwd,id)
        c.execute(command)
        connect.commit()
        connect.close()



