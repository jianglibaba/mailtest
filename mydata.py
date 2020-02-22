import pymysql

#import pandas as pd
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

    # 删除数据的数据库操作
    @staticmethod
    def delData():
        # 打开数据库连接
        connect = pymysql.connect("192.168.1.137", "mail_user", "ah7032", 'mail_db')
        # 使用cursor()方法创建一个游标对象c
        c = connect.cursor()
        # 使用execute()方法执行SQL语句


        command = "delete from mydata where id = 1"
        c.execute(command)
        connect.commit()
        connect.close()



