from instaloader import Instaloader, Profile, TwoFactorAuthRequiredException
from instabot.config import *


class Insta:
    def __init__(self):
        self.loader = Instaloader()
        try:
            self.loader.load_session_from_file(USER, f'session-{USER}')
        except FileNotFoundError:
            self.loader.context.log("Session file does not exist yet - Logging in.")
        if not self.loader.context.is_logged_in:
            try:
                self.loader.login(USER, PASSWORD)
            except TwoFactorAuthRequiredException:
                self.loader.two_factor_login(input('Code: '))
            self.loader.save_session_to_file(f'session-{USER}')
        if self.loader.context.is_logged_in:
            self.loader.context.log('Logged in.', end='\n' * 2)

    def get_unfollowers(self, user):
        self.loader.context.log('Getting list of accounts i\'m subscribed to but not subscribed to me:')
        profile = Profile.from_username(self.loader.context, user)

        followers = profile.get_followers()
        followees = profile.get_followees()

        unfollowers = set(followees).difference(set(followers))
        unfollowers_list = []

        for unfollower in unfollowers:
            unfollowers_list.append(f'{unfollower.full_name} @{unfollower.username}')

        return '\n'.join(unfollowers_list)
