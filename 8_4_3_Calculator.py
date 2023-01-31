from _Generate_test_data import generate_calc_data
from sys import stdin


def main():
	reader = (line for line in stdin)
	# n = int(next(reader))
	n = 96234
	values, mutations, preds = calculate_mutations(target = n)
	print(values)
	print(mutations)
	print(preds)

def calculate_mutations(target: int):
	values = [1]
	mutations = [0]
	predecessors = [None]
	i = 0
	while True:
		additing = values[i] + 1
		value_checker(value = additing, i = i, values = values, mutations = mutations, predecessors = predecessors)
		if additing == target:
			return values, mutations, predecessors
		mult_x2 = values[i] * 2
		value_checker(value = mult_x2, i = i, values = values, mutations = mutations, predecessors = predecessors)
		if additing == target:
			return values, mutations, predecessors
		mult_x3 = values[i] * 3
		value_checker(value = mult_x3, i = i, values = values, mutations = mutations, predecessors = predecessors)
		if additing == target:
			return values, mutations, predecessors
		i += 1
		print(values)
		print(mutations)
		print(predecessors)
		print('---------------')			

def value_checker(value: int, i: int, values: list, mutations: list, predecessors: list):
	# print(value, values, i)
	if value not in values:
		# print(f'im here with {value}')
		values.append(value)
		mutations.append(mutations[i] + 1)
		predecessors.append(i)
	else:
		# print(f'im checking {value}')
		index = values.index(value)
		mutations[index] = min(
		mutations[index],
		mutations[i] + 1)
		predecessors[index] = i
	# print('------------------')

if __name__ == '__main__':
	# generate_calc_data()
	main()
