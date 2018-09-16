import vk
import getpass


APP_ID = 6693960


def get_user_login():
    return input('Enter your login: ')


def get_user_password():
    return getpass.getpass('Enter your password: ')


def get_online_friends(login, password):
    api_version = '5.85'
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends',
    )
    api = vk.API(session, v=api_version)
    friends_online_ids = api.friends.getOnline()
    return api.users.get(user_ids=friends_online_ids)


def output_friends_to_console(friends_online):
    if not friends_online:
        print('None of your friends is online')
    else:
        print('Currently online: ')
        for friend in friends_online:
            print('{f[first_name]} {f[last_name]}'.format(f=friend))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    try:
        friends_online = get_online_friends(login, password)
        output_friends_to_console(friends_online)
    except vk.exceptions.VkAuthError:
        print('Login or password is incorrect')
