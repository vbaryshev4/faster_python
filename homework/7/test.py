from lru import LRUCache

if __name__ == '__main__':
	
	cache_limit = 4
	cache = LRUCache(cache_limit)

	for i in range(0, 10):
		cache.set(i, '{0}00'.format(i))
		if i % 2 == 0:
			print('Get a key', cache.get(0))
		print(cache.cache)

# STD_OUT
# Get a key 000
# OrderedDict([(0, '000')])
# OrderedDict([(0, '000'), (1, '100')])
# Get a key 000
# OrderedDict([(1, '100'), (2, '200'), (0, '000')])
# OrderedDict([(1, '100'), (2, '200'), (0, '000'), (3, '300')])
# Get a key 000
# OrderedDict([(2, '200'), (3, '300'), (4, '400'), (0, '000')])
# OrderedDict([(3, '300'), (4, '400'), (0, '000'), (5, '500')])
# Get a key 000
# OrderedDict([(4, '400'), (5, '500'), (6, '600'), (0, '000')])
# OrderedDict([(5, '500'), (6, '600'), (0, '000'), (7, '700')])
# Get a key 000
# OrderedDict([(6, '600'), (7, '700'), (8, '800'), (0, '000')])
# OrderedDict([(7, '700'), (8, '800'), (0, '000'), (9, '900')])