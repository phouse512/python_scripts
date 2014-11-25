import math

def reverse_string(string):
	string = list(string)
	length = int(math.floor(len(string)/2))

	for i in range(length):
		temp = string[i]
		string[i] = string[len(string) - i - 1]
		string[len(string) - i - 1] = temp

	return ''.join(string)


print reverse_string("abcdefg")
print reverse_string("yo")
print reverse_string("racecar")
print ""