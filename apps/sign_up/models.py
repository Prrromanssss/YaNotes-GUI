import sqlite3

from settings import DATABASE


class UsersModel:
    @staticmethod
    def insert_new_user(*, login, password, email):
        con = sqlite3.connect(DATABASE)
        request = f'''INSERT INTO users
                          ('login', 'password', 'email')
                      VALUES ('{login}', '{password}', '{email}')
                   '''
        con.execute(request)
        con.commit()


users_model = UsersModel()
