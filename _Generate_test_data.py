from random import randint
import random, string


def generator(func):
	def wrapper(*args, **kwargs):
		with open('test_data.txt', 'w') as ouf:
			result = func(*args, **kwargs)
			ouf.write(result)
	return wrapper


@generator
def generate_quick_sort_data():
	startings = [randint(-1e8, 1e8) for i in range(int(5e4))]
	endings = [randint(startings[i], 1e8) for i in range(len(startings))]
	lines = [[startings[i], endings[i]] for i in range(len(startings))]
	points = [randint(-1e8, 1e8) for i in range(int(5e4))]
	write_list = [(str(len(lines)), str(len(points)))]
	for i in lines:
		write_list.append(tuple(map(str, i)))
	write_list.append(tuple(map(str, points)))
	to_write = ''
	for i in write_list:
		to_write += ' '.join(i)
		if len(i) < 10:
			to_write += '\n'
	return to_write


@generator
def generate_random_select_data():
	total = int(1e6)
	target_index = randint(0, total)
	numbers = [str(randint(-1e9, 1e9)) for i in range(total)]
	to_write = f'{total} \n' 
	to_write += f'{target_index} \n'
	to_write += ' '.join(numbers)
	return to_write


@generator
def generate_heap_sort_data():
	to_write = str()
	total = int(1e6)
	to_write = f'{total} \n' 
	lst = [str(randint(-1e9, 1e9)) for i in range(total)]
	to_write += ' '.join(lst)
	return to_write


@generator
def generate_count_sort_data():
	total = int(1e4)
	to_write = f'{total} \n' 
	lst = [str(randint(1, 10)) for i in range(total)]
	to_write += ' '.join(lst)
	return to_write


@generator
def generate_lis_data():
	limit = int(1e5)
	to_write = str(limit) + '\n'
	array = [str(randint(0, 1e9)) for i in range(limit)]
	to_write += ' '.join(array)
	return to_write


@generator
def generate_editing_data():
	length_1  = randint(0, 1e2)
	length_2 = randint(0, 1e2)
	letters = string.ascii_lowercase
	to_write = ''.join(random.choice(letters) for i in range(length_1))
	to_write += '\n'
	to_write += ''.join(random.choice(letters) for i in range(length_2))
	return to_write


@generator
def generate_knapsack_data():
	n = 10
	weigths = ' '.join([str(randint(0, 20)) for i in range(n)])
	capacity = str(20) + ' '
	# n = randit(1, 3e2)
	# weigths = ' '.join([str(randint(0, 1e5)) for i in range(n)])
	# capacity = str(randint(1, 1e4)) + ' '
	capacity += str(n)
	to_write = capacity + '\n' + weigths
	return to_write


if __name__ == '__main__':
	pass
