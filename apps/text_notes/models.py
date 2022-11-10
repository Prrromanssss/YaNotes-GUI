import sqlite3


class TextNotesModel:
    @staticmethod
    def insert(*, text, login, page, title_of_the_page):
        con = sqlite3.connect('YaNotes.sqlite3')
        request_for_user_id = f'''SELECT id FROM users
                              WHERE login = '{login}' '''
        user_id = con.execute(request_for_user_id).fetchone()[0]
        request = f'''INSERT INTO text_notes 
                     (text, user_id, page, title_of_the_page)
                     VALUES ('{text}', {user_id}, {page}, '{title_of_the_page}')
                   '''
        con.execute(request)
        con.commit()




text_notes_model = TextNotesModel()
