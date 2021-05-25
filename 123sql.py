import mysql.connector
import datetime
from dbutils.pooled_db import PooledDB
from dbutils.persistent_db import PersistentDB


dbSource = {
    'host': '192.168.70.128',
    'port': 3306,
     # 用户名和密码
    'user': 'root',
    'password': 'checkcheck',
     # 数据库编码
    'charset': 'utf8'
}

test1 = {
    'host': '192.168.70.128',
    'port': 3306,
    'database': 'test1',
     # 用户名和密码
    'user': 'root',
    'password': 'checkcheck',
     # 数据库编码
    'charset': 'utf8'
}

def get_pool(is_mult_thread):
    if is_mult_thread:
        poolDB = PooledDB(
            # 指定数据库连接驱动
            creator=mysql.connector,
            # 连接池允许的最大连接数,0和None表示没有限制
            maxconnections=30,
            # 初始化时,连接池至少创建的空闲连接,0表示不创建
            mincached=10,
            # 连接池中空闲的最多连接数,0和None表示没有限制
            maxcached=30,
            # 连接池中最多共享的连接数量,0和None表示全部共享(其实没什么卵用)
            maxshared=10,
            # 连接池中如果没有可用共享连接后,是否阻塞等待,True表示等等,
            # False表示不等待然后报错
            blocking=True,
            # 开始会话前执行的命令列表
            setsession=[],
            # ping Mysql服务器检查服务是否可用
            ping=0,
            **dbSource)
    else:
        poolDB = PersistentDB(
            # 指定数据库连接驱动
            creator=mysql.connector,
            # 一个连接最大复用次数,0或者None表示没有限制,默认为0
            maxusage=1000,
            **dbSource)
    return poolDB

def get_pool_test1(is_mult_thread):
    if is_mult_thread:
        poolDB = PooledDB(
            # 指定数据库连接驱动
            creator=mysql.connector,
            # 连接池允许的最大连接数,0和None表示没有限制
            maxconnections=30,
            # 初始化时,连接池至少创建的空闲连接,0表示不创建
            mincached=10,
            # 连接池中空闲的最多连接数,0和None表示没有限制
            maxcached=30,
            # 连接池中最多共享的连接数量,0和None表示全部共享(其实没什么卵用)
            maxshared=10,
            # 连接池中如果没有可用共享连接后,是否阻塞等待,True表示等等,
            # False表示不等待然后报错
            blocking=True,
            # 开始会话前执行的命令列表
            setsession=[],
            # ping Mysql服务器检查服务是否可用
            ping=0,
            **test1)
    else:
        poolDB = PersistentDB(
            # 指定数据库连接驱动
            creator=mysql.connector,
            # 一个连接最大复用次数,0或者None表示没有限制,默认为0
            maxusage=1000,
            **test1)
    return poolDB

db_pool_root = get_pool(False)
# 从数据库连接池中取出一条连接
conn = db_pool_root.connection()
cursor = conn.cursor()
# 随便查一下吧
cursor.execute('show databases')
# 随便取一条查询结果
result = cursor.fetchall()
# print(result)
conn.close()

# mydb = mysql.connector.connect(
#     host="192.168.70.128",  # 数据库主机地址
#     user="root",  # 数据库用户名
#     passwd="checkcheck",  # 数据库密码
#
# )
#
# test1 = mysql.connector.connect(
#     host="192.168.70.128",  # 数据库主机地址
#     user="root",  # 数据库用户名
#     passwd="checkcheck",  # 数据库密码
#     database="test1"
#
# )
#
# mydb2 = mysql.connector.connect(
#     host="192.168.70.128",  # 数据库主机地址
#     user="root",  # 数据库用户名
#     passwd="checkcheck",  # 数据库密码
#     database="test2"
#
# )

# mycursor = mydb.cursor()
# mycursor1 = mydb1.cursor()
# mycursor2 = mydb2.cursor()

# mycursor1.execute("SHOW tables")
# myresult = mycursor1.fetchall()
# cursor.excute("SHOW database")
# dbs_res = cursor.fetchall
# print(dbs_res)
db_pool_test1 = get_pool_test1(False)
conn_test1 = db_pool_test1.connection()
cursor1 = conn_test1.cursor()
# 随便查一下吧
cursor1.execute('show tables')
res_test1 = cursor1.fetchall()
# print(res_test1)
conn_test1.close()


