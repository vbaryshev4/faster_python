from lru import LRUCache

if __name__ == '__main__':
	
	cache_limit = 4
	cache = LRUCache(4)

	for i in range(cache_limit*3):
		cache.set(i, '{0}00'.format(i))
		print(cache.keys_log)
		if i % 2 == 0:
			print('get of key 0 and return value', cache.get(0))
		print(cache.cache)

# STD_OUT
# [0]
# get of key 0 and return value 000
# {0: '000'}
# [0, 1]
# {0: '000', 1: '100'}
# [0, 1, 2]
# get of key 0 and return value 000
# {0: '000', 1: '100', 2: '200'}
# [1, 2, 0, 3]
# {0: '000', 1: '100', 2: '200', 3: '300'}
# [2, 0, 3, 4]
# get of key 0 and return value 000
# {0: '000', 2: '200', 3: '300', 4: '400'}
# [3, 4, 0, 5]
# {0: '000', 3: '300', 4: '400', 5: '500'}
# [4, 0, 5, 6]
# get of key 0 and return value 000
# {0: '000', 4: '400', 5: '500', 6: '600'}
# [5, 6, 0, 7]
# {0: '000', 5: '500', 6: '600', 7: '700'}
# [6, 0, 7, 8]
# get of key 0 and return value 000
# {0: '000', 6: '600', 7: '700', 8: '800'}
# [7, 8, 0, 9]
# {0: '000', 7: '700', 8: '800', 9: '900'}
# [8, 0, 9, 10]
# get of key 0 and return value 000
# {0: '000', 8: '800', 9: '900', 10: '1000'}
# [9, 10, 0, 11]
# {0: '000', 9: '900', 10: '1000', 11: '1100'}
