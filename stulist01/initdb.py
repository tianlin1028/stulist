#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

from dbconn import db_cursor

def create_db():
    sqlstr = """
    DROP TABLE IF EXISTS course;

    CREATE TABLE IF NOT EXISTS course  (
        cou_sn   INTEGER,     --序号
        cou_no   TEXT,        --学号
        name     TEXT,        --姓名
        pice     TEXT,        --出生日期
        sex      TEXT,        --性别
        notes    TEXT,        --班级
        PRIMARY KEY(cou_sn)
    );
    -- CREATE UNIQUE INDEX idx_course_no ON course(cou_no);

    CREATE SEQUENCE seq_cou_sn 
        START 10000 INCREMENT 1 OWNED BY course.cou_sn;

    """
    with db_cursor() as cur :
        cur.execute(sqlstr) # 执行SQL语句
    
def init_data():
    sqlstr = """
    DELETE FROM course;

    INSERT INTO course (cou_sn, cou_no, name, pice, sex, notes)  VALUES 
        (101, '1310650303',  '王  治', '1994年06月', '男', '信息1303'),
        (102, '1310650312',  '安鹏旭', '1995年01月', '男', '信息1303'),
        (103, '1310650215',  '杨文妹', '1992年06月', '女', '信息1302'),
        (104, '1310650425',  '魏筱霖', '1994年10月', '女', '信息1304'),
        (105, '1310650120',  '王  月', '1995年08月', '女', '信息1301');

    """
    with db_cursor() as cur :
        cur.execute(sqlstr)    

if __name__ == '__main__':
    create_db()
    init_data()
    print('数据库已初始化完毕！')