# 1. 获取「今天」
today = datetime.date.today()
# newyearday = datetime.datetime.strptime('2021-01-01', '%Y-%m-%d')
# 2. 获取当前月的第一天
first = today.replace(day=1)
# 3. 减一天，得到上个月的最后一天
last_month = first - datetime.timedelta(days=1)
# 4. 格式化成指定形式
# print(last_month.strftime("%Y-%m-%d"))

first_lastmonth = last_month.replace(day=1)
last_month_two = first_lastmonth - datetime.timedelta(days=1)
# print(myresult)
#


for x in res_test1:
    part_sql_1 = "select * from %s" % (x)
    select_sql = part_sql_1 + " where create_time <= %(createtime)s"
    cursor1.execute(select_sql, {'createtime': last_month_two})
    data_myresults = cursor1.fetchall()
    conn_test1.close()
    # print(data_myresults)

    for y in data_myresults:
        # print(y[14])
        # # insert_sql = "insert into %s %s" %(x[0],y[0])
        if len(str(y[21])) == 1:

            db_name = "%s" % y[20] + "0%d" % y[21]
            # mydb = mysql.connector.connect(
            #     host="192.168.70.128",  # 数据库主机地址
            #     user="root",  # 数据库用户名
            #     passwd="checkcheck",  # 数据库密码
            #
            # )
            # mycursor = mydb.cursor()
            # create_db_sql = "CREATE DATABASE IF NOT EXISTS `%s` default CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_general_ci" % db_name
            # mycursor.execute(create_db_sql)
            # mydb.commit()
            create_db_sql = "CREATE DATABASE IF NOT EXISTS `%s` default CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_general_ci" % db_name
            conn = db_pool_root.connection()
            cursor = conn.cursor()
            # 随便查一下吧
            cursor.execute(create_db_sql)
            conn.commit()
            # print(create_db_sql)

            for tb_name in res_test1:
                # mydb = mysql.connector.connect(
                #     host="192.168.70.128",  # 数据库主机地址
                #     user="root",  # 数据库用户名
                #     passwd="checkcheck",  # 数据库密码
                #     database=db_name,
                #
                # )

                create_table_sql = "CREATE TABLE IF NOT EXISTS `%s`.`%s` (`id` bigint(20) NOT NULL COMMENT 'id', \
                                `thirdparty_id` varchar(64) NOT NULL COMMENT '三方ID', \
                                `thirdparty_platform` varchar(32) NOT NULL COMMENT '所属平台', \
                                `thirdparty_module` varchar(32) NOT NULL COMMENT '所属模块', \
                                `user_id` bigint(20) NOT NULL COMMENT '会员ID', \
                                `useraccount` varchar(32) NOT NULL DEFAULT '' COMMENT '会员账号', \
                                `valid_bet_amount` bigint(20) NOT NULL COMMENT '有效投注', \
                                `bet_amount` bigint(20) NOT NULL COMMENT '下注金额', \
                                `settle_amount` bigint(20) NOT NULL COMMENT '结算金额', \
                                `payment_amount` bigint(20) NOT NULL COMMENT '盈亏金额', \
                                `is_settle` tinyint(4) NOT NULL DEFAULT '0' COMMENT '是否结算', \
                                `create_time` datetime NOT NULL COMMENT '注单时间', \
                                `insert_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间', \
                                `is_chb` tinyint(4) NOT NULL DEFAULT '0' COMMENT '是否结算打码量', \
                                `chb_time` datetime DEFAULT NULL COMMENT '打码量结算时间', \
                                `game_name` varchar(50) DEFAULT NULL COMMENT '游戏名称', \
                                `real_account` varchar(50) DEFAULT NULL COMMENT '真人账号', \
                                `game_type` varchar(20) DEFAULT NULL COMMENT '游戏类型', \
                                `game_code` varchar(20) DEFAULT NULL COMMENT '游戏编码', \
                                `record_details` text COMMENT '游戏记录详情', \
                                `year` int(11) DEFAULT '0' COMMENT '年', \
                                `month` int(11) DEFAULT '0' COMMENT '月', \
                                `day` int(11) DEFAULT '0' COMMENT '天', \
                                PRIMARY KEY (`id`,`thirdparty_platform`) USING BTREE, \
                                UNIQUE KEY `unp_tp_id` (`thirdparty_id`,`thirdparty_platform`), \
                                KEY `create_time_index` (`create_time`), \
                                KEY `idx_game_name` (`game_name`), \
                                KEY `idx_user_gametype` (`game_type`,`useraccount`), \
                                KEY `idx_useraccount` (`useraccount`), \
                                KEY `id_platform_idx` (`thirdparty_id`,`thirdparty_platform`,`user_id`), \
                                KEY `id_platform_month_day_idx` (`thirdparty_id`,`thirdparty_platform`,`month`,`day`), \
                                KEY `type_module_idx` (`game_type`,`thirdparty_module`) \
                                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC COMMENT='三方游戏记录'" % (db_name,tb_name[0])
                # mycursor = mydb.cursor()
                # mycursor.execute(create_table_sql)
                # print(create_table_sql)
                # mydb.commit()
                # mydb.close()

                # 随便查一下吧
                cursor.execute(create_table_sql)
                conn.commit()
                # print(create_table_sql)
                # conn.close()
                insert_part_sql1 = "replace into `%s`.`%s`" % (db_name,tb_name[0])
                insert_sql = insert_part_sql1 + "(`id`,`thirdparty_id`,`thirdparty_platform`,`thirdparty_module`," \
                                                "`user_id`,`useraccount`,`valid_bet_amount`,`bet_amount`," \
                                                "`settle_amount`,`payment_amount`,`is_settle`,`create_time`," \
                                                "`insert_time`,`is_chb`,`chb_time`,`game_name`,`real_account`," \
                                                "`game_type`,`game_code`,`record_details`,`year`,`month`," \
                                                "`day`)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
                                                "%s,%s,%s,%s,%s,%s,%s,%s,%s)" \
                    # % (y[0], y[1], y[2], y[3], y[4], y[5], y[6], y[7], y[8], y[9], y[10], y[11], y[12], y[13],
                #     y[14], y[15], y[16], y[17], y[18], y[19], y[20], y[21], y[22])
                # print(insert_sql)

                cursor.execute(insert_sql, (
                y[0], y[1], y[2], y[3], y[4], y[5], y[6], y[7], y[8], y[9], y[10], y[11], y[12], y[13],
                y[14], y[15], y[16], y[17], y[18], y[19], y[20], y[21], y[22]))

                conn.commit()
                conn.close()
    for y in data_myresults:
        if len(str(y[21])) == 2:
            db_name = "%s" % y[20] + "%d" % y[21]
            create_db_sql = "CREATE DATABASE IF NOT EXISTS `%s` default CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_general_ci" % (
                db_name)
            # mycursor = mydb.cursor()
            # mycursor.execute(create_db_sql)
            # mydb.commit()
            conn = db_pool_root.connection()
            cursor = conn.cursor()
            # 随便查一下吧
            cursor.execute(create_db_sql)
            conn.commit()

            for tb_name in res_test1:
                # mydb = mysql.connector.connect(
                #     host="192.168.70.128",  # 数据库主机地址
                #     user="root",  # 数据库用户名
                #     passwd="checkcheck",  # 数据库密码
                #     port="3306",
                #     database=db_name,
                #
                # )

                create_table_sql = "CREATE TABLE IF NOT EXISTS `%s`.`%s` (`id` bigint(20) NOT NULL COMMENT 'id', \
                                `thirdparty_id` varchar(64) NOT NULL COMMENT '三方ID', \
                                `thirdparty_platform` varchar(32) NOT NULL COMMENT '所属平台', \
                                `thirdparty_module` varchar(32) NOT NULL COMMENT '所属模块', \
                                `user_id` bigint(20) NOT NULL COMMENT '会员ID', \
                                `useraccount` varchar(32) NOT NULL DEFAULT '' COMMENT '会员账号', \
                                `valid_bet_amount` bigint(20) NOT NULL COMMENT '有效投注', \
                                `bet_amount` bigint(20) NOT NULL COMMENT '下注金额', \
                                `settle_amount` bigint(20) NOT NULL COMMENT '结算金额', \
                                `payment_amount` bigint(20) NOT NULL COMMENT '盈亏金额', \
                                `is_settle` tinyint(4) NOT NULL DEFAULT '0' COMMENT '是否结算', \
                                `create_time` datetime NOT NULL COMMENT '注单时间', \
                                `insert_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间', \
                                `is_chb` tinyint(4) NOT NULL DEFAULT '0' COMMENT '是否结算打码量', \
                                `chb_time` datetime DEFAULT NULL COMMENT '打码量结算时间', \
                                `game_name` varchar(50) DEFAULT NULL COMMENT '游戏名称', \
                                `real_account` varchar(50) DEFAULT NULL COMMENT '真人账号', \
                                `game_type` varchar(20) DEFAULT NULL COMMENT '游戏类型', \
                                `game_code` varchar(20) DEFAULT NULL COMMENT '游戏编码', \
                                `record_details` text COMMENT '游戏记录详情', \
                                `year` int(11) DEFAULT '0' COMMENT '年', \
                                `month` int(11) DEFAULT '0' COMMENT '月', \
                                `day` int(11) DEFAULT '0' COMMENT '天', \
                                PRIMARY KEY (`id`,`thirdparty_platform`) USING BTREE, \
                                UNIQUE KEY `unp_tp_id` (`thirdparty_id`,`thirdparty_platform`), \
                                KEY `create_time_index` (`create_time`), \
                                KEY `idx_game_name` (`game_name`), \
                                KEY `idx_user_gametype` (`game_type`,`useraccount`), \
                                KEY `idx_useraccount` (`useraccount`), \
                                KEY `id_platform_idx` (`thirdparty_id`,`thirdparty_platform`,`user_id`), \
                                KEY `id_platform_month_day_idx` (`thirdparty_id`,`thirdparty_platform`,`month`,`day`), \
                                KEY `type_module_idx` (`game_type`,`thirdparty_module`) \
                                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC COMMENT='三方游戏记录'" % (db_name,tb_name[0])
                # mycursor = mydb.cursor()
                # mycursor.execute(create_table_sql)
                # mydb.commit()
                cursor.execute(create_table_sql)
                conn.commit()
                # print(create_table_sql)
                conn.close()


