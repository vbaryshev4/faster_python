from control import Session
from control import ProgressAndStatus
from get_users import GetUsers


session = Session()
progress = ProgressAndStatus()
users_ids = GetUsers(vkapi=session.get_vk_session(), queue_limit=10)
init_users = users_ids.get_users()
print(init_users)