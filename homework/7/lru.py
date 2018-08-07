import collections


class LRUCache:

	"""docstring for LRUCache"""

	def __init__(self, n):
		self.cache_size = n
		self.cache = collections.OrderedDict()
	
	def set(self, key, value):

		# добавляет значение value по ключу key. 
		# Общий размер кэша не должен превысить n. 
		# Для этого нужно удалять наиболее давно использованные ключи, 
		# когда кэш достигнет размера n.
		
		if len(self.cache) == self.cache_size:
			self.cache.popitem(last=False)

		self.cache.update({key:value})
		
	def get(self, key):

		# возвращает value, соответствующее данному ключу.

		self.cache.move_to_end(key, True)

		return self.cache.get(key)
