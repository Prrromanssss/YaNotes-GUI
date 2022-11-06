import re


class ValidationError(Exception):
    pass


keywords = ['qwertyuiop[]\\', 'asdfghjkklжэё;\'`\'', 'zxcvbnm,./',
            '`1234567890-=', 'йцукенгшщзхъ\\', 'фывапролджэ',
            'чсмитьбю.жэё']


def validate_email(email, con):
    request = f'''SELECT email from users
                  WHERE email = '{email}' '''
    data = con.execute(request).fetchall()
    if len(data) > 0:
        raise ValidationError('Such email already exists')
    email = email.strip()
    regex = re.compile(
        r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")"
        r"@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
    if re.fullmatch(regex, email):
        return email
    raise ValidationError('Not valid email')


def validate_password(password1, password2, con=None):
    if password1 != password2:
        raise ValidationError('Passwords not the same')
    password = password1
    if len(password) < 9:
        raise ValidationError('The password is too short')
    elif not all([any([_.islower() for _ in password]),
                  any([_.isupper() for _ in password])]):
        raise ValidationError('The password must contain characters of different case')
    elif not any([_.isnumeric() for _ in password]):
        raise ValidationError('The password must contain at least 1 digit')
    elif not all([password[k:k + 3].lower() not in x for k in range(len(password) - 2)
                  for x in keywords]):
        raise ValidationError('Combination of 3 letters standing side by side in the keyboard line is not allowed')
    else:
        return password


def validate_agreement(agreement, con=None):
    if not agreement:
        raise ValidationError('Confirm Personal Data Processing Policy')
    return True


def validate_login(login, con):
    login = login.strip()
    if not login:
        raise ValidationError('Not valid login')
    request = f'''SELECT login from users
                  WHERE login = '{login}' '''
    data = con.execute(request).fetchall()
    if len(data) > 0:
        raise ValidationError('Such login already exists')
    return login
