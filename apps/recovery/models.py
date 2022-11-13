import sqlite3


class UsersModel:
    @staticmethod
    def update_password_of_the_user(*, login, password):
        con = sqlite3.connect('YaNotes.sqlite3')
        request = f'''UPDATE users
                      SET password = '{password}'
                      WHERE login = '{login}' '''
        con.execute(request)
        con.commit()

    @staticmethod
    def select_all_user_data(*, login):
        con = sqlite3.connect('YaNotes.sqlite3')
        request = f'''SELECT * FROM users
                      WHERE login = '{login}'
                   '''
        data = con.execute(request).fetchall()
        con.commit()
        return data


users_model = UsersModel()
