math_expression = "5 * 5 + 3 * (2**4) + (5 - (3**2)) + ((100 * 10 / 1) / 10) - 24 + (4**4)"
string_array = []

for letter in math_expression:
	if letter == "*":
		string_array.append("times")
	elif letter == "/":
		string_array.append("divided by")
	elif letter == "^":
		string_array.append(" to the ")
	elif letter == "+":
		string_array.append("plus")
	elif letter == "-":
		string_array.append("minus")
	elif letter == '(':
		string_array.append("left parentheses ")
	elif letter == ')':
		string_array.append(" right parentheses")
	else:
		string_array.append(letter)


print "".join(string_array)
print eval(math_expression)