#
#
# for x in myresult:
#
#     part_sql_1 = "select * from %s" % (x)
#     select_sql = part_sql_1 + " where create_time <= %(createtime)s"
#     mycursor1.execute(select_sql, {'createtime': last_month_two})
#     data_myresults = mycursor1.fetchall()
#     for y in data_myresults:
#
#         for tb_name in myresult:
#             mydb = mysql.connector.connect(
#                 host="192.168.70.128",  # 数据库主机地址
#                 user="root",  # 数据库用户名
#                 passwd="checkcheck",  # 数据库密码
#                 port="3306",
#                 database=db_name,
#
#             )
#             insert_part_sql1 = "replace into %s" % x
#             insert_sql = insert_part_sql1 + "(`id`,`thirdparty_id`,`thirdparty_platform`,`thirdparty_module`," \
#                                             "`user_id`,`useraccount`,`valid_bet_amount`,`bet_amount`," \
#                                             "`settle_amount`,`payment_amount`,`is_settle`,`create_time`," \
#                                             "`insert_time`,`is_chb`,`chb_time`,`game_name`,`real_account`," \
#                                             "`game_type`,`game_code`,`record_details`,`year`,`month`," \
#                                             "`day`)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
#                                             "%s,%s,%s,%s,%s,%s,%s,%s,%s)" \
#                                             # % (y[0], y[1], y[2], y[3], y[4], y[5], y[6], y[7], y[8], y[9], y[10], y[11], y[12], y[13],
#                                             #     y[14], y[15], y[16], y[17], y[18], y[19], y[20], y[21], y[22])
#             # print(insert_sql)
#             mycursor = mydb.cursor()
#             mycursor.execute(insert_sql, (y[0], y[1], y[2], y[3], y[4], y[5], y[6], y[7], y[8], y[9], y[10], y[11], y[12], y[13],
#                                                 y[14], y[15], y[16], y[17], y[18], y[19], y[20], y[21], y[22]))
#             mydb.commit()

    # part_sql_del = "delete from %s" % (x)
    # delete_sql = part_sql_del + " where create_time <= %(createtime)s"
    # mycursor1.execute(delete_sql, {'createtime': last_month_two})
    # print(delete_sql)
    # mydb1.commit()
