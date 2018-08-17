import uuid
import vk
import os


class Session:
    """docstring for Session"""
    def __init__(self, login, password, vk_id):
        self.login = login
        self.password = password
        self.vk_id = vk_id
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
        self.path = '/Users/vbaryshev/Documents/Computer_Science/Kirill/faster_python/homework/9/VisionLabs/'
        
    def __get_log(self, path):
        folder_content = os.listdir(path)
        result = folder_content.copy()
        result.remove('.DS_Store') 
        if result is None:
            return []
        return result

    def get_users_log(self):
        result = self.__get_log(self.path)
        return result

    def plus_to_count(self):
        self.users_count += 1        

    def get_status(self):
        return {'status': len(self.get_users_log()), 'limit': self.users_limit}


# a = ProgressAndStatus()
# print(a.get_status())
# print(a.plus_to_count())
# print(a.get_status())
# print(a.log)
# print(a.get_status())

