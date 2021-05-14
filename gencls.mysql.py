import os
import sys
import mysql.connector
from pathlib import Path
from classes.Column import Column
from classes.JavaClass import JavaClass

def main():
    DB_NAME = "db_name"
    DB_HOST = "localhost"
    DB_USER = "root"
    DB_PASS = ""

    PACKAGE_NAME = "com.project.model;"
    file_path = sys.modules[__name__].__file__
    project_path = os.path.dirname(file_path)
    OUTPUT_PATH = os.path.join(project_path, "output")
    Path(OUTPUT_PATH).mkdir(parents=True, exist_ok=True)

    MESSAGE_PROCESSING = "Processing table "
    QUERY_GET_TABLES = "SELECT table_name FROM information_schema.tables WHERE table_type = 'base table' " \
                       "AND table_schema='" + DB_NAME + "';"

    QUERY_GET_COLUMNS = "SELECT * FROM information_schema.columns WHERE table_schema='" + DB_NAME + "' " \
                        "AND TABLE_NAME='%s';"

    dbCon = mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        password = DB_PASS,
        database = DB_NAME
    )
    cursor = dbCon.cursor()
    # Get tables
    cursor.execute(QUERY_GET_TABLES)
    tableNames = cursor.fetchall()

    for tableName_raw in tableNames:
        tableName = tableName_raw[0]
        columns = []
        print(MESSAGE_PROCESSING + tableName)
        cursor.execute(QUERY_GET_COLUMNS % tableName)
        rawColumns = cursor.fetchall()
        for rawColumn in rawColumns:
            print(rawColumn)
            column = Column(rawColumn[3], rawColumn[7], True if rawColumn[15] == 'PRI' else False)
            columns.append(column)
        javaClass = JavaClass(tableName,columns,PACKAGE_NAME)
        javaClass.createJavaFile(OUTPUT_PATH)
    cursor.close()
    dbCon.close()



if __name__ == '__main__':
    sys.exit(main())