"""
处理mysql的操作
连接数据库
游标的创建

数据的提取：所有，单条，条数
数据库的修改： update
数据库的关闭：
"""
import pymysql
from Test.Interface.Common.handle_config import conf
class HandleMysql():

    def __init__(self):
        #连接数据库
        self.conn=pymysql.connect(
            host=conf.get('mysql','host'),
            port=conf.getint('mysql','port'),
            user=conf.get('mysql','user'),
            password=conf.get('mysql','password'),
            db=conf.get('mysql','db'),
            charset=conf.get('mysql','charset'),
        )
        #创建游标对象
        self.cursor=self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def select_all_data(self,sql):
        """
        获取所有的数据
        :param sql: sql语句
        :return: 所有值   [{}]
        """
        #执行sql语句
        self.cursor.execute(sql)
        self.conn.commit()
        #通过游标取所有值
        data=self.cursor.fetchall()
        #返回值
        return data

    def select_one_data(self,sql):
        """
        获取单条数据
        :param sql: sql语句
        :return: 所有值   [{}]
        """
        #执行sql语句
        self.cursor.execute(sql)
        self.conn.commit()
        #通过游标取单个值
        data=self.cursor.fetchone()
        #返回值
        return data

    def get_count(self,sql):
        """
              获取条数
              :param sql: sql语句
              :return: 条数  int
              """
        # 执行sql语句
        res=self.cursor.execute(sql)
        self.conn.commit()
        return res

    def  update(self,sql):
        self.cursor.execute(sql)
        self.conn.commit()


    def close(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    db=HandleMysql()
    sql = 'select `name` ,`age` from `keen_api` where `status`=1 and id={} '.format(1094)
    data = db.select_all_data(sql)
    print(data)