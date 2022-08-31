import math

glob_list = []

for n in (3, 100000):
	lst = []

	b = math.pow(math.log(n, 4), 0.5)
	lst.append(b)

	b = math.log(math.log2(n))
	lst.append(b)

	b = math.log(n, 3)
	lst.append(b)

	b = math.pow(math.log2(n), 2)
	lst.append(b)

	b = math.pow(n, 0.5)
	lst.append(b)

	b = n / math.log(n, 5)
	lst.append(b)

	b = math.log2(math.factorial(n))
	lst.append(b)

	b = math.pow(3, math.log2(n))
	lst.append(b)

	b = math.pow(n, 2)
	lst.append(b)

	b = math.pow(7, math.log2(n))
	lst.append(b)

	b = math.pow(math.log2(n), math.log2(n))
	lst.append(b)

	b = math.pow(n, math.log2(n))
	lst.append(b)

	# b = math.pow(n, math.pow(n, 0.5))
	# lst.append(b)

	# b = math.pow(2, n)
	# lst.append(b)

	# b = math.pow(4, n)
	# lst.append(b)

	# b = math.pow(2, 3*n)
	# lst.append(b)

	# b = float(math.factorial(n))
	# lst.append(b)

	# b = math.pow(2, math.pow(2, n))
	# lst.append(b)

	glob_list.append(lst)


for i in range(len(glob_list[0])):
	print(round((glob_list[1][i]/glob_list[0][i]), 2))



