import re

username = input("Insert your username: ")

password = input("Insert your password: ")
email = input("Insert your e-mail address: ")

reg_express_username = re.compile(r"[a-zA-Z]{6,10}")
reg_express_password = re.compile(r"[a-zA-Z_\-\.\+=]{12,30}")
reg_express_email = re.compile(r"^[\"]?[a-zA-Z0-9_]+[\+\"\.\+\-]?\w+[\"]?@[\[]?\w+[\-]?\w+\.[a-vx-z0-9]+.\w+[\.]?\d{0,3}[\]]?$")

check_username = reg_express_username.fullmatch(username)
check_password = reg_express_password.fullmatch(password)
check_email = reg_express_email.fullmatch(email)

if check_username:
    print(f'The username * {username.upper()} * is valid.')
else:
    print(f'The username * {username.upper()} * is not valid. Please try again.')

if check_password:
    print(f'The password is valid.')
else:
    print(f'The password is not valid. Please try again.')

if check_email:
    print(f'The e-mail address * {email.upper()} * is valid.')
else:
    print(f'The e-mail address * {email.upper()} * is not valid. Please try again.')
