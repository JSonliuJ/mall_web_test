# -- encoding: utf-8 --
# @time:    	2021/10/11 22:12
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import time

import pymysql
import sys

class MySQLHandler:

    def __init__(self, host=None,
                 port=3306,
                 user=None,
                 password=None,
                 database=None, **kwargs):
        self.conn = pymysql.connect(host=host,
                                    port=port,
                                    user=user,
                                    password=password,
                                    database=database, **kwargs)
        # 初始化游标
        self.cursor = self.conn.cursor()

    def query_all(self, sql):
        """查询所有的记录.
        游标对象最好不要用多次，用完关掉，下次再初始化。
        """
        self.cursor.execute(sql)
        self.conn.commit()
        records = self.cursor.fetchall()
        return records

    def query_one(self, sql):
        """查询一条记录"""
        # 提交事务
        self.cursor.execute(sql)
        self.conn.commit()
        record = self.cursor.fetchone()
        return record

    def select_sql(self, sql, args=None, one=True):
        # 查询 select 字段名 from 表名 where 条件;
        print("sql:",sql)
        for i in range(3):
            self.cursor.execute(sql, args)
            # TODO: 提交事务(数据同步)
            self.conn.commit()
            if one:
                one_data = self.cursor.fetchone()
                if one_data:
                    return one_data
                else:
                    time.sleep(10)
            else:
                all_data = self.cursor.fetchall()
                if all_data:
                    return all_data
                else:
                    time.sleep(10)
        else:
            sys.exit('sql：{}没有查询到数据'.format(sql))


    def close(self):
        """关闭连接"""
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    from TestDatas.Common_datas import Config as cf
    my_db = MySQLHandler(**cf.db)
    iphone = 18593298790
    sql = f"SELECT mobile_code FROM tz_sms_log WHERE user_phone = '%s' ORDER BY rec_date DESC" % iphone
    code = my_db.query_one(sql)
    print("code", code)
    my_db.close()