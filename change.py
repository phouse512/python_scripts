hash_map = {}

def change_possibilities(amount, denominations):

	key = str((amount,denominations))
	if hash_map.has_key(key):
		print "using memo"
		return hash_map[key]

	if amount == 0: return 1

	# we overshoot, we can't use this coin to do this
	if amount < 0: return 0

	# there are no more coins to test
	if len(denominations) == 0: return 0

	print "checking if we can make %i from %s" % (amount, denominations)

	current_coin, rest_of_coins = denominations[0], denominations[1:]

	possible = 0
	while amount >= 0:
		possible += change_possibilities(amount, rest_of_coins)
		amount -= current_coin

	hash_map[key] = possible
	return possible

print change_possibilities(10,[1,2,3])


print change_possibilities(100, range(1,100))