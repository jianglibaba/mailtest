import pymysql
import pandas as pd
#import os

class Tools():


    # 获取数据库的数据
    @staticmethod
    def getData():
        # 打开数据库连接
        connect = pymysql.connect(host='192.168.2.6',port=3306,user='xxx',password='hfDSt130-=',database='mail')
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
            temp_list.append(row[4])
            data_list.append(temp_list)
        connect.close()
        return data_list

    #获取暂停账号的行数的列表
    @staticmethod
    def redData():
        # 打开数据库连接
        connect = pymysql.connect(host='192.168.2.6', port=3306, user='xxx', password='hfDSt130-=', database='mail')
        # 使用cursor()方法创建一个游标对象c
        c = connect.cursor()
        # 使用execute()方法执行SQL语句
        c.execute("SELECT * FROM users")
        # 获取所有记录列表
        data = c.fetchall()

        data_list = []
        row_list = []
        for row in data:
            temp_list = []
            temp_list.append(row[0])
            temp_list.append(row[1])
            temp_list.append(row[2])
            temp_list.append(row[3])
            temp_list.append(row[4])
            data_list.append(temp_list)


        for team in data_list:
            if team[2] == 0:
                row_id = data_list.index(team)
                row_list.append(row_id)

        connect.close()
        return row_list



    # 新增数据的数据库操作
    @staticmethod
    def addData(account, pwd, comment, dep, who):
        connect = pymysql.connect(host='192.168.2.6',port=3306,user='xxx',password='hfDSt130-=',database='mail')
        c = connect.cursor()
        command = "insert into users values('%s','%s','%s','%s','%s')" % (account, pwd, comment, dep, who)
        c.execute(command)
        connect.commit()
        connect.close()

    # 删除数据的数据库操作
    @staticmethod
    def delData(id):
        connect = pymysql.connect(host='192.168.2.6',port=3306,user='xxx',password='hfDSt130-=',database='mail')
        c = connect.cursor()
        command = 'delete from users where email = "%s"' % id
        c.execute(command)
        connect.commit()
        connect.close()

    # 编辑数据的数据库操作（设comment为0，暂停账户）
    @staticmethod
    def pauseData(id):
        connect = pymysql.connect(host='192.168.2.6',port=3306,user='xxx',password='hfDSt130-=',database='mail')
        c = connect.cursor()
        command = 'update users set enable = 0 where email = "%s"' % id
        c.execute(command)
        connect.commit()
        connect.close()

    # 编辑数据的数据库操作（设comment为1，启用账户）
    @staticmethod
    def enableData(id):
        connect = pymysql.connect(host='192.168.2.6', port=3306, user='xxx', password='hfDSt130-=', database='mail')
        c = connect.cursor()
        command = 'update users set enable = 1 where email = "%s"' % id
        c.execute(command)
        connect.commit()
        connect.close()

    # 保存为csv文件
    @staticmethod
    def saveData():
            connect = pymysql.connect(host='192.168.2.6',port=3306,user='xxx',password='hfDSt130-=',database='mail')

            # 使用cursor()方法创建一个游标对象c
            c = connect.cursor()
            # 使用execute()方法执行SQL语句
            c.execute("SELECT remark,email FROM users")
            # 获取所有记录列表
            data = c.fetchall()

            one_list = []
            two_list = []
            three_list = []
            for row in data:

                one_list.append(row[0])
                two_list.append(row[1])
                three_list.append(-9220000000000000000)

            data = {'姓名': one_list, 'email': two_list, 'foxmail': three_list}
            data_df = pd.DataFrame(data)
            # index表示设定是否需要行索引，设定为FALSE表明不需要，就不会生成新的行索引
            # header表明是否需要列索引，设定为True（默认设置）表明需要，那么之前df的列标签就会保存。
            data_df.to_csv('data_df.csv',index=False,header=True)

            connect.close()

    #修改密码
    @staticmethod
    def changepwd(id,newwpwd):
        connect = pymysql.connect(host='192.168.2.6',port=3306,user='xxx',password='hfDSt130-=',database='mail')
        c = connect.cursor()
        command = 'update users set password = "%s" where email = "%s"' % (newwpwd,id)
        c.execute(command)
        connect.commit()
        connect.close()


t=Tools()
Tools.saveData()
