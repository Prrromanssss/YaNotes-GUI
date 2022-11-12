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


class TextNotesModel:
    @staticmethod
    def page_already_exist(*, folder_id, page):
        con = sqlite3.connect('YaNotes.sqlite3')
        request = f'''SELECT id FROM text_notes
                      WHERE folder_id = {folder_id}
                      AND page = {page}
                    '''
        data = con.execute(request).fetchall()
        con.commit()
        return data

    @staticmethod
    def insert(*, text, folder_id, page, title_of_the_page):
        con = sqlite3.connect('YaNotes.sqlite3')

        data = text_notes_model.page_already_exist(
            folder_id=folder_id,
            page=page,
        )
        if data:
            request = f'''UPDATE text_notes
                          SET text = '{text}',
                              title_of_the_page = '{title_of_the_page}'
                          WHERE id = {data[0][0]}
                       '''
        else:
            request = f'''INSERT INTO text_notes
                              (text, folder_id, page, title_of_the_page)
                          VALUES ('{text}', {folder_id}, {page},
                              '{title_of_the_page}')
                       '''
        con.execute(request)
        con.commit()

    @staticmethod
    def select(*, folder_id):
        con = sqlite3.connect('YaNotes.sqlite3')
        request = f'''SELECT * FROM text_notes
                      WHERE folder_id = {folder_id}
                      ORDER BY page
                   '''
        data = con.execute(request).fetchall()
        con.commit()
        return data

    @staticmethod
    def update_title_of_the_page(*, folder_id, title_of_the_page, page):
        con = sqlite3.connect('YaNotes.sqlite3')
        request = f'''UPDATE text_notes
                      SET title_of_the_page = '{title_of_the_page}'
                      WHERE folder_id = {folder_id} AND page = {page}'''
        con.execute(request)
        con.commit()


class ListTextNotesModel:
    @staticmethod
    def insert(*, folder, title_of_the_folder, login):
        con = sqlite3.connect('YaNotes.sqlite3')
        user_id = users_model.select_user_id(login=login)
        request = f'''INSERT INTO list_text_notes
                          (user_id, folder, title_of_the_folder)
                      VALUES ({user_id}, {folder}, '{title_of_the_folder}')
                           '''
        con.execute(request)
        con.commit()

    @staticmethod
    def select(*, login):
        con = sqlite3.connect('YaNotes.sqlite3')
        user_id = users_model.select_user_id(login=login)
        request = f'''SELECT * FROM list_text_notes
                      WHERE user_id = {user_id}
                      ORDER BY folder
                   '''
        data = con.execute(request).fetchall()
        con.commit()
        return data

    @staticmethod
    def select_foreign_key_text_notes(*, login, title_of_the_folder):
        con = sqlite3.connect('YaNotes.sqlite3')
        user_id = users_model.select_user_id(login=login)
        request = f'''SELECT text_notes.id, text_notes.text,
                          text_notes.folder_id,
                          text_notes.page, text_notes.title_of_the_page
                      FROM text_notes
                      INNER JOIN list_text_notes
                      ON text_notes.folder_id = list_text_notes.id
                      WHERE list_text_notes.user_id = {user_id}
                      AND list_text_notes.title_of_the_folder =
                          '{title_of_the_folder}'
                      ORDER BY text_notes.page
                   '''
        data = con.execute(request).fetchall()
        con.commit()
        return data

    @staticmethod
    def check_unique_title(*, login, title_of_the_folder):
        con = sqlite3.connect('YaNotes.sqlite3')
        user_id = users_model.select_user_id(login=login)
        request = f'''SELECT id
                     FROM list_text_notes
                     WHERE user_id = {user_id}
                     AND title_of_the_folder = '{title_of_the_folder}'
                    '''
        data = con.execute(request).fetchall()
        con.commit()
        return data

    @staticmethod
    def update_title_of_the_folder(*, entry_id, new_title):
        con = sqlite3.connect('YaNotes.sqlite3')
        request = f'''UPDATE list_text_notes
                      SET title_of_the_folder = '{new_title}'
                      WHERE id = {entry_id}
                  '''
        con.execute(request).fetchall()
        con.commit()

    @staticmethod
    def cascade_delete_folder(*, entry_id):
        con = sqlite3.connect('YaNotes.sqlite3')
        request = f'''DELETE FROM
                          list_text_notes
                      WHERE id = {entry_id}
                   '''
        con.execute(request)

        request = f'''DELETE FROM
                          text_notes
                      WHERE folder_id = {entry_id}
                   '''
        con.execute(request)
        con.commit()


text_notes_model = TextNotesModel()
users_model = UsersModel()
list_text_notes_model = ListTextNotesModel()
