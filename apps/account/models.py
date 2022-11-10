import sqlite3


class UsersModel:
    @staticmethod
    def insert_image(file, login):
        con = sqlite3.connect('YaNotes.sqlite3')
        request = f'''UPDATE users
                      SET image = '{file}'
                      WHERE login = '{login}' '''
        con.execute(request)
        con.commit()

    @staticmethod
    def delete_user(login):
        con = sqlite3.connect('YaNotes.sqlite3')
        request = f'''DELETE FROM users
                      WHERE login = '{login}' '''
        con.execute(request)
        con.commit()


users_model = UsersModel()
