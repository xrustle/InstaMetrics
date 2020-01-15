from instaloader import Instaloader, Profile, TwoFactorAuthRequiredException
import json

with open('config.json') as json_data_file:
    conf = json.load(json_data_file)
    USER = conf['credentials']['username']
    PASSWORD = conf['credentials']['password']

loader = Instaloader()

# login
try:
    loader.load_session_from_file(USER, f'session-{USER}')
except FileNotFoundError:
    loader.context.log("Session file does not exist yet - Logging in.")
if not loader.context.is_logged_in:
    try:
        loader.login(USER, PASSWORD)
    except TwoFactorAuthRequiredException:
        loader.two_factor_login(input('Code: '))
    loader.save_session_to_file(f'session-{USER}')
if loader.context.is_logged_in:
    loader.context.log('Logged in.', end='\n' * 2)





if __name__ == '__main__':
    print('\t', *get_unfollowers(USER), sep='\n\t')
