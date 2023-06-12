import sqlite3
import os
import glob

def execute_query(sql: str) -> list:
    with sqlite3.connect('school.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
    
if __name__ == '__main__':
    for query_sql_file in glob.glob('query_*.sql')[-1:]:
        print(query_sql_file)
        with open(query_sql_file, 'r') as f:
            sql_query = f.read()
        print(execute_query(sql_query))