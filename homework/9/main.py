from control import Session
from control import ProgressAndStatus
from get_users import GetUsers

geo = {
        1:{'city_name':'Алма-Ата','population':1787964,'vk_city_id':183},
        2:{'city_name':'Астана','population':1020722,'vk_city_id':14},
        3:{'city_name':'Шымкент','population':912300,'vk_city_id':3193},
        4:{'city_name':'Караганда', 'population':501129,'vk_city_id':284},
        5:{'city_name':'Актобе','population':417471,'vk_city_id':1517767},
        6:{'city_name':'Тараз', 'population':357577,'vk_city_id':730},
        7:{'city_name':'Павлодар', 'population':344720,'vk_city_id':536},
        8:{'city_name':'Усть-Каменогорск', 'population':328294,'vk_city_id':205},
        9:{'city_name':'Семей', 'population':321159,'vk_city_id':361},
        10:{'city_name':'Кызылорда', 'population':267750,'vk_city_id':1517642}
    }

session = Session()
progress = ProgressAndStatus()

def print_bunch(users):
    print('Users', users)
    for user in users.get_users():
        print('User:', user.user_vk_id, 'Photo links', len(user.get_photos_links()),'\n')

for geo_id in range(1, 11):
    vk_city_id = geo[geo_id]['vk_city_id']
    city_name = geo[geo_id]['city_name']
    for sex_id in range(3):
        sex = sex_id
        for birth_year_int in range(1980, 2001):
            birth_year = birth_year_int
            users = GetUsers(vkapi=session.get_vk_session(), queue_limit=10)
            users.get_users(vk_city_id, city_name, sex, birth_year)
            print_bunch(users)
            # break
        break
    break




