def decorate_divide(func):
	def decorated(a, b):
		if b == 0:
			print("Division by 0")
			return 0;
		return func(a, b)
	return decorated

def divide(x, y):
	return x // y

@decorate_divide
def divide1(x, y):
	return x // y

decorated_divide = decorate_divide(divide)

print(decorated_divide(6, 3))
print(decorated_divide(2, 0))
print(divide1(24, 4))
print(divide1(9, 0))
