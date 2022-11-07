from ..core.exceptions import ValidationError

keywords = ['qwertyuiop[]\\', 'asdfghjkklжэё;\'`\'', 'zxcvbnm,./',
            '`1234567890-=', 'йцукенгшщзхъ\\', 'фывапролджэ',
            'чсмитьбю.жэё']


def validate_login(login, con):
    login = login.strip()
    request = f'''SELECT login from users
                  WHERE login = '{login}' '''
    data = con.execute(request).fetchall()
    if len(data) < 1:
        raise ValidationError('Such login doesn\'t exist. You need to sign up')
    assert len(data) == 1, 'Some users have the same login'
    return login


def validate_password(password1, password2, con=None):
    if password1 != password2:
        raise ValidationError('Passwords not the same')
    password = password1
    if len(password) < 9:
        raise ValidationError('The password is too short')
    elif not all([any([_.islower() for _ in password]),
                  any([_.isupper() for _ in password])]):
        raise ValidationError(
            'The password must contain characters of different case')
    elif not any([_.isnumeric() for _ in password]):
        raise ValidationError('The password must contain at least 1 digit')
    elif not all([password[k:k + 3].lower() not in x
                 for k in range(len(password) - 2)
                  for x in keywords]):
        raise ValidationError(
            'Combination of 3 letters standing side by side'
            'in the keyboard line is not allowed')
    else:
        return password
