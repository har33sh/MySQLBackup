import MySQLdb
from datetime import date, timedelta
import os
from config import tables,host, user, passwd, db


def write_sql (dbs,host,user,passwd,db,tables):

    db = MySQLdb.connect(host, user, passwd, db)
    yesterday = (date.today() - timedelta(1)).strftime('%Y-%m-%d')

    for table in tables :
        cursor = db.cursor()
        #check if ts or timestamp is used for storing the timestamp in the table
        sql = "DESC "+table
        try:
            cursor.execute(sql)
        except:
            print sql + " error in executing"
            continue

        timestamp_in_table_flag = 0

        for row in cursor:
            column_name = row[0]

            if column_name == 'timestamp':
                fieldname = 'timestamp'
                column_type = row[1]
                print column_type
                timestamp_in_table_flag = 1
                break

            elif column_name == 'ts':
                fieldname = 'ts'
                column_type = row[1]
                timestamp_in_table_flag = 1
                break

        if timestamp_in_table_flag == 0:
            continue

        if column_type == 'timestamp':
            sql = "SELECT * FROM " + table+ " where "+ fieldname + " like "+ "'"+ yesterday+"%" + "'"

        elif 'int' in column_type:
            sql = "SELECT * FROM " + table+ " where from_unixtime("+ fieldname + ") like "+ "'"+ yesterday+"%" + "'"

        file_writer = open("./"+dbs+"/"+table+".sql", "a+")

        try:
            cursor.execute(sql)

        except:
            print "Error in Executing: "+sql
            continue

        for row in cursor:
            row_value="("
            for r in range(len(row)):
                if r==len(row)-1:
                    row_value=row_value+"'"+str(row[r])+"'"
                else:
                    row_value=row_value+"'"+str(row[r])+"',"
            row_value=row_value+")"
            print>>file_writer,row_value
        file_writer.close()

    db.close()
