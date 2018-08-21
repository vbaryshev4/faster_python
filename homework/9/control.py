import vk
import os


class Session:
    """docstring for Session"""
    def __init__(self, login, password, vk_id):
        self.login = login
        self.password = password
        self.vk_id = vk_id
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
        self.users_limit = 256
        self.path = '/Users/vbaryshev/Documents/Computer_Science/Kirill/faster_python/homework/9/VisionLabs/'
        
    def get_users_log(self):

        def __get_log(path):
            folder_content = os.listdir(path)

            if folder_content is None:
                return []

            r = folder_content.copy()
            trash = ['.DS_Store', 'Photos']
            for i in folder_content:
                if i in trash:
                    r.remove(i)
            return r

        return __get_log(self.path)

    def get_status(self):
        return {'status': len(self.get_users_log()), 'users_limit': self.users_limit}


if __name__ == '__main__':
    a = ProgressAndStatus()
    print(a.get_status())
    print(a.get_status())
    print(a.get_status())
    print(a.get_users_log())