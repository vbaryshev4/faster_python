from random import randint

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

class User:
	"""docstring for User"""
	def __init__(self, user_vk_id, vk_city_id, city_name):
		self.user_vk_id = user_vk_id
		self.vk_city_id = vk_city_id
		self.city_name = city_name
		

class GetUsers:
	"""docstring for GetUsers"""
	def __init__(self, vkapi, queue_limit):
		self.vkapi = vkapi
		self.users = None
		self.queue_limit = queue_limit

	def get_users(self):
		result = []
		city = geo[randint(1,10)]
		data = self.vkapi.users.search(count=self.queue_limit, city=city['vk_city_id'], coutry=4, v=5.80)
		for item in data['items']:
			person = User(item['id'], city['vk_city_id'], city['city_name'])
			result.append(person.user_vk_id)
		return result
		
