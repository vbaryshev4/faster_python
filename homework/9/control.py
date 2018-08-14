import uuid
import vk


class Session:
    """docstring for Session"""
    def __init__(self):
        self.login = '+79262265269'
        self.password = 'Rfmclp76'
        self.vk_id = '6656799'
        # Setup session
        self.session = vk.AuthSession(
                app_id=self.vk_id, 
                user_login=self.login, 
                user_password=self.password
                ) 
        self.vkapi = vk.API(self.session)

    def get_vk_session(self):
        return self.vkapi


class ProgressAndStatus:
    """docstring for ProgressStatus"""
    def __init__(self):
        self.uuid = uuid.uuid1()
        self.users_limit = 256
        self.users_count = 0