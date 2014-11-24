from stack import Stack


def bracket_validator(string):
	stack = Stack()
	opener = ['(', '{', '[']
	closer = [')', '}', ']']

	close_dict = { 
		'(': ')',
		'{': '}',
		'[': ']'
	}

	for element in string:
		if element in opener:
			stack.push(element)
		elif element in closer:
			result = stack.pop()
			if close_dict[result] != element:
				return "no dice"

	return "dice"


string = "{ [ ( ] ) }"
print bracket_validator(string)

string2 = "{ [ }"
print bracket_validator(string2)

string3 = "{ [ ] ( ) }"
print bracket_validator(string3)

