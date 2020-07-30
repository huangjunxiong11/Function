import MySQLdb

"""
只需更改对应的数据库ip、端口、账号、密码、数据库名词、sql语句即可
前提是需要自己熟练掌握数据库的语法和语句
        :param str host:        host to connect
        :param str user:        user to connect as
        :param str password:    password to use
        :param str passwd:      alias of password, for backward compatibility
        :param str database:    database to use
        :param str db:          alias of database, for backward compatibility
        :param int port:        TCP/IP port to connect to
# 测试线数据库配置
# HOST = "192.168.1.16"
# PORT = "4737"
# USER = "dev"
# PASSWORD = "dev@gzfsnet.com"
# DB = "adsys"
# 正式线配置
HOST = "192.168.8.105"
PORT = "4737"
USER = "fsaduser"
PASSWORD = "FSzh201622@$*"
DB = "adsys"
"""


class MysqlDb(object):
    def __init__(self):
        pass

    @property
    def connect_db(self):
        """
        连接本地mysql数据库
        :return:
        """
        db = MySQLdb.connect(host='192.168.8.105', port=4737, user="fsaduser", password="FSzh201622@$*", db="adsys",
                             charset='utf8')
        # cursor = db.cursor()
        # cursor.execute("SELECT VERSION()")
        # data = cursor.fetchone()
        # print(data)
        # db.close()
        pass
        return db

    def create_table(self):
        """
        创建数据库中的表
        :return:
        """
        # 打开数据库连接
        db = self.connect_db

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 创建数据表SQL语句
        sql = """CREATE TABLE EMPLOYEE (
                 FIRST_NAME  CHAR(20) NOT NULL,
                 LAST_NAME  CHAR(20),
                 AGE INT,  
                 SEX CHAR(1),
                 INCOME FLOAT )"""
        cursor.execute(sql)

        # 关闭数据库连接
        db.close()

    def insert_into(self):
        """
        向数据表插入写入数据
        :return:
        """

        # 打开数据库连接
        db = self.connect_db
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
                 LAST_NAME, AGE, SEX, INCOME)
                 VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()
        # 关闭数据库连接
        db.close()

    def fetch_all(self):
        """
        从数据表中查询所有数据
        :return:
        """

        # 打开数据库连接
        db = self.connect_db
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = "SELECT * FROM EMPLOYEE \
               WHERE INCOME > %s" % (1000)  # sql语句插入变量
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                fname = row[0]
                lname = row[1]
                age = row[2]
                sex = row[3]
                income = row[4]
                # 打印结果
                print(
                    "fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
                    (fname, lname, age, sex, income))
        except:
            print(
                "Error: unable to fecth data")

        # 关闭数据库连接
        db.close()

    def update_db(self):
        """
        更新数据库表中的数据
        :return:
        """
        # 打开数据库连接
        db = self.connect_db
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 更新语句
        sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()

        # 关闭数据库连接
        db.close()

    def delete_db(self):
        """
        删除数据库中的数据
        :return:
        """
        # 打开数据库连接
        db = self.connect_db
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 删除语句
        sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交修改
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()

        # 关闭连接
        db.close()

# mysqldb = MysqlDb()
# aa = mysqldb.connect_db
