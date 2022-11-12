import sqlite3


class UsersModel:
    @staticmethod
    def select_user_id(*, login):
        con = sqlite3.connect('YaNotes.sqlite3')
        request = f'''SELECT id FROM users
                      WHERE login = '{login}' '''
        user_id = con.execute(request).fetchone()[0]
        con.commit()
        return user_id


class TableNotesModel:
    ...


class ListTabelNotesModel:
    @staticmethod
    def insert(*, table, title_of_the_table, login):
        con = sqlite3.connect('YaNotes.sqlite3')
        user_id = users_model.select_user_id(login=login)
        request = f'''INSERT INTO list_table_notes
                          (user_id, 'table', title_of_the_table)
                      VALUES ({user_id}, '{table}', '{title_of_the_table}')
                   '''
        con.execute(request)
        con.commit()

    @staticmethod
    def select(*, login):
        con = sqlite3.connect('YaNotes.sqlite3')
        user_id = users_model.select_user_id(login=login)
        request = f'''SELECT * FROM list_table_notes
                      WHERE user_id = {user_id}
                      ORDER BY 'table'
                    '''
        data = con.execute(request).fetchall()
        con.commit()
        return data

    @staticmethod
    def check_unique_title(*, login, title_of_the_table):
        con = sqlite3.connect('YaNotes.sqlite3')
        user_id = users_model.select_user_id(login=login)
        request = f'''SELECT id
                      FROM list_table_notes
                      WHERE user_id = {user_id}
                      AND title_of_the_table = '{title_of_the_table}'
                   '''
        data = con.execute(request).fetchall()
        con.commit()
        return data

    @staticmethod
    def cascade_delete_folder(*, entry_id):
        con = sqlite3.connect('YaNotes.sqlite3')
        request = f'''DELETE FROM
                          list_table_notes
                      WHERE id = {entry_id}
                   '''
        con.execute(request)

        request = f'''DELETE FROM
                          table_notes
                      WHERE table_id = {entry_id}
                   '''
        con.execute(request)
        con.commit()

    @staticmethod
    def update_title_of_the_folder(*, entry_id, new_title):
        con = sqlite3.connect('YaNotes.sqlite3')
        request = f'''UPDATE list_table_notes
                      SET title_of_the_table = '{new_title}'
                      WHERE id = {entry_id}
                   '''
        con.execute(request)
        con.commit()


table_notes_model = TableNotesModel()
users_model = UsersModel()
list_table_notes_model = ListTabelNotesModel()
