import sqlite3


class UsersModel:
    @staticmethod
    def insert_new_user(*, login, password, email):
        con = sqlite3.connect('YaNotes.sqlite3')
        request = f'''INSERT INTO users
                      ('login', 'password', 'email')
                      VALUES ('{login}', '{password}', '{email}')'''
        con.execute(request)
        con.commit()


users_model = UsersModel()
