def fib_mod(n, m):

	### Граничные условия задачи
	
	fib_list = (0, 1)
	rest_list = (0, 1)
	period = 0
	
	if n == 1:
		return 1

	### Ищем период Пизано

	for i in range(2, 6*m+3):

		fib_last_number = fib_list[0] + fib_list[1]
		fib_list = (fib_list[1], fib_last_number)

		last_rest_number = fib_last_number % m
		rest_list = (rest_list[1], last_rest_number)

		period += 1

		if rest_list == (0, 1):
			break

	### Ищем n-ый член, от которого нужно взять остаток
	
	required_n = n % period
	fib_list = (0, 1)

	if required_n in fib_list:
		return fib_list[required_n]

	for i in range(2, required_n+1):

		fib_last_number = fib_list[0] + fib_list[1]
		if i == required_n:
			return fib_last_number % m
		fib_list = (fib_list[1], fib_last_number)
	

def main():
	while True:
		n, m = map(int, input().split())
		print(fib_mod(n, m))


if __name__ == "__main__":
	main()
