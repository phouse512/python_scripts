hash_map = {}

# dynamic programming

def fib(n):
	key = str(n)
	if hash_map.has_key(key):
		print "grabbing from hash"
		return hash_map[key]

	if n < 2:
		return n
	else:
		print "recursively calculating %i" % n
		val = fib(n-2) + fib(n-1)
		hash_map[key] = val
		return val

print fib(10)
