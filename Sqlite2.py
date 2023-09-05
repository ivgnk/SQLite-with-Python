'''
2017 Python: Работа с базой данных, часть 1/2: Используем DB-API
https://habr.com/ru/articles/321510/

Данные из https://github.com/lerocha/chinook-database/blob/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite

Описание демо-базы данных
https://www.sqlitetutorial.net/sqlite-sample-database/

01.09.2023 Воссоздание базы данных Chinook
'''

# Импортируем библиотеку, соответствующую типу нашей базы данных
import sqlite3
from Sqlite_const import *
from pfile import *
from pstring import *

class MySqlite3_Chinook():
    def __init__(self, work_name:str):
        self.clear_db_file(work_name = work_name)
        self.db_name = work_name
        # Создаем соединение с нашей базой данных
        # В нашем примере у нас это просто файл базы
        self.conn = sqlite3.connect(self.db_name)
        # Создаем курсор - это специальный объект который делает запросы и получает их результаты
        self.cursor = self.conn.cursor()
        self.clear_all_tables()
        self.num_tables = len(tables_list)
        print('Object initialized')

    def work_frame(self):
        # self.cursor.execute("PRAGMA foreign_keys = off;")
        # self.cursor.execute("BEGIN TRANSACTION;")
        # www.geeksforgeeks.org/string-alignment-in-python-f-string/
        self.creating_tables()

            # self.cursor.execute("COMMIT TRANSACTION;")
        # self.cursor.execute("PRAGMA foreign_keys = on;")

    def creating_tables(self):
        all_tables = []
        for i in range(self.num_tables):
            # print(f"{i:2}  {tables_list[i]:>15}")
            res = self.create_table(tables_list[i])
            all_tables.append(res)
        if all:
            print('Все таблицы созданы')
        else:
            notall_tables= [not elem for elem in all_tables]

    def clear_db_file(self, work_name:str):
        '''
        https://sky.pro/media/udalenie-fajla-ili-papki-v-python/
        '''
        delete_file(work_name)

    def clear_all_tables(self):
        '''
        https://stackoverflow.com/questions/38672579/delete-all-tables-from-sqlite-database
        '''
        # ------- 1 вариант
        for table_name in tables_list:
            self.cursor.execute("DROP TABLE IF EXISTS " + table_name+';')

    def create_prf_full_table_name_sql(self)->str:
        match sql_exprt_prg:
            case SqlExprtPrgType.full_SQLiteStudio:
                prf_name = 'fS'
            case SqlExprtPrgType.short_SQLiteStudio:
                prf_name = 'sS'
            case SqlExprtPrgType.dbeaver:
                prf_name = 'dbeav'
            case _:
                prf_name = ''
        return prf_name

    def create_full_table_name_sql(self, table_name:str)->str:
        global sql_export_list
        prf_name = self.create_prf_full_table_name_sql()
        s = "\\".join([dat_dir, prf_name+table_name+'_create.sql']) #   print(s)
        return s


    def create_table(self, table_name:str)->bool:
        create_full_table_name_sql = self.create_full_table_name_sql(table_name)
        if file_exist(create_full_table_name_sql):
            ss = self.load_create_table_sql(create_full_table_name_sql)
            # https://habr.com/ru/articles/321510/
            self.cursor.executescript(ss)
            return True
        else:
            print(f' Файл {create_full_table_name_sql} не найден')
            return False

    def load_create_table_sql(self, create_full_table_name_sql:str)->str:
        f = open(create_full_table_name_sql, 'r')
        ss= f.read()
        f.close()
        return ss


class_exem = MySqlite3_Chinook(my_db_fn)
class_exem.work_frame()

# class_exem = MySqlite3(ini_fn)
# class_exem.work(5,'Начальный вариант')
