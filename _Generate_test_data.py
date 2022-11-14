from random import randint


def generate_test_data():
	with open('test_data.txt', 'w') as ouf:
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
		ouf.write(to_write)


if __name__ == '__main__':
	generate_test_data()