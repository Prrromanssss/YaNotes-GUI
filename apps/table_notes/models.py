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
    @staticmethod
    def select_pages(*, table_id):
        con = sqlite3.connect('YaNotes.sqlite3')
        request = f'''SELECT page FROM table_notes
                      WHERE table_id = {table_id}
                      ORDER BY page
                    '''
        pages = con.execute(request).fetchall()
        con.commit()
        return pages

    @staticmethod
    def check_unique_title(*, table_id, title_of_the_page):
        con = sqlite3.connect('YaNotes.sqlite3')
        request = f'''SELECT id
                      FROM table_notes
                      WHERE table_id = {table_id}
                      AND title_of_the_page = '{title_of_the_page}'
                   '''
        data = con.execute(request).fetchall()
        con.commit()
        return data

    @staticmethod
    def select_file(*, entry_id):
        con = sqlite3.connect('YaNotes.sqlite3')
        request = f'''SELECT file
                      FROM table_notes
                      WHERE id = {entry_id}
                   '''
        data = con.execute(request).fetchall()
        con.commit()
        return data

    @staticmethod
    def update_title_of_the_page(*, entry_id, new_title):
        con = sqlite3.connect('YaNotes.sqlite3')
        request = f'''UPDATE table_notes
                      SET title_of_the_page = '{new_title}'
                      WHERE id = {entry_id}
                   '''
        con.execute(request)
        con.commit()

    @staticmethod
    def delete_page(*, entry_id):
        con = sqlite3.connect('YaNotes.sqlite3')
        request = f'''DELETE FROM
                          table_notes
                      WHERE id = {entry_id}
                  '''
        con.execute(request)
        con.commit()

    @staticmethod
    def insert(
        *, table_id, file, page, title_of_the_page, delimiter,
        quotechar, newline
    ):
        con = sqlite3.connect('YaNotes.sqlite3')
        request = f'''INSERT INTO table_notes
                          (table_id, file, page, title_of_the_page,
                           delimiter, quotechar, newline)
                      VALUES ({table_id}, '{file}', {page},
                      '{title_of_the_page}', '{delimiter}',
                      '{quotechar}', '{newline}')
                    '''
        con.execute(request)
        con.commit()

    @staticmethod
    def select_foreign_key_list_table_notes(*, table_id):
        con = sqlite3.connect('YaNotes.sqlite3')
        request = f'''SELECT table_notes.id, table_notes.file,
                                  table_notes.table_id,
                                  table_notes.page,
                                  table_notes.title_of_the_page,
                                  table_notes.delimiter, table_notes.quotechar,
                                  table_notes.newline
                              FROM table_notes
                              INNER JOIN list_table_notes
                              ON table_notes.table_id = list_table_notes.id
                              WHERE list_table_notes.id = {table_id}
                              ORDER BY table_notes.page
                           '''
        data = con.execute(request).fetchall()
        con.commit()
        return data


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
    def select_user_id(*, login):
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
    def select(*, login, title_of_the_table):
        con = sqlite3.connect('YaNotes.sqlite3')
        user_id = users_model.select_user_id(login=login)
        request = f'''SELECT * FROM list_table_notes
                      WHERE user_id = {user_id}
                      AND title_of_the_table = '{title_of_the_table}'
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

    @staticmethod
    def select_foreign_key_table_notes(*, login, title_of_the_table):
        con = sqlite3.connect('YaNotes.sqlite3')
        user_id = users_model.select_user_id(login=login)
        request = f'''SELECT table_notes.id, table_notes.file,
                              table_notes.table_id,
                              table_notes.page, table_notes.title_of_the_page
                          FROM table_notes
                          INNER JOIN list_table_notes
                          ON table_notes.table_id = list_table_notes.id
                          WHERE list_table_notes.user_id = {user_id}
                          AND list_table_notes.title_of_the_table =
                              '{title_of_the_table}'
                          ORDER BY table_notes.page
                       '''
        data = con.execute(request).fetchall()
        con.commit()
        return data


table_notes_model = TableNotesModel()
users_model = UsersModel()
list_table_notes_model = ListTabelNotesModel()
