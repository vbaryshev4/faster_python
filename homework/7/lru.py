class LRUCache:

	"""docstring for LRUCache"""

	def __init__(self, n):
		self.cache_size = n
		self.keys_log = []
		self.cache = {}
	
	def set(self, key, value):

		# добавляет значение value по ключу key. 
		# Общий размер кэша не должен превысить n. 
		# Для этого нужно удалять наиболее давно использованные ключи, 
		# когда кэш достигнет размера n.
		
		if len(self.cache) == self.cache_size:
			key_to_delete = self.keys_log.pop(0)
			self.cache.pop(key_to_delete)

		self.cache.update({key:value})
		self.keys_log.append(key)
		
	def get(self, key):

		# возвращает value, соответствующее данному ключу.
		self.keys_log.remove(key)
		self.keys_log.append(key)

		return self.cache.get(key)
		