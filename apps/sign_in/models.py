import sqlite3

from settings import DATABASE


class UsersModel:
    @staticmethod
    def select_user(*, login):
        con = sqlite3.connect(DATABASE)
        request = f'''SELECT * FROM users
                      WHERE login = '{login}'
                   '''
        data = con.execute(request).fetchall()
        con.commit()
        return data


users_model = UsersModel()
