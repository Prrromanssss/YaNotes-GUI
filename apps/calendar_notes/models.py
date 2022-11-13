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


class CalendarNotesModel:
    @staticmethod
    def select_all():
        con = sqlite3.connect('YaNotes.sqlite3')
        request = '''SELECT * FROM calendar_notes
                  '''
        data = con.execute(request).fetchall()
        con.commit()
        return data

    @staticmethod
    def delete_entry(*, entry_id):
        con = sqlite3.connect('YaNotes.sqlite3')
        request = f'''DELETE
                      FROM calendar_notes
                      WHERE id = {entry_id}
                   '''
        con.execute(request)
        con.commit()

    @staticmethod
    def insert(*, login, event, gmt, datetime, flag_to_send):
        con = sqlite3.connect('YaNotes.sqlite3')
        user_id = users_model.select_user_id(login=login)
        request = f'''INSERT INTO calendar_notes
                         (user_id, event, gmt, datetime, flag_to_send)
                     VALUES
                         ({user_id}, '{event}', {gmt},
                         '{datetime}', {flag_to_send})
                  '''
        con.execute(request)
        con.commit()

    @staticmethod
    def update_flag_to_send(*, login, flag_to_send):
        con = sqlite3.connect('YaNotes.sqlite3')
        user_id = users_model.select_user_id(login=login)
        request = f'''UPDATE calendar_notes
                      SET flag_to_send = {flag_to_send}
                      WHERE user_id = {user_id}
                   '''
        con.execute(request)
        con.commit()

    @staticmethod
    def select(*, login):
        con = sqlite3.connect('YaNotes.sqlite3')
        user_id = users_model.select_user_id(login=login)
        request = f'''SELECT * FROM calendar_notes
                      WHERE user_id = {user_id}
                   '''
        data = con.execute(request).fetchall()
        con.commit()
        return data

    @staticmethod
    def update_chat_id(*, chat_id, login):
        con = sqlite3.connect('YaNotes.sqlite3')
        user_id = users_model.select_user_id(login=login)
        request = f'''UPDATE calendar_notes
                      SET chat_id = {chat_id}
                      WHERE user_id = {user_id}
                   '''
        con.execute(request)
        con.commit()


calendar_notes_model = CalendarNotesModel()
users_model = UsersModel()
