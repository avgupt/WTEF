def decorate_divide(func):
	def decorated(a, b):
		if b == 0:
			print("Division by 0")
			return 0;
		return func(a, b)
	return decorated

def divide(x, y):
	return x // y

decorated_divide = decorate_divide(divide)

print(decorated_divide(6, 3))
print(decorated_divide(2, 0))
