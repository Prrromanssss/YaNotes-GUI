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

    @staticmethod
    def insert_image(*, file, login):
        con = sqlite3.connect('YaNotes.sqlite3')
        request = f'''UPDATE users
                      SET image = '{file}'
                      WHERE login = '{login}' 
                   '''
        con.execute(request)
        con.commit()

    @staticmethod
    def delete_user(*, login):
        con = sqlite3.connect('YaNotes.sqlite3')

        user_id = users_model.select_user_id(login=login)
        request = f'''DELETE FROM users
                      WHERE id = {user_id}
                   '''
        con.execute(request)

        request = f'''DELETE FROM list_text_notes
                      WHERE user_id = {user_id}
                   '''
        con.execute(request)

        request = f'''DELETE FROM list_table_notes
                      WHERE user_id = {user_id}
                   '''
        con.execute(request)

        con.commit()


users_model = UsersModel()
