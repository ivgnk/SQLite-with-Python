'''
Константы для работы с SQLite
'''

from enum import Enum
class SqlExprtPrgType(Enum):
    full_SQLiteStudio = 0
    short_SQLiteStudio = 1
    dbeaver = 2

sql_exprt_prg = SqlExprtPrgType.full_SQLiteStudio

# sql_export_list = ['full_SQLiteStudio','short_SQLiteStudio',
#                    'dbeaver'] # для формирования имени файла для ввода
# sql_export_type = sql_export_list[0]
dat_dir = 'Dat'

ini_fn = 'Ini_Chinook_Sqlite.sqlite'
wrk_fn = 'Chinook_Sqlite.sqlite'
my_db_fn = 'MyChinook_Sqlite.db'
tables_list = ['albums','artists','customers','employees','genres','invoice_items',
               'invoices','media_types', 'playlist_track','playlists','tracks']

def create_dict_with_tables()->dict:
    '''
    https/stackoverflow.com/questions/35830612/how-to-create-a-new-dictionary-in-for-loop
    '''
    tables_dict:dict ={}
    i = 0
    for s in tables_list:
        tables_dict[s] =[]
        i += 1
    return tables_dict

def thetest_enum():
    '''
    2021 Гайд по использованию enum в Python
    https://habr.com/ru/companies/timeweb/articles/564826/
    '''
    print(0  == SqlExprtPrgType.full_SQLiteStudio)
    print(SqlExprtPrgType.full_SQLiteStudio == SqlExprtPrgType.full_SQLiteStudio)
    print(1  == SqlExprtPrgType.short_SQLiteStudio)
    print('\nMember name: {}'.format(SqlExprtPrgType.full_SQLiteStudio.name))
    print()
    print(type(SqlExprtPrgType.full_SQLiteStudio.name))
    print(type(SqlExprtPrgType.full_SQLiteStudio))
    print(type(SqlExprtPrgType))

    for status in SqlExprtPrgType:
        print('{:25} = {}'.format(status.name, status.value))
    for status in SqlExprtPrgType:
        print(f"{status.name:>18} = {status.value:2}")

if __name__ == "__main__":
    # print(tables_list)
    # print('-- main_dict --')
    # print(create_dict_with_tables())
    thetest_enum()
    pass

