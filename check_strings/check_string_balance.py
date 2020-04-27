# Script to check the string has balanced usage of parenthesis. 

from stacks import Stack

def is_match(a,b):
	if a == "(" and b == ")":
		return True
	elif a == "{" and b == "}":
		return True
	elif a == "[" and b == "]":
		return True
	else:
		return False

def is_balanced(string):
	s = Stack()
	is_balanced = True
	index = 0

	while index < len(string) and is_balanced:
		par = string[index]

		if par in "({[":
			s.push(par)
		else:
			if s.is_empty():
				is_balanced = False
			else:
				top = s.pop()

				if not is_match(top, par):
					is_balanced = False
		index +=1
	
	if 	s.is_empty and is_balanced:
		return True
	else:
		return False			


words = "{[())]}"
print(is_balanced(words))
